{
    'name': 'BonSens Vivario add-on',
    'summary': """
        BonSens add-on for Inventory""",
    'description': """
        BonSens add-on for Inventory""",
    'author': "BonSens",
    'website': "https://www.bonsens.com.ua",
    'category': 'Inventory',
    'version': '17.0.1.0.1',
    'depends': ['stock'],
    'data': [
         'views/delivery_order_view.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'stock/static/src/scss/report_stock_reception.scss',
            'stock/static/src/scss/report_stock_rule.scss',
        ],
        'web.assets_backend': [
            'stock/static/src/**/*.js',
            'stock/static/src/**/*.xml',
            'stock/static/src/scss/*.scss',
            'stock/static/src/views/**/*',
        ],
        'web.assets_frontend': [
            'stock/static/src/scss/stock_traceability_report.scss',
        ],
        'web.assets_tests': [
            'stock/static/tests/tours/*.js',
        ],
        'web.qunit_suite_tests': [
            'stock/static/tests/counted_quantity_widget_tests.js',
            'stock/static/tests/inventory_report_list_tests.js',
            'stock/static/tests/popover_widget_tests.js',
            'stock/static/tests/stock_traceability_report_backend_tests.js',
            'stock/static/tests/stock_move_one2many_tests.js',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': True,
}