from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    # The computed field to fetch attendance records
    attendance_count = fields.Integer(string='Attendance Records', compute='_compute_attendance_count')
    attendance_history_ids = fields.Many2many('hr.attendance', string='Attendance History', compute='_compute_attendance_history')

    def _compute_attendance_count(self):
        # Count attendance records for each employee
        for employee in self:
            employee.attendance_count = self.env['hr.attendance'].search_count([('employee_id', '=', employee.id)])

    def _compute_attendance_history(self):
        # Fetch the actual attendance records
        for employee in self:
            employee.attendance_history_ids = self.env['hr.attendance'].search([('employee_id', '=', employee.id)])