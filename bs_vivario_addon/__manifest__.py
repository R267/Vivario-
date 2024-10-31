# -*- coding: utf-8 -*-
{
    'name': "BonSens Vivario add-on",

    'summary': """
        BonSens add-on for Vivario""",

    'description': """
        BonSens add-on for Vivario
    """,

    'author': "BonSens",
    'website': "https://www.bonsens.com.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '17.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'views/delivery_order_view.xml', 
    ],
}
