from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class FamilyClientController(http.Controller):
    @http.route('/crm/family/create', auth='user', type='http', methods=['GET'], website=True)
    def create_family_form(self, **kw):
        States = request.env['res.country.state'].search([])
        return request.render('custom_crm_client.crm_family_form_template', {'states': States})

    @http.route('/crm/family/submit', type='http', auth='public', methods=['POST'], website=True)
    def submit_family(self, **kw):
        try:
            Family = request.env['crm.family']
            Client = request.env['crm.client']

            family_data = {
                'name': request.httprequest.form.get('family_name'),
                'family_phone': request.httprequest.form.get('family_phone'),
                'family_email': request.httprequest.form.get('family_email')
            }
            family = Family.create(family_data)

            client_names = request.httprequest.form.getlist('client_name[]')
            client_phones = request.httprequest.form.getlist('client_phone[]')
            client_emails = request.httprequest.form.getlist('client_email[]')
            client_streets = request.httprequest.form.getlist('client_street[]')
            client_streets2 = request.httprequest.form.getlist('client_street2[]')
            client_cities = request.httprequest.form.getlist('client_city[]')
            client_state_ids = request.httprequest.form.getlist('client_state_id[]')

            for name, phone, email, street, street2, city, state_id in zip(client_names, client_phones, client_emails,
                                                                           client_streets, client_streets2,
                                                                           client_cities,
                                                                           client_state_ids):
                if name:
                    Client.create({
                        'name': name,
                        'phone': phone,
                        'email': email,
                        'street': street,
                        'street2': street2,
                        'city': city,
                        'state_id': int(state_id) if state_id else False,
                        'family_id': family.id
                    })

            return request.render('custom_crm_client.submission_thanks', {})
        except Exception as e:
            _logger.error("Error submitting form: %s", e)
            return request.render('custom_crm_client.error_template', {'error': str(e)})
