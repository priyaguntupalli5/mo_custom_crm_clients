{
    'name': "CRM Configuration",
    'summary': "Service for handling configuration",
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
        'views/servicetag.xml',
        'views/servicestage.xml',
        'views/servicetype.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
