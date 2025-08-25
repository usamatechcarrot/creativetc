from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "project.task"

    date_assigned = fields.Date(
        string="Assigned Date",
        help="Date when the task was assigned. <Dinesh>"
    )
