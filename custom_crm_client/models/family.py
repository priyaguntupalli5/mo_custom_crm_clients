import re

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Family(models.Model):
    _name = 'crm.family'
    _description = 'CRM Family'

    name = fields.Char('Family Name', required=True)
    family_id = fields.Char(string='Family ID', index=True, readonly=True, copy=False)
    client_ids = fields.One2many('crm.client', 'family_id', string='Clients')
    family_phone = fields.Char('Phone Number', required=True)
    family_email = fields.Char('Email', required=True)

    @api.model
    def create(self, vals):
        record = super(Family, self).create(vals)
        record.family_id = str(record.id)
        return record

    @api.constrains('family_phone')
    def _check_family_phone(self):
        for record in self:
            if record.family_phone and not re.match(r"^\d{10}$", record.family_phone):
                raise ValidationError(
                    "Phone number must be exactly 10 digits.")

    @api.constrains('family_email')
    def _check_family_email(self):
        for record in self:
            if record.family_email and not re.match(r"[^@]+@[^@]+\.[^@]+", record.family_email):
                raise ValidationError("Please provide a valid email address.")
