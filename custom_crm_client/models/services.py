from odoo import api, models, fields


class Services(models.Model):
    _name = 'crm.services'
    _description = "CRM Services"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    partner_id = fields.Many2one('res.partner', required=True, auto_join=True, index=True)
    name = fields.Char('Name', required=True)
    service_id = fields.Char(string='Service ID', index=True, readonly=True, copy=False)
    description = fields.Text('Description')
    date = fields.Date(string='Date')
    responsible = fields.Char('Responsible')
    tags = fields.Many2one('crm.service.tag', string='Tag')
    contact = fields.Many2one('crm.client', string='Contact')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End date')

    services_location = fields.Selection([
        ('Mcaf', 'Mcaf'),
    ], string=" Service Location")

    ircc_services_type = fields.Selection([
        ('Information session', 'Information session'),
        ('Settlement Plan', 'Settlement Plan'),
        ('Resume', 'Resume')], string="IRCC Service Types")

    state = fields.Selection([
        ('new', 'New'),
        ('in-progress', 'In Progress'),
        ('delayed', 'Delayed'),
        ('done', 'Done')
    ], default="new", string="Status")

    @api.model
    def create(self, vals):
        record = super(Services, self).create(vals)
        record.service_id = str(record.id)
        return record
