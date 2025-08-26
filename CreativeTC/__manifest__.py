{
    'name': 'Stock Location Progress Bar',
    'version': '18.0',
    'category': 'Inventory',
    'summary': 'Show progress bar of stock usage in each location',
    'depends': ['stock', 'project', 'project_todo','hr','hr_attendance'],
    
    'data': [
        'views/stock_location_views.xml',
        'views/product_views.xml',
        'views/todo_task_views.xml',
        'views/hr_employee_views.xml'
     ],
    'installable': True,
    'application': False,
}
