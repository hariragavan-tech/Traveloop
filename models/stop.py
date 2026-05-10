from odoo import models, fields

class TravelStop(models.Model):
    _name = 'travel.stop'
    _description = 'Travel Stop'

    trip_id = fields.Many2one('travel.trip', string="Trip", ondelete='cascade')
    city_name = fields.Char(string="City Name", required=True)
    stop_cost = fields.Float(string="Estimated Cost")