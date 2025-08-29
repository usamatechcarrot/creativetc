from odoo import models, fields

class HelloWorld(models.Model):
    _name = 'creative.hello_world'
    _description = 'Hello World Model'

    name = fields.Char(string="Name", default="Hello World")
