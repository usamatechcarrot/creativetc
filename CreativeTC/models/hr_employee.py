
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    test_field = fields.Char(string="This is a test field")

 # You can type the employee's joining date here
    joining_date = fields.Date(string="Joining Date")

    #   # Auto-computed in years from joining_date to today
    # experience_years = fields.Integer(
    #     string="Experience (Years)",
    #     compute="_compute_experience_years",
    #     store=True  # set to False if you want it to always compute on the fly
    # )

    experience_text = fields.Char(string="Experience",
        compute="_compute_experience_text",
        store=True
    )
    # @api.depends('joining_date')
    # def _compute_experience_years(self):
    #     for rec in self:
    #         if rec.joining_date:
    #             rec.experience_years = (date.today() - rec.joining_date).days // 365
    #         else:
    #             rec.experience_years = 0

    @api.depends('joining_date')
    def _compute_experience_text(self):
        for rec in self:
            if rec.joining_date:
                diff = relativedelta(date.today(), rec.joining_date)
                rec.experience_text = f"{diff.years} Years, {diff.months} Months, {diff.days} Days with us !!!"
            else:
                rec.experience_text = "Select joining date"

# Multiple choice / option for Location and Client...

    main_choice = fields.Selection([
        ('button1', 'Button 1'),
        ('button2', 'Button 2'),
    ], string="Location:")

    dependent_choice = fields.Selection([], string="Client: ")

    @api.onchange('main_choice')
    def _onchange_main_choice(self):
        if self.main_choice == 'button1':
            self.dependent_choice = False
            return {'domain': {'dependent_choice': [('value', 'in', ['Hydrabad', 'Chennai', 'Noida'])]}}
        
        elif self.main_choice == 'button2':
            self.dependent_choice = False
            return {'domain': {'dependent_choice': [('value', 'in', ['Dubai-AFG', 'Dubai-DHA', 'AbuDhabi-Etihad'])]}}
        else:
            self.dependent_choice = False
            return {'domain': {'dependent_choice': []}}
