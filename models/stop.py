class TravelStop(models.Model):
    _name = 'travel.stop'
    
    trip_id = fields.Many2one('travel.trip', string="Trip", ondelete='cascade')
    city_name = fields.Char(string="City", required=True)
    arrival_date = fields.Date(string="Arrival")
    departure_date = fields.Date(string="Departure")
    
    # Relationship: One Stop has many Activities
    activity_ids = fields.One2many('travel.activity', 'stop_id', string="Activities")
    stop_cost = fields.Float(string="Stop Cost", compute="_compute_stop_cost", store=True)

    @api.depends('activity_ids.cost')
    def _compute_stop_cost(self):
        for record in record:
            record.stop_cost = sum(record.activity_ids.mapped('cost'))