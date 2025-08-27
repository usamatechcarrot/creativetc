
from datetime import date
from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    test_field = fields.Char(string="This is a test field")

 # You can type the employee's joining date here
    joining_date = fields.Date(string="Joining Date")

      # Auto-computed in years from joining_date to today
    experience_years = fields.Integer(
        string="Experience (Years)",
        compute="_compute_experience_years",
        store=True  # set to False if you want it to always compute on the fly
    )

    @api.depends('joining_date')
    def _compute_experience_years(self):
        for rec in self:
            if rec.joining_date:
                rec.experience_years = (date.today() - rec.joining_date).days // 365
            else:
                rec.experience_years = 0
