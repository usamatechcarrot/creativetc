from odoo import models, fields
from datetime import datetime, date, timedelta, time

class EmployeeAttendanceLine(models.Model):
    _name = "employee.attendance.line"
    _description = "Daily Attendance Line"
    _order = "date desc"

    employee_id = fields.Many2one('hr.employee', string="Employee", ondelete="cascade")
    date = fields.Date(string="Date")
    check_in = fields.Datetime(string="Check In")
    check_out = fields.Datetime(string="Check Out")
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent')
    ], string="Status", default='absent')


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    attendance_line_ids = fields.One2many(
        'employee.attendance.line',
        'employee_id',
        string='Daily Attendance'
    )

    def generate_attendance_lines(self, days=7):
        """Fill last X days of attendance for this employee."""
        Attendance = self.env['hr.attendance']
        today = date.today()

        for emp in self:
            for i in range(days):
                day = today - timedelta(days=i)
                # Skip if line already exists
                if self.env['employee.attendance.line'].search([
                    ('employee_id', '=', emp.id),
                    ('date', '=', day)
                ]):
                    continue

                att = Attendance.search([
                    ('employee_id', '=', emp.id),
                    ('check_in', '>=', datetime.combine(day, time.min)),
                    ('check_in', '<=', datetime.combine(day, time.max))
                ], limit=1)

                vals = {
                    'employee_id': emp.id,
                    'date': day,
                    'check_in': att.check_in if att else False,
                    'check_out': att.check_out if att else False,
                    'status': 'present' if att else 'absent',
                }
                self.env['employee.attendance.line'].create(vals)
