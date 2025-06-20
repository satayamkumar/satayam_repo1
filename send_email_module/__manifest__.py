{
    'name': 'send email module',
    'version': '1.0',
    'summary': 'Manage student information',
    'category': 'Education',
    'author': 'Your Name',
    'depends': ['base','contacts','hr', 'mail',],
    'data': [
        'data\mail_template.xml',
        'data\scheduled_action.xml',
    ],
    'installable': True,
    'application': True,
}


