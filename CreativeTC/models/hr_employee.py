from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    test_field = fields.Char(string="This is a test field")

    joining_date = fields.Date(string="Joining Date")

    experience_text = fields.Char(
        string="Experience",
        compute="_compute_experience_text",
        store=True
    )

    @api.depends('joining_date')
    def _compute_experience_text(self):
        for rec in self:
            if rec.joining_date:
                diff = relativedelta(date.today(), rec.joining_date)
                rec.experience_text = f"{diff.years} Years, {diff.months} Months, {diff.days} Days with us !!!"
            else:
                rec.experience_text = "Select joining date"

    main_choice = fields.Selection([
        ('button1', 'Button 1 - India'),
        ('button2', 'Button 2 - UAE'),
    ], string="Location:")

    dependent_client = fields.Selection([], string="Client:")

    # @api.onchange('main_choice')
    # def _onchange_main_choice(self):
    #     if self.main_choice == 'button1':
    #         return {
    #             'domain': {
    #                 'dependent_client': [
    #                     ('selection_key', 'in', ['hydrabad', 'chennai', 'noida'])
    #                 ]
    #             },
    #             'value': {'dependent_client': False}
    #         }
    #     elif self.main_choice == 'button2':
    #         return {
    #             'domain': {
    #                 'dependent_client': [
    #                     ('selection_key', 'in', ['dubai_afg', 'dubai_dha', 'abudhabi'])
    #                 ]
    #             },
    #             'value': {'dependent_client': False}
    #         }
    #     else:
    #         return {
    #             'domain': {'dependent_client': []},
    #             'value': {'dependent_client': False}
    #         }

    # @api.model
    def action_india(self, *args, **kwargs):
        for rec in self:
            return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': "Button Clicked",
                'message': f"{rec.name}: You clicked INDIA button 🚩",
                'sticky': False,
            }
        }

    # @api.model
    def action_uae(self, *args, **kwargs):
        for rec in self:
            return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': "Button Clicked",
                'message': f"{rec.name}: You clicked UAE button 🇦🇪",
                'sticky': False,
            }
        }

    # Will hold whether user clicked India or UAE
    region = fields.Selection([
        ('india', 'India'),
        ('uae', 'UAE'),
    ], string="Region")

    # Dropdown that will be shown only after clicking button
    client_choice = fields.Selection(
        selection=[],
        string="Client"
    )
    
    def action_india(self, *args, **kwargs):
        for rec in self:
            rec.region = 'india'
            rec._fields['client_choice'].selection = [
                ('noida', 'Noida'),
                ('chennai', 'Chennai'),
                ('hyderabad', 'Hyderabad'),
            ]
        return {}

    def action_uae(self, *args, **kwargs):
        for rec in self:
            rec.region = 'uae'
            rec._fields['client_choice'].selection = [
                ('dubai_dha', 'Dubai-DHA'),
                ('dubai_afg', 'Dubai-AFG'),
                ('abudhabi', 'Abu Dhabi'),
            ]
        return {}