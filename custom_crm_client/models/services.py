from odoo import api, models, fields

class Services(models.Model):
    _name = 'crm.services'
    _description = "CRM Services"
   # _inherits = {'res.partner': 'partner_id'}
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Add inheritance



    partner_id = fields.Many2one('res.partner', required=True, auto_join=True, index=True)
    name = fields.Char('Name', required=True)
    service_id = fields.Char(string='Service ID', index=True, readonly=True, copy=False)
    description = fields.Text('Description')
    date = fields.Date(string='Date')
    responsible = fields.Char('Responsible')
    tags = fields.Char('Tags')
    contact = fields.Char('Contact')
    startdate = fields.Date(string='Start Date')
    enddate = fields.Date(string='End date')


    #stage_name = fields.One2many('crm.client', 'service_id', string='Stage Name')

    stage_ID = fields.Many2one('crm.service_stage',
                                string='Stage Name',
                                ondelete='set null',
                                help="Select a Stage.")
    uci_no = fields.Integer(string='UCI Number ')

    client_id = fields.Many2one('crm.client',  string='client_id')

    serviceslocation = fields.Selection([
        ('Mcaf', 'Mcaf'),
        ], string=" Service Location")

    ircc_servicestype = fields.Selection([
        ('Information session', 'Information session'),
        ('Settlement Plan', 'Settlement Plan'),
        ('Resume', 'Resume')], string="IRCC Service Types")

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

    @api.model
    def create(self, vals):
        record = super(Services, self).create(vals)
        record.service_id = str(record.id)
        return record