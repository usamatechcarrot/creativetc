from odoo import models, fields, api
from datetime import datetime, timedelta

class EmployeeAttendanceLine(models.Model):
    _name = "employee.attendance.line"
    _description = "Daily Attendance Line"

    employee_id = fields.Many2one("hr.employee", string="Employee", ondelete="cascade")
    date = fields.Date("Date")
    check_in = fields.Datetime("Check In")
    check_out = fields.Datetime("Check Out")
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
    ], string="Status", default="absent")


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    attendance_line_ids = fields.One2many(
        "employee.attendance.line",
        "employee_id",
        string="Daily Attendance",
        compute="_compute_attendance_lines",
        store=False  # dynamic, not stored in DB
    )

    def _compute_attendance_lines(self):
        for emp in self:
            lines = []
            # Example: last 7 days
            today = fields.Date.today()
            for i in range(7):
                day = today - timedelta(days=i)
                att = self.env['hr.attendance'].search([
                    ('employee_id', '=', emp.id),
                    ('check_in', '>=', day),
                    ('check_in', '<', day + timedelta(days=1)),
                ], limit=1)

                if att:
                    lines.append((0, 0, {
                        'date': day,
                        'check_in': att.check_in,
                        'check_out': att.check_out,
                        'status': 'present'
                    }))
                else:
                    lines.append((0, 0, {
                        'date': day,
                        'status': 'absent'
                    }))
            emp.attendance_line_ids = lines
