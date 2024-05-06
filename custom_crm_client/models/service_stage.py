import re

from odoo import models, fields, api

class ServiceStage(models.Model):
    _name = 'crm.service.stage'
    _description = "CRM Services Stages"
    stage_seq = fields.Integer(string='stage sequence')
    stage_name = fields.Char(string='Stage Name', required=True, translate=True)

    services_stage_ID = fields.Char(string='Stage ID', index=True, readonly=True, copy=False)
    # services_id = fields.One2many('crm.services', 'services_stage_ID', string='Stages')



    @api.model
    def create(self, vals):
        record = super(ServiceStage, self).create(vals)
        record.services_stage_ID = str(record.id)
        return record
