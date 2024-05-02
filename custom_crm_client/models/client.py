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

    #Personal Details tab
    #Personal details
    referred_by_selection = fields.Selection([
        ('not referred', 'Not referred'),
        ('school', 'School'),
        ('other settlement service provider','Other settlement service provider'),
        ('overseas orientation session', 'Overseas orientation session (e.g. CIIP)'),
        ('in-canada orientation session', 'In-Canada orientation session'),
        ('Non-governmental newspaper/media/publication/brochure/Website', 'Non-governmental newspaper/media/publication/brochure/Website'),
        ('internal to my organization', 'Internal to my organization'),
        ('immigration consultant/lawyer', 'Immigration Consultant/Lawyer'),
        ('government publication/brochure/website','Government publication/brochure/Website'),
        ('canadian government agency', 'Canadian Government Agency'),
        ('family/ friends','Family/ Friends'),
        ('ethnic or religious organization','Ethnic or religious organization'),
        ('employer/ co-worker','Employer/ Co-worker'),
        ('community cerner/ library','Community Cerner/ Library')
    ], string="Referred By")
    arrival_date_or_expected_date = fields.Datetime(string="Arrival Date/Expected Date")
    landing_date =fields.Datetime(string="Landing Date")
    english_level = fields.Selection([
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced")
    ], string="English Level")
    languages_spoken = fields.Char(string="Languages Spoken")
    present_living_situation = fields.Char(string="Present Living Situation")
    #other details
    mcaf_electronic_messages = fields.Boolean(string="MCAF's Electronic Messages")
    share_info_with_mcaf = fields.Boolean(string="Share information with MCAF Staff")
    consent_from_ircc = fields.Boolean(string="Consent for Future Research/Consultation from IRCC")
    virtual_info_sessions = fields.Boolean(string="Virtual information sessions")

    @api.model
    def create(self, vals):
        record = super(Client, self).create(vals)
        record.client_id = str(record.id)
        return record
