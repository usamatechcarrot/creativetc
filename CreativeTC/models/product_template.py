from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    origin_country = fields.Selection([
        ('india', 'India'),
        ('uae', 'UAE'),
    ], string="Origin Country:")
