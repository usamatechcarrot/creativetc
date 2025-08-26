from odoo import fields, models
 
class Employee(models.Model):
    _inherit = "hr.employee"
 
    attendance_ids = fields.One2many(
        "hr.attendance",  # foreign model
        "employee_id",    # inverse field
        string="Attendances"
    )
 