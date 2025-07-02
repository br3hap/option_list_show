# -*- coding: utf-8 -*-
{
    'name': 'Option_list_show',
    'version': '1.0',
    'summary': """ Modulo que extiende la funcionalidad de ocultar a usuarios el boton botón que aparece al final de la cabecera en las vistas tipo lista - odoo 18  """,
    'author': 'Breithner Aquituari',
    'website': '',
    'category': '',
    'depends': ['base', 'web'],
    "data": [
        "views/res_users_views.xml"
    ],

    'assets': {
        'web.assets_backend': [
            'option_list_show/static/src/components/list_renderer/**/*',
        ]
    },
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
