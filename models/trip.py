from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TravelTrip(models.Model):
    _name = 'travel.trip'
    _description = 'Travel Itinerary'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Enables the "Chatter" for collaboration

    name = fields.Char(string="Trip Name", required=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    total_budget = fields.Float(string="Total Budget", compute="_compute_total_budget", store=True)

    stop_ids = fields.One2many('travel.stop', 'trip_id', string="Stops")

    @api.depends('stop_ids.stop_cost')
    def _compute_total_budget(self):
        for trip in self:
            # DYNAMIC DATA: Automatically sums stop costs
            trip.total_budget = sum(trip.stop_ids.mapped('stop_cost'))

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for trip in self:
            # ROBUST VALIDATION: Prevents logical errors in dates
            if trip.start_date and trip.end_date and trip.start_date > trip.end_date:
                raise ValidationError("The Departure Date cannot be before the Arrival Date!")