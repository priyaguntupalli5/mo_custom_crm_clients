from odoo import models, fields

class NaarsStage(models.Model):
    _name = 'crm.naars.stage'
    _description = "CRM NAARS Stages"
    naars_seq = fields.Integer(string='stage sequence')
    naars_name = fields.Char(string='Stage Name', required=True, translate=True)
