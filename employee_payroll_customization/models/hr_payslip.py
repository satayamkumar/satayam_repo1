import calendar
from datetime import date
from datetime import timedelta

from odoo import api, fields, models, _


# hr_payroll_community  this module for some code commented
# if any(self.filtered(lambda payslip: payslip.date_from > payslip.date_to)):
#     raise ValidationError(_("Payslip 'Date From' must be earlier 'Date To'."))
class PayslipInherit(models.Model):
    _inherit = 'hr.payslip'
    # Employee_Status = fields.Selection(
    #     [('probation', 'Probation'), ('regular', 'Regular'), ('notice', 'Notice'), ('left', 'Left')],
    #     string='Employee Status',
    #     compute='_compute_employee_status',
    #     store=True)
    Employee_Status = fields.Selection(
        [('probation', 'Probation'),
         ('regular', 'Regular'),
         ('notice', 'Notice'),
         ('left', 'Left'),
         ('hold', 'Hold')],  # Added hold
        string='Employee Status',
        compute='_compute_employee_status',
        store=True)

    date = fields.Date(default=fields.Date.today)

    @api.onchange('date_from')
    def _onchange_date_from(self):
        if self.date_from:
            year = self.date_from.year
            month = self.date_from.month
            # Get last day of the month
            last_day = calendar.monthrange(year, month)[1]
            self.date_to = date(year, month, last_day)

    # @api.depends('employee_id', 'employee_id.resignation_date', 'date', 'date_from', 'date_to')
    # def _compute_employee_status(self):
    #     for payslip in self:
    #         payslip.Employee_Status = False  # Default
    #         if not payslip.employee_id:
    #             continue
    #         employee = payslip.employee_id
    #         resignation_date = employee.resignation_date
    #         payslip_date = payslip.date or date.today()
    #         date_from = payslip.date_from
    #         contract_history = self.env['hr.contract.history'].search([
    #             ('employee_id', '=', employee.id),
    #             ('date_hired', '!=', False)
    #         ], limit=1, order='date_hired desc')
    #         # job = employee.job_id
    #         # notice_period_months = job.notice_period_number_of_months if job else None
    #         # print("notice_period_months ", notice_period_months)
    #         # notice_mapping = {
    #         #     'one month': 30,
    #         #     'two month': 60,
    #         #     'three month': 90,
    #         #     'four month': 120,
    #         # }
    #         job = employee.job_id
    #         month_to_days = {
    #             'one month': 30,
    #             'two month': 60,
    #             'three month': 90,
    #             'four month': 120,
    #
    #             'one_month': 30,
    #             'two_month': 60,
    #             'three_month': 90,
    #             'four_month': 120,
    #         }
    #         notice_period_days = 90  # default if not set
    #         probation_period_days = 120  # default if not set
    #         if job:
    #             if job.notice_period_number_of_months:
    #                 notice_period_days = month_to_days.get(job.notice_period_number_of_months, 90)
    #             if job.employee_probation_of_months:
    #                 probation_period_days = month_to_days.get(job.employee_probation_of_months, 120)
    #
    #         # notice_period_days = notice_mapping.get(notice_period_months, 90)  # Default 90 if not set
    #         print("notice_period_days ", notice_period_days)
    #         if resignation_date and date_from:
    #             ninety_days_after_resign = resignation_date + timedelta(days=notice_period_days)
    #             if resignation_date <= date_from <= ninety_days_after_resign:
    #                 employee.stage = 'probation'
    #                 payslip.Employee_Status = 'notice'
    #         # If not in notice period, check contract hiring date
    #         else:
    #             if contract_history and contract_history.date_hired and date_from:
    #                 joining_date = contract_history.date_hired
    #                 if (joining_date.month == date_from.month and
    #                         joining_date.year == date_from.year and
    #                         joining_date.day > 17):
    #                     employee.stage = 'hold'
    #                     payslip.Employee_Status = 'hold'
    #                     continue  # Skip further checks
    #             if contract_history:
    #                 hired_date = contract_history.date_hired
    #                 print('----hired_date', hired_date)
    #                 if hired_date:
    #                     probation_cutoff = hired_date + timedelta(days=probation_period_days)  # 4 months
    #                     if date_from < probation_cutoff:
    #                         employee.stage = 'probation'
    #                         payslip.Employee_Status = 'probation'
    #                     else:
    #                         employee.stage = 'regular'
    #                         payslip.Employee_Status = 'regular'



    @api.depends('employee_id', 'employee_id.resignation_date', 'date', 'date_from', 'date_to')
    def _compute_employee_status(self):
        for payslip in self:
            payslip.Employee_Status = False  # Default
            if not payslip.employee_id:
                continue
            employee = payslip.employee_id
            resignation_date = employee.resignation_date
            payslip_date = payslip.date or date.today()

            probation_end = employee.probation_end_date
            date_from = payslip.date_from
            contract_history = self.env['hr.contract.history'].search([
                ('employee_id', '=', employee.id),
                ('date_hired', '!=', False)
            ], limit=1, order='date_hired desc')
            # job = employee.job_id
            # notice_period_months = job.notice_period_number_of_months if job else None
            # print("notice_period_months ", notice_period_months)
            # notice_mapping = {
            #     'one month': 30,
            #     'two month': 60,
            #     'three month': 90,
            #     'four month': 120,
            # }
            job = employee.job_id
            month_to_days = {
                'one month': 30,
                'two month': 60,
                'three month': 90,
                'four month': 120,

                'one_month': 30,
                'two_month': 60,
                'three_month': 90,
                'four_month': 120,
            }
            notice_period_days = 0  # default if not set
            probation_period_days = 0  # default if not set
            if job:
                if job.notice_period_number_of_months:
                    notice_period_days = month_to_days.get(job.notice_period_number_of_months, 0)
                if job.employee_probation_of_months:
                    probation_period_days = month_to_days.get(job.employee_probation_of_months, 0)

            # notice_period_days = notice_mapping.get(notice_period_months, 90)  # Default 90 if not set
            print("notice_period_days ", notice_period_days)
            if resignation_date and date_from:
                ninety_days_after_resign = resignation_date + timedelta(days=notice_period_days)
                if resignation_date <= date_from <= ninety_days_after_resign:
                    employee.stage = 'probation'
                    payslip.Employee_Status = 'notice'
            # If not in notice period, check contract hiring date
            else:
                # ✅ If probation end date is set and payslip is for month after it → regular
                if probation_end and date_from:
                    # Compare with the first day of the month following probation end date
                    next_month = probation_end.replace(day=1) + timedelta(days=32)
                    next_month_start = next_month.replace(day=1)
                    if date_from >= next_month_start:
                        print("prvation_test")
                        employee.stage = 'regular'
                        payslip.Employee_Status = 'regular'
                        continue  # ⛔ Skip rest of logic

                if contract_history and contract_history.date_hired and date_from:
                    joining_date = contract_history.date_hired
                    if (joining_date.month == date_from.month and
                            joining_date.year == date_from.year and
                            joining_date.day > 17):
                        employee.stage = 'hold'
                        payslip.Employee_Status = 'hold'
                        continue  # Skip further checks
                if contract_history:
                    hired_date = contract_history.date_hired
                    print('----hired_date', hired_date)

                    if hired_date:
                        probation_cutoff = hired_date + timedelta(days=probation_period_days)  # 4 months
                        if date_from < probation_cutoff:
                            employee.stage = 'probation'
                            payslip.Employee_Status = 'probation'
                        else:
                            employee.stage = 'regular'
                            payslip.Employee_Status = 'regular'