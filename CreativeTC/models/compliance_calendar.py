from odoo import models, fields

class ComplianceCalendar(models.Model):
    _name = "compliance.calendar"
    _description = "Compliance Calendar"

    name = fields.Char("Compliance Name", required=True)
    office_id = fields.Selection([
        ("techcarrot india pvt. ltd", "techcarrot india pvt. ltd"),
        ("techcarrot fz llc", "techcarrot fz llc"),
        ("techcarrot technologies fz llc", "techcarrot technologies fz llc")
    ], default="techcarrot india pvt. ltd")
   location_id = fields.Selection([
        ("Noida", "Noida"),
        ("Chennai", "Chennai"),
        ("Faridabad", "Faridabad")
        ("Hyderabad", "Hyderabad")
    ], default="Chennai")
    compliance_type_id = fields.Many2one("compliance.type", "Compliance Type")
    due_date = fields.Date("Due Date", required=True)
    submission_date = fields.Date("Submission Date")
    status = fields.Selection([
        ("pending", "Pending"),
        ("complied", "Complied"),
        ("delayed", "Delayed")
    ], default="pending")
    responsible_id = fields.Many2one("res.users", "Responsible")
    notes = fields.Text("Description")