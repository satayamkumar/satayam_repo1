from odoo import models, fields, api, _
from odoo.exceptions import AccessError


class TsSecret(models.Model):
    _name = 'ts.secret'
    _description = 'Password Manager Secret'
    # _inherit = ['mail.thread', 'mail.followers.mixin']
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True)
    secret_line_ids = fields.One2many('ts.secret.line', 'secret_id', string='Secrets')
    active = fields.Boolean(string='Active', default=True)

