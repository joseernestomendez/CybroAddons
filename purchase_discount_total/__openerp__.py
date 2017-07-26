{
    'name': 'Purchase Discount on Total Amount',
    'version': '1.0',
    'category': 'Purchase Management',
    'summary': "Discount on total in Purchase and invoice with Discount limit and approval",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'http://www.cybrosys.com',

    'description': """

Sale Discount for Total Amount
=======================
Module to manage discount on total amount in Sale.
        as an specific amount or percentage
""",
    'depends': ['sale',
                'account'
                ],
    'data': [
        'views/purchase_view.xml',
        'views/account_invoice_view.xml',
        'views/invoice_report.xml',
        'views/purchase_order_report.xml',
        'views/res_config_view.xml',

    ],
    'demo': [
    ],
    'images': ['static/description/banner.jpg'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
