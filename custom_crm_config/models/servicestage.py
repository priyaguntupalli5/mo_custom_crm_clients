from odoo import models, fields, api, _


class ServiceStage(models.Model):
    _name = 'crm.servicestage'
    _description = "CRM Services Stages"

    New = fields.Char(string='New', required = True)
    in_progress = fields.Char(string='In Progress', required = True)
    delayed = fields.Char(string='Delayed', required = True)
    done = fields.Char(string='Done', required = True)


