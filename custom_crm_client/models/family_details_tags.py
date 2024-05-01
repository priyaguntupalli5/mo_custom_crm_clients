from odoo import models, fields


class FamilyDetailsTags(models.Model):
    _name = 'crm.family.details.tags'
    _description = "CRM Family Details Tags"
    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color", required=True)

