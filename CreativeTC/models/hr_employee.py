from odoo import models, fields

class HREmployee(models.Model):
    _inherit = 'hr.employee'
  

    attendance_ids = fields.One2many(
        'hr.attendance',
        'employee_id',
        string="Attendance Records"
    )

class HRAttendance(models.Model):
    _name = 'hr.attendance'

    name = fields.Char(string='Name')
    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee'
    )
