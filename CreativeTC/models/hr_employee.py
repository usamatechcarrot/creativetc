from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'hr.employee'

    # Custom Fields
    test_field = fields.Char(string="This is a test field")
    joining_date = fields.Date(string="Joining Date")
    experience_text = fields.Char(string="Experience", compute="_compute_experience_text", store=True)

    region = fields.Selection([
        ('india', 'India'),
        ('uae', 'UAE'),
        ('hello', 'USA'),
    ], string="Region")

    client_choice = fields.Selection(
        selection=[],
        string="Client",
    )

    client_visible = fields.Boolean(default=False)

    # --- Compute Methods ---
    @api.depends('joining_date')
    def _compute_experience_text(self):
        """Compute difference between today and joining_date."""
        for rec in self:
            if rec.joining_date:
                diff = relativedelta(date.today(), rec.joining_date)
                rec.experience_text = f"{diff.years} Years, {diff.months} Months, {diff.days} Days with us !!!"
            else:
                rec.experience_text = "Select joining date"

    # --- Button Actions ---
    def action_india(self):
        """Triggered when India button clicked."""
        self.write({
            'region': 'india',
            'client_visible': True,
        })
        self._set_client_options([
            ('noida', 'Noida'),
            ('chennai', 'Chennai'),
            ('hyderabad', 'Hyderabad'),
        ])
        return self._notify("You clicked India button!")

    def action_uae(self):
        """Triggered when UAE button clicked."""
        self.write({
            'region': 'uae',
            'client_visible': False,
        })
        self._set_client_options([
            ('dubai_dha', 'Dubai-DHA'),
            ('dubai_afg', 'Dubai-AFG'),
            ('abudhabi', 'Abu Dhabi'),
        ])
        return self._notify("You clicked UAE button!")

    # --- Helpers ---
    def _set_client_options(self, options):
        """Update client_choice selection dynamically."""
        self._fields['client_choice'].selection = options

    def _notify(self, message):
        """Return frontend notification."""
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': "Button Clicked",
                'message': message,
                'sticky': False,
            }
        }
