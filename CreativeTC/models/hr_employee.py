from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    # Test fields
    test_field = fields.Char(string="This is a test field")
    joining_date = fields.Date(string="Joining Date")
    experience_text = fields.Char(string="Experience", compute="_compute_experience_text", store=True)

    # Region (set by buttons)
    region = fields.Selection([
        ('india', 'India'),
        ('uae', 'UAE'),
    ], string="Region")

    # Client dropdown (options will change based on region)
    client_choice = fields.Selection(selection=[], string="Client", help="Select city here")

    # Control visibility of client dropdown
    client_visible = fields.Boolean(default=False)

    @api.depends('joining_date')
    def _compute_experience_text(self):
        for rec in self:
            if rec.joining_date:
                diff = relativedelta(date.today(), rec.joining_date)
                rec.experience_text = f"{diff.years} Years, {diff.months} Months, {diff.days} Days with us !!!"
            else:
                rec.experience_text = "Select joining date"

    client_choice = fields.Selection([
        ('noida', 'Noida'),
        ('chennai', 'Chennai'),
        ('hyderabad', 'Hyderabad'),
        ('dubai', 'Dubai'),
        ('abu_dhabi', 'Abu Dhabi'),
        ('sharjah', 'Sharjah'),
    ], string="Client")

    client_visible = fields.Boolean(default=False)

    def action_india(self):
        self.write({'client_visible': True})
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'hr.employee',
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_uae(self):
        self.write({'client_visible': True})
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'hr.employee',
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'current',
        }

    # # India button
    # def action_india(self):
    #     for rec in self:
    #         rec.region = 'india'
    #         rec.client_visible = True
    #         # assign options dynamically
    #         rec._fields['client_choice'].selection = [
    #             ('noida', 'Noida'),
    #             ('chennai', 'Chennai'),
    #             ('hyderabad', 'Hyderabad'),
    #         ]
    #     return {
    #         'type': 'ir.actions.client',
    #         'tag': 'display_notification',
    #         'params': {
    #             'title': "Region Selected",
    #             'message': "India selected! Choose your client below.",
    #             'sticky': False,
    #         }
    #     }

    # # UAE button
    # def action_uae(self):
    #     for rec in self:
    #         rec.region = 'uae'
    #         rec.client_visible = True
    #         rec._fields['client_choice'].selection = [
    #             ('dubai_dha', 'Dubai-DHA'),
    #             ('dubai_afg', 'Dubai-AFG'),
    #             ('abudhabi', 'Abu Dhabi'),
    #         ]
    #     return {
    #         'type': 'ir.actions.client',
    #         'tag': 'display_notification',
    #         'params': {
    #             'title': "Region Selected",
    #             'message': "UAE selected! Choose your client below.",
    #             'sticky': False,
    #         }
    #     }
