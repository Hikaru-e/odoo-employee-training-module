{
    'name': 'Employee Training Management',
    'version': '1.0',
    'author': 'My Company',
    'license': 'LGPL-3',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'security/employee_training_security.xml',
        'security/models.xml',
        'security/ir.model.access.csv',
        'reports/training_session_report.xml',  # Add this line
        'views/training_topic_view.xml',
        'views/training_session_view.xml',
        'views/menus.xml',
        'views/session_enroll_wizard_view.xml',
    ],
    'installable': True,
    'application': True,
}