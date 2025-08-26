
from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    test_field = fields.Char(string="This is a test field")
