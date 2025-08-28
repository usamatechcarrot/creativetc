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

    # Dropdown that will be shown only after clicking button
    client_choice = fields.Selection(selection=[], string="Client")

    # India button
    def action_india(self):
        for rec in self:
            rec.region = 'india'
            rec._fields['client_choice'].selection = [
                ('noida', 'Noida'),
                ('chennai', 'Chennai'),
                ('hyderabad', 'Hyderabad'),
            ]
        return True

    # UAE button
    def action_uae(self):
        for rec in self:
            rec.region = 'uae'
            rec._fields['client_choice'].selection = [
                ('dubai_dha', 'Dubai-DHA'),
                ('dubai_afg', 'Dubai-AFG'),
                ('abudhabi', 'Abu Dhabi'),
            ]
        return True
