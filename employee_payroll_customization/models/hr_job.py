from odoo import api, fields, models, _
from dateutil.relativedelta import relativedelta
import calendar

class HrJobInherit(models.Model):
    _inherit = 'hr.job'

    notice_period_days = fields.Integer(string='Notice Period Days')

    notice_period_number_of_months = fields.Selection([
        ('one month', 'One Month'),
        ('two month', 'Two Month'),
        ('three month', 'Three Month'),
        ('four month', 'Four Month')],
        string='Notice Period'
    )

    employee_probation_of_months = fields.Selection(
        [('one_month', 'One Month'),
        ('two_month', 'Two Month'),
        ('three_month', 'Three Month'),
        ('four_month', 'Four Month')],
        string='Probation Period'
    )



    @api.onchange('job_id','job_id.employee_probation_of_months')
    def _onchange_set_probation_end_date(self):
        """
        Set probation_end_date to the *last day* of the month that ends
        the chosen probation period, counted from today.
        """
        MONTHS = {
            'one_month': 1,
            'two_month': 2,
            'three_month': 3,
            'four_month': 4,
        }

        for emp in self:
            emp.probation_end_date = False  # default / clear
            months_key = emp.job_id.employee_probation_of_months
            months_int = MONTHS.get(months_key, 0)  # 0 ⇒ nothing selected
            print("months_key ",months_key)
            print("months_int ",months_int)

            if not months_int:
                continue

            # Count forward the required number of months from today…
            target = fields.Date.today() + relativedelta(months=months_int)

            # …then jump to that month’s last day
            last_dom = calendar.monthrange(target.year, target.month)[1]
            emp.probation_end_date = target.replace(day=last_dom)