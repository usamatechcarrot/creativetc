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
        comodel_name="employee.attendance.line",
        inverse_name="employee_id",
        string="Daily Attendance",
    )
