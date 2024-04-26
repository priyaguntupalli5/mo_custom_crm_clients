from odoo import models, fields, api, _


class Client(models.Model):
    _name = 'crm.client'
    _description = 'CRM Client'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade', auto_join=True, index=True)
    client_id = fields.Char(string='Client ID', index=True, readonly=True, copy=False)

    household = fields.Selection([
        ('individual', 'Individual'),
        ('family', 'Family')
    ], string='Household Type', help="Type of household.")

    immigration_status = fields.Selection([
        ('none', 'None'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Immigration Status')

    referred_by = fields.Char(string='Referred By ')
    family_id = fields.Many2one('crm.client', string='Family ID', help="Family reference")

    @api.model
    def create(self, vals):
        if 'household' in vals and vals['household'] == 'family' and not vals.get('family_id'):
            # If it's a family and no family_id is set, create the record and set its own ID as family_id
            record = super(Client, self).create(vals)
            record.family_id = record.id
            record.client_id = str(record.id)
            record.write({'family_id': record.id})  # Update the family_id to be its own id

        elif 'household' in vals and vals['household'] == 'individual' and not vals.get('family_id'):
            # If it's a family and no family_id is set, create the record and set its own ID as family_id
            record = super(Client, self).create(vals)
            record.family_id = record.id
            record.client_id = str(record.id)
            record.write({'family_id': record.id})  # Update the family_id to be its own id

        else:
            record = super(Client, self).create(vals)
            record.client_id = str(record.id)
        return record

