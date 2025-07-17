{
    'name': 'password manager app',
    'version': '1.0',
    'summary': 'password manager app information',
    'category': 'password manager app',
    'author': 'password manager app',
    'depends': ['base', 'contacts', 'mail'],
    'data': [
        'security/password_manager_security.xml',
        'security/ir.model.access.csv',
        'views/ts_secret.xml',
        'views/ts_secret_line.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'password_manager_app/static/src/css/char_toggle_widget.css',
            'password_manager_app/static/src/js/char_toggle_widget.js',
            'password_manager_app/static/src/xml/char_toggle_widget.xml',
        ],
    },
    'installable': True,
    'application': True,
    'images': ['static/description/icon.png'],

}


# id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
# password_manager_app.access_ts_secret,access_ts_secret,password_manager_app.model_ts_secret,base.group_user,1,1,1,1
# password_manager_app.access_ts_secret_line,access_ts_secret_line,password_manager_app.model_ts_secret_line,base.group_user,1,1,1,1







# id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
# access_ts_secret_line_user,access_ts_secret_line_user,password_manager_app.model_ts_secret_line,password_manager_app.group_password_user,1,0,0,0
# access_ts_secret_line_manager,access_ts_secret_line_manager,password_manager_app.model_ts_secret_line,password_manager_app.group_password_manager_user,1,1,1,1
# access_ts_secret_user,access_ts_secret_user,password_manager_app.model_ts_secret,password_manager_app.group_password_user,1,0,0,0
# access_ts_secret_manager,access_ts_secret_manager,password_manager_app.model_ts_secret,password_manager_app.group_password_manager_user,1,1,1,1

