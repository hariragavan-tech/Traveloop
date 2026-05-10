from odoo import models, fields, api

class TravelTrip(models.Model):
    _name = 'travel.trip'
    _description = 'Travel Trip'

    name = fields.Char(string="Trip Name", required=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    
    # Relationship: One Trip has many Stops
    stop_ids = fields.One2many('travel.stop', 'trip_id', string="Stops")
    
    # The "Winning" Feature: Automatic Budgeting
    total_budget = fields.Float(string="Total Budget", compute="_compute_total_budget", store=True)

    @api.depends('stop_ids.stop_cost')
    def _compute_total_budget(self):
        for record in record:
            record.total_budget = sum(record.stop_ids.mapped('stop_cost'))