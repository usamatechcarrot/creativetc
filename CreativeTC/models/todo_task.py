from odoo import models, fields

class TodoTask(models.Model):
    _inherit = "todo.task"  # inherit the existing Todo model

    # Existing field
    x_studio_assigned_date = fields.Date(string="Date Assigned")

    # New UI fields
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string="Priority", default='medium')

    notes = fields.Text(string="Notes")
