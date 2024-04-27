from odoo import models, fields, api, _


class ServiceType(models.Model):
    _name = 'crm.service.type'
    _description = "CRM Services Types"

    resume = fields.Char(string='Resume', required = True)
    settlement_plan = fields.Char(string='Settlement Plan', required = True)
    info_session = fields.Char(string='Information session', required = True)

