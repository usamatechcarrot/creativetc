from odoo import models, fields

class TodoTask(models.Model):
    _inherit = "todo.task"  # inherit the existing Todo model

    x_studio_assigned_date = fields.Date(string="Date Assigned")
