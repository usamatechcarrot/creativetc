from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    # Test fields
    test_field = fields.Char(string="This is a test field")
    joining_date = fields.Date(string="Joining Date")
    experience_text = fields.Char(string="Experience", compute="_compute_experience_text", store=True)

    # Region message field (hidden by default, shows on button click)
    region_message = fields.Char(string="Region Message")
    region_visible = fields.Boolean(default=False)

    # Radio Radio buttons (A/B)
    choice_visible = fields.Boolean(default=False)
    choice_option = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
    ], string="Choice")
    choice_visible = fields.Boolean(default=False)

    @api.depends('joining_date')
    def _compute_experience_text(self):
        for rec in self:
            if rec.joining_date:
                diff = relativedelta(date.today(), rec.joining_date)
                rec.experience_text = f"{diff.years} Years, {diff.months} Months, {diff.days} Days with us !!!"
            else:
                rec.experience_text = "Select joining date"

    def action_india(self):
        for rec in self:
            rec.region_message = "Hello India"
            rec.region_visible = True
            rec.choice_visible = True     # show the radio buttons
            rec.choice_option = False     # clear any old choice

    def action_uae(self):
        for rec in self:
            rec.region_message = "Hello UAE"
            rec.region_visible = False
        rec.region_message = False  # clear message
        rec.choice_option = False   # clear radio selection
        rec.choice_visible = False  # hide fields
