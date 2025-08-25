from odoo import models, fields

class TodoTask(models.Model):
    _name = "todo.task"
    _description = "Todo Task"

    name = fields.Char("Title", required=True)
    description = fields.Text("Description")

    # 👉 New text field
    notes = fields.Text(string="Notes")  
