from odoo import models, fields, api
from datetime import date

class DailyHabit(models.Model):
    _name = 'daily.habit'
    _description = 'Daily Habit Tracker'

    name = fields.Char(string="Habit Name", required=True)
    user_id = fields.Many2one('res.users', string="User", default=lambda self: self.env.user)
    frequency = fields.Selection([
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ], string="Frequency", default='daily')
    target_count = fields.Integer(string="Target", default=1)
    date = fields.Date(string="Date", default=date.today)
    completed_count = fields.Integer(string="Completed Count", default=0)
    status = fields.Selection([
        ('not_done', 'Not Done'),
        ('done', 'Done')
    ], string="Status", compute='_compute_status', store=True)

    @api.depends('completed_count', 'target_count')
    def _compute_status(self):
        for rec in self:
            if rec.completed_count >= rec.target_count:
                rec.status = 'done'
            else:
                rec.status = 'not_done'
