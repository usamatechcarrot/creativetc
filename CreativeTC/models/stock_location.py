from odoo import models, fields, api

class StockLocation(models.Model):
    _inherit = 'stock.location'

    stock_capacity = fields.Float(
        string="Max Capacity by Usama",
        default=6500,
        help="Maximum stock capacity for this location. Set by Usama"
    )

    stock_used = fields.Float(
        string="Current Stock",
        compute="_compute_stock_used",
        store=False
    )

    stock_usage_percent = fields.Float(
        string="Usage (%)",
        compute="_compute_stock_used",
        store=False
    )

    @api.depends('quant_ids', 'quant_ids.quantity')
    def _compute_stock_used(self):
        """Compute how much stock is stored in this location"""
        for location in self:
            qty = sum(location.quant_ids.mapped('quantity'))
            location.stock_used = qty
            if location.stock_capacity > 0:
                location.stock_usage_percent = min(100, (qty / location.stock_capacity) * 100)
            else:
                location.stock_usage_percent = 0.0
