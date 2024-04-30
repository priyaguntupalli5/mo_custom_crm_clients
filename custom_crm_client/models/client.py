from odoo import models, fields, api, _


class Client(models.Model):
    _name = 'crm.client'
    _description = 'CRM Client'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade', auto_join=True, index=True)
    client_id = fields.Char(string='Client ID', index=True, readonly=True, copy=False)
    family_id = fields.Many2one('crm.family', string='Family')

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

    @api.model
    def create(self, vals):
        record = super(Client, self).create(vals)
        record.client_id = str(record.id)
        return record
