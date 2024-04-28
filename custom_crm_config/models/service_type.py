from odoo import models, fields

class ServiceType(models.Model):
    _name = 'crm.service.type'
    _description = "CRM Services Types"
    desc_seq = fields.Integer(string='desc sequence')
    description = fields.Char(string='Description', required=True)

