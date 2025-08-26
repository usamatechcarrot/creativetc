from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

#     partner_rating = fields.Selection([
#         ('1', '⭐'),
#         ('2', '⭐⭐'),
#         ('3', '⭐⭐⭐'),
#         ('4', '⭐⭐⭐⭐'),
#         ('5', '⭐⭐⭐⭐⭐'),
#     ], string="Ratingssss")
