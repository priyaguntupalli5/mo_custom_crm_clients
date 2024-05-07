from odoo import models, fields, api


class ServiceStage(models.Model):
    _name = 'crm.service.stage'
    _description = "CRM Services Stages"
    stage_seq = fields.Integer(string='stage sequence')
    stage_name = fields.Char(string='Stage Name', required=True, translate=True)
    stage_id = fields.Char(string='Stage ID', index=True, readonly=True, copy=False)


    @api.model
    def create(self, vals):
        record = super(ServiceStage, self).create(vals)
        record.stage_id = str(record.id)
        return record
