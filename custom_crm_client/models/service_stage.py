from odoo import models, fields

class ServiceStage(models.Model):
    _name = 'crm.service.stage'
    _description = "CRM Services Stages"
    _rec_name ='stage_name'

    stage_seq = fields.Integer(string='stage sequence')
    stage_name = fields.Char(string='Stage Name', required=True, translate=True)


