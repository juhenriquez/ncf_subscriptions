# -*- coding: utf-8 -*-

{
    'name': "NCF Manager Support for Sale Subscriptions",
    'version': '1.0',
    'category': 'Subscription',
 
    'author': 'Marcus Almeida, Grupo Consultoria Henca',
    'license': 'AGPL-3',
    "depends" : [
        'sale_subscription',
        'ncf_manager',
    ],
    'data': ["views.xml"],
    "active": False,
    "installable": True
}