from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "project.task"

    date_assigned = fields.date(
        string="Date the task was assigned",
        help="Define the date on which the task was assigned. <Dinesh>"
    )
