{
    'name': 'Stock Location Progress Bar',
    'version': '18.0',
    'category': 'Inventory',
    'summary': 'Show progress bar of stock usage in each location',
    'depends': ['stock', 'base', 'project', 'project_todo', 'product', 'hr'],

    'data': [
        'views/stock_location_views.xml',
        'views/product_views.xml',
        'views/todo_task_views.xml',
        'views/product_template_view.xml',
        'views/hr_employee_view.xml',
    ],
    'installable': True,
    'application': False,
}

{
    "name": "Daily Habit Tracker",
    "version": "1.0",
    "summary": "Track daily habits and progress",
    "author": "Your Name",
    "category": "Productivity",
    "depends": ["base"],
    "data": [
        "views/habit_views.xml",
    ],
    "installable": True,
    "application": True,
}
