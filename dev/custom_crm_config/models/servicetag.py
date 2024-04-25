from odoo import models, fields, api, _


class ServiceTag(models.Model):
    _name = 'crm.servicetag'
    _description = "CRM Services Tags"

    tag = fields.Char(string='tag', required = True)
