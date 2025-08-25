from odoo import models, fields

class TodoTask(models.Model):
    # 👉 New text field
    notes = fields.Text(string="Notes")  
