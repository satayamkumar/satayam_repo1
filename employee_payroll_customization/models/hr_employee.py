from odoo import api, fields, models
from datetime import date


class EmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    resignation_date = fields.Date(string="Resignation  Date")

    stage = fields.Selection(
        [('probation', 'Probation'),
         ('regular', 'Regular'),
         ('notice', 'Notice'),
         ('left', 'Left'),
         ('hold', 'Hold')],
        string='Employee Status',
    )
    probation_end_date  = fields.Date(string="Probation End  Date")

    # def _compute_stage(self):
    #     for employee in self:
    #         latest_payslip = self.env['hr.payslip'].search([
    #             ('employee_id', '=', employee.id)
    #         ], order='date_to desc', limit=1)
    #
    #         if latest_payslip:
    #             employee.stage = latest_payslip.Employee_Status or 'draft'
    #             print("employee.stage ",employee.stage)
    #         else:
    #             employee.stage = 'draft'
    #             print("employee.stage ", employee.stage)


