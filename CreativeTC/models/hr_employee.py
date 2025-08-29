from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    test_field = fields.Char(string="This is a test field")
    joining_date = fields.Date(string="Joining Date")
    experience_text = fields.Char(string="Experience", compute="_compute_experience_text", store=True)

    @api.depends('joining_date')
    def _compute_experience_text(self):
        for rec in self:
            if rec.joining_date:
                diff = relativedelta(date.today(), rec.joining_date)
                rec.experience_text = f"{diff.years} Years, {diff.months} Months, {diff.days} Days with us !!!"
            else:
                rec.experience_text = "Select joining date"

    # Will hold whether user clicked India or UAE
    region = fields.Selection([
        ('india', 'India'),
        ('uae', 'UAE'),
    ], string="Region")

    client_choice = fields.Selection([], string="Client", placeholder="Select city here...")

    @api.onchange('region')
    def _onchange_region(self):
        """Dynamically load clients based on region"""
        if self.region == 'india':
            self.client_choice = False
            self._fields['client_choice'].selection = [
                ('noida', 'Noida'),
                ('chennai', 'Chennai'),
                ('hyderabad', 'Hyderabad'),
            ]
        elif self.region == 'uae':
            self.client_choice = False
            self._fields['client_choice'].selection = [
                ('dubai_dha', 'Dubai-DHA'),
                ('dubai_afg', 'Dubai-AFG'),
                ('abudhabi', 'Abu Dhabi'),
            ]
