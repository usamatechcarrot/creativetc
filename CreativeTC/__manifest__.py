{
    'name': 'Stock Location Progress Bar',
    'version': '18.0',
    'category': 'Inventory',
    'summary': 'Show progress bar of stock usage in each location',
    'depends': ['stock'],
    'data': [
        'views/stock_location_views.xml',
        'views/product_views.xml',
        'views/project_task.xml',
    ],
    'installable': True,
    'application': False,
}
