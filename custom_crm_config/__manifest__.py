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
        'views/menu.xml',
        'views/service_tag_views.xml',
        'views/service_stage_views.xml',
        'views/service_type_views.xml'
    ],
}
