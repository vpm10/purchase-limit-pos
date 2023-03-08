{
    'name': 'Purchase Limit In POS',
    'version': '16.0.1.0.0',
    'sequence': '-9',
    'category': 'pos',
    'summary': 'Set Purchase Limit In POS',
    'description': 'Set Purchase Limit In POS',

    'installation': True,
    'application': True,

    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/res_partner.xml',
    ],
    'assets': {
       'point_of_sale.assets': [
           'pos_purchase_limit/static/src/xml/partner_list_screen.xml',
           'pos_purchase_limit/static/src/js/payment_screen.js',
       ],
}
}