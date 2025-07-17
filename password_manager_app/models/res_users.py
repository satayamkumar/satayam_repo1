# from odoo import models, fields, api, _
# from odoo.exceptions import AccessError
#
# # Inherit user archive to notify
# class ResUsers(models.Model):
#     _inherit = 'res.users'
#
#     def write(self, vals):
#         archived = vals.get('active') is False
#         result = super().write(vals)
#         if archived:
#             secrets = self.env['ts.secret'].search([])
#             user_partner = self.partner_id
#             user_secrets = secrets.filtered(lambda s: user_partner.id in s.message_follower_ids.mapped('partner_id').ids)
#             for secret in user_secrets:
#                 secret.message_post(
#                     body=_("A follower has been archived. Consider resetting credentials for security."),
#                     subtype_xmlid="mail.mt_note")
#         return result