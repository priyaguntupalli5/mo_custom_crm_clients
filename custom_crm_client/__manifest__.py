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
        'views/client_views.xml',
        'views/family_views.xml',
        'views/services.xml',
        'views/menu.xml',
        'views/service_tag_views.xml',
        'views/service_stage_views.xml',
        'views/service_type_views.xml',
        'views/family_details_tags_views.xml',

    ],
    'demo': [
        'demo/demo.xml',
    ],
}
