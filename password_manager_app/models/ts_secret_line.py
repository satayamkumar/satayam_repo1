from odoo import models, fields, api, _
from odoo.exceptions import AccessError


class TsSecretLine(models.Model):
    _name = 'ts.secret.line'
    _description = 'Password Manager Secret Line'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    secret_id = fields.Many2one('ts.secret', string='Secret id', ondelete='cascade')
    name = fields.Char(string='Name', required=True)
    secret = fields.Char(string='Secret Password', required=True)
    secret_type = fields.Selection([
        ('email', 'Email'),
        ('username', 'Username'),
        ('password', 'Password'),
        ('url', 'URL'),
        ('token', 'Token'),
        ('api_key', 'API Key')
    ], string='Secret Type', required=True)
    active = fields.Boolean(string='Active', default=True)


    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super().fields_view_get(view_id, view_type, toolbar, submenu)
        user = self.env.user
        if not user.has_group('base.group_system') and not user.has_group('password_manager_app.group_password_manager_user'):
            raise AccessError(_('You do not have permission to access this page.'))
        return res

    # def read(self, fields=None, load='_classic_read'):
    #     result = super().read(fields, load)
    #     for record in result:
    #         record_id = record.get('id')
    #         if record_id:
    #             rec = self.browse(record_id)
    #             if self.env.user.id not in rec.secret_id.message_follower_ids.mapped('partner_id.user_ids').ids:
    #                 raise AccessError(_('You are not allowed to view this credential.'))
    #     return result