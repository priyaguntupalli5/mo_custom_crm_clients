from odoo import api, models, fields

class Services(models.Model):
    _name = 'crm.services'
    _description = "CRM Services"
   # _inherits = {'res.partner': 'partner_id'}



    partner_id = fields.Many2one('res.partner', required=True, auto_join=True, index=True)
    name = fields.Char('Name', required=True)
    service_id = fields.Char(string='Service ID', index=True, readonly=True, copy=False)
    description = fields.Text('Description')
    date = fields.Date(string='Date')
    responsible = fields.Char('Responsible')
    tags = fields.Char('Tags')
    contact = fields.Char('Contact')
    enddate = fields.Date(string='End date')

    stage_id = fields.Many2one('crm.service.stage',  string='Stage',group_expand='_expand_stage_groups')

    client_id = fields.Many2one('crm.client',  string='client_id')

    serviceTypes = fields.Selection([
    ('Information session', 'Information session'),
    ('Settlement Plan', 'Settlement Plan'),
    ('Resume', 'Resume')], string="Service Types")

    state = fields.Selection([
        ('new','New'),
        ('in-progress','In Progress'),
        ('delayed', 'Delayed'),
        ('done', 'Done')
    ], default="new", string="Status")

    def _expand_stage_groups(self, stages, domain, order):
        return stages.search([], order=order)

