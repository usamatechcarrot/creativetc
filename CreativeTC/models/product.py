from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    max_capacity = fields.Float(
        string="Maximum Capacity",
        help="Define the maximum storage capacity for this product. by usama"
    )

class ProductProduct(models.Model):
    _inherit = "product.product"

    max_capacity = fields.Float(
        related="product_tmpl_id.max_capacity",
        store=True,
        readonly=False
    )

    
