from odoo import models, fields


class ServiceTag(models.Model):
    _name = 'crm.service.tag'
    _description = "CRM Services Tags"
    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color", required=True)

