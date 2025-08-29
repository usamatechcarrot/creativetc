from odoo import models, fields

class DailyHabit(models.Model):
    _name = 'creative.daily_habit'
    _description = 'Daily Habit Tracker'

    name = fields.Char(string="Habit", required=True)
    date = fields.Date(string="Date", default=fields.Date.today)
    completed = fields.Boolean(string="Completed")
    notes = fields.Text(string="Notes")

