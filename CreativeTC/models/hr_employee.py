from odoo import models, fields, api
from datetime import date, timedelta

class EmployeeAttendanceLine(models.Model):
    _name = 'employee.attendance.line'
    _description = 'Daily Attendance Line'
    _order = 'date desc'

    employee_id = fields.Many2one('hr.employee', string="Employee", ondelete="cascade")
    date = fields.Date(string="Date")
    check_in = fields.Datetime(string="Check In")
    check_out = fields.Datetime(string="Check Out")
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
    ], string="Status", default="absent")

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    attendance_line_ids = fields.One2many(
        'employee.attendance.line',
        'employee_id',
        string="Attendance Lines"
    )

    @api.model
    def generate_attendance_lines(self):
        """Sync attendance data into our custom model."""
        employees = self.search([])
        today = date.today()

        for emp in employees:
            # Avoid duplicates
            if not self.env['employee.attendance.line'].search([
                ('employee_id', '=', emp.id),
                ('date', '=', today)
            ]):
                # Find attendance in hr.attendance
                att = self.env['hr.attendance'].search([
                    ('employee_id', '=', emp.id),
                    ('check_in', '>=', today),
                    ('check_in', '<', today + timedelta(days=1))
                ], limit=1)

                vals = {
                    'employee_id': emp.id,
                    'date': today,
                    'status': 'present' if att else 'absent',
                    'check_in': att.check_in if att else False,
                    'check_out': att.check_out if att else False,
                }
                self.env['employee.attendance.line'].create(vals)
