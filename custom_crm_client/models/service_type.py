from odoo import models, fields


class ServiceType(models.Model):
    _name = 'crm.service.type'
    _description = "CRM Services Types"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    sequence = fields.Integer(string='sequence')
    description = fields.Char(string='Description', required=True, translate=True)
    type = fields.Char(string='Type')
    dep_id = fields.Selection([
        ('ESL', 'ESL'),
        ('Employment', 'Employment'),
        ('Settlement', 'Settlement'),
        ('Children & Youth', 'Children & Youth'),
        ('IT Department', 'IT Department'),
    ],
        string='Department')
