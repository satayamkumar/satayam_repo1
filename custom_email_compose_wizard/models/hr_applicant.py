from odoo import models, fields, api, _


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    def action_custom_button(self):
        self.ensure_one()
        print(" self ", self.id)
        # email_template_data_applicant_refuse
        # template_id = self.env.ref('hr_recruitment.email_template_data_applicant_refuse').id
        template_id = self.env.ref('custom_email_compose_wizard.custom_email_compose_wizard_template').id
        compose_form_id = self.env.ref('mail.email_compose_message_wizard_form').id
        print("template_id ", template_id)
        print("compose_form_id ", compose_form_id)
        ctx = {
            'default_model': 'hr.applicant',
            'default_res_id': self.id,
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'custom_layout': "mail.mail_notification_paynow",
            'force_email': False,
        }
        return {
            'type': 'ir.actions.act_window',
            'name': _('Send Email'),
            'res_model': 'mail.compose.message',
            'view_mode': 'form',
            'views': [(compose_form_id, 'form')],
            'target': 'new',
            'context': ctx,
        }
