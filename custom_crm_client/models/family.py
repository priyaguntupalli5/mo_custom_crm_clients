from odoo import models, fields, api


class Family(models.Model):
    _name = 'crm.family'
    _description = 'CRM Family'

    name = fields.Char('Family Name', required=True)
    family_id = fields.Char(string='Family ID', index=True, readonly=True, copy=False)
    client_ids = fields.One2many('crm.client', 'family_id', string='Clients')

    @api.model
    def create(self, vals):
        record = super(Family, self).create(vals)
        record.family_id = str(record.id)
        return record

