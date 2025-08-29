from odoo import models, fields

class DailyHabitTracker(models.Model):
    _name = 'creative.daily_habit_tracker'
    _description = 'Daily Habit Tracker'

    name = fields.Char(string="Habit", default="Hello Habit")
