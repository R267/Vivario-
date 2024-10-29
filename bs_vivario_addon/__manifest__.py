{
    'name': 'BS Vivario Addon',
    'version': '1.1',
    'category': 'Inventory',
    'summary': 'Adds "Закрито документами" status to delivery orders',
    'description': 'This module adds a final status "Закрито документами" and a flag to Delivery Orders in Odoo.',
    'website': 'https://www.odoo.com/app/inventory',
    'depends': ['stock'],
    'data': [
         'views/delivery_order_view.xml',
         'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'auto_install': True,
}