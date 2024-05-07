from odoo import models, fields


class Department(models.Model):
    _inherit = 'hr.department'

    # Many2many relationship to crm.client
    crm_client_ids = fields.Many2many(
        comodel_name='crm.client',
        relation='department_client_rel',  # intermediate relation table
        column1='department_id',
        column2='client_id',
        string='CRM Clients'
    )
