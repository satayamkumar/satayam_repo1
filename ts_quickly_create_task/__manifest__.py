{
    "name": "Quickly Create Tasks",
    "author": "Technians",
    'website': 'https://technians.com/odoo',
    "support": "support@technians.com",
    "version": "17.0",
    "category": "Project",
    "summary": """ Create the task quickly with the help of create task wizard """,
    "description": """ Create the task quickly with the help of create task wizard """,
    "depends": ['project', 'base', 'web'],
    "data": [
        'security/ir.model.access.csv',
        'views/create_quickly_project_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ts_quickly_create_task/static/src/js/create_task.js',
            'ts_quickly_create_task/static/src/xml/create_task.xml',
            'ts_quickly_create_task/static/src/scss/create_task.scss',
        ],
    },
    'images': [
        'static/description/banner.png'
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "license": "OPL-1",
    "price": 9,
    "currency": "USD",
}
