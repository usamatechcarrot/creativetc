from odoo import models, fields, api
from datetime import datetime, timedelta, time


class EmployeeAttendanceLine(models.Model):
    _name = "employee.attendance.line"
    _description = "Daily Attendance Line"
    _order = "date desc"

    employee_id = fields.Many2one(
        "hr.employee", string="Employee", required=True, ondelete="cascade"
    )
    date = fields.Date("Date", required=True)
    check_in = fields.Datetime("Check In")
    check_out = fields.Datetime("Check Out")
    status = fields.Selection(
        [
            ("present", "Present"),
            ("absent", "Absent"),
        ],
        string="Status",
        default="absent",
    )


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    attendance_line_ids = fields.One2many(
        "employee.attendance.line",
        "employee_id",
        string="Daily Attendance",
        compute="_compute_attendance_lines",
        store=False,
    )

    def _compute_attendance_lines(self):
        """Compute last 7 days of attendance (present/absent)."""
        Attendance = self.env["hr.attendance"]
        for emp in self:
            lines = []
            today = fields.Date.today()
            for i in range(7):  # last 7 days
                day = today - timedelta(days=i)
                att = Attendance.search([
                    ("employee_id", "=", emp.id),
                    ("check_in", ">=", datetime.combine(day, time.min)),
                    ("check_in", "<=", datetime.combine(day, time.max)),
                ], limit=1)
                if att:
                    lines.append((0, 0, {
                        "date": day,
                        "check_in": att.check_in,
                        "check_out": att.check_out,
                        "status": "present",
                    }))
                else:
                    lines.append((0, 0, {
                        "date": day,
                        "status": "absent",
                    }))
            emp.attendance_line_ids = lines
