{
    'name': 'Traveloop - Intelligent Travel Planner',
    'version': '1.0',
    'category': 'Services/Travel',
    'summary': 'Collaborative multi-city travel planning and automated budgeting.',
    'description': """
Traveloop Hackathon Project:
- Dynamic budget estimation based on activities.
- Robust date validation for travel stops.
- Collaborative trip planning using Odoo Chatter.
- Visual Kanban and Timeline views for itineraries.
    """,
    'author': 'Your Team Name',
    'depends': [
        'base', 
        'mail', # Required for the "Collaborative" chatter/notes feature
    ],
    'data': [
        'security/ir.model.access.csv',  # Your security file
        'views/trip_views.xml',         # The file your teammate is working on
        'views/menus.xml',              # The file your teammate is working on
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}