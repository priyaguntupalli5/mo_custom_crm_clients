{
    'name': "CRM client",
    'summary': "Service for handling client and household management",
    'author': "MCAF",
    'website': "https://mcaf.nb.ca/en/",
    'author': "MCAF",
    'category': "CRM Internal",
    'license': 'OPL-1',
    "application": True,
    "installable": True,
    'version': '16.0.1.0.0',
    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
