# -*- coding: utf-8 -*-
{
    'name': "Payment Voucher Printout",

    'summary': """
    """,

    'description': """

    """,

    'author': "Hery",
    'website': "https://h3ry.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/payment_voucher_templates.xml',
        'views/account_payment_print.xml',
        
    ]
}
