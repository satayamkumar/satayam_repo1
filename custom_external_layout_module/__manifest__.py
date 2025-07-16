# -*- coding: utf-8 -*-
{
    'name': "custom external layout module",
    'summary': """
        change defult font to nice arabic font""",
    'description': """
        Change the external layout of the all interfaces with 
        a beautiful one preferred by the Arabic user """,
    'author': "Mali, MuhlhelITS",
    'website': "http://muhlhel.com",
    'category': 'Localization',
    'version': '16.0',
    'depends': ['base','web'],

    'data': [
        'views/report_template.xml'
    ],

    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'auto_install': True,
    'installable': True,
    'live_test_url': 'https://youtu.be/aR3ZmDu8OjI',
}
