import logging
from odoo import models,api,fields
_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def send_missing_image_email(self):
        # Search for employees without image and with a valid email
        employees = self.search([
            ('image_1920', '=', False),
            ('work_email', '!=', False)
        ])
        # Load the email template
        template = self.env.ref('send_email_module.mail_template_employee_missing_image')
        print("template ",template)
        print("employees", employees)
        for employee in employees:
            template.send_mail(employee.id, force_send=True)