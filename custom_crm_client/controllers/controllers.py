from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class ClientController(http.Controller):
    @http.route('/crm/client/new', auth='user', website=True)
    def new_client_form(self, **kwargs):
        request.session['client_form_data'] = {}
        return request.render("custom_crm_client.client_form")

    @http.route('/crm/client/save_temp', type='http', auth='user', methods=['POST'], website=True)
    def save_temp_client(self, **post):
        client_form_data = {
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'household': post.get('household'),
            # Ensure family_id is handled correctly; this seems unused or incorrectly set
        }
        request.session['client_form_data'] = client_form_data
        if post.get('household') == 'family':
            return request.redirect('/crm/client/add_family_member')
        return request.redirect('/crm/client/final_submit')

    @http.route('/crm/client/add_family_member', type='http', auth='user', methods=['GET', 'POST'], website=True)
    def add_family_member(self, **post):
        if request.httprequest.method == 'POST':
            client_form_data = request.session.get('client_form_data', {})
            family_member = {
                'name': post.get('name'),
                # Add other necessary fields here if your model requires them
            }
            if 'family_members' not in client_form_data:
                client_form_data['family_members'] = []
            client_form_data['family_members'].append(family_member)
            request.session['client_form_data'] = client_form_data
            _logger.info('Added family member: %s', family_member)
            return request.redirect('/crm/client/add_family_member')  # Loop to add more or proceed to finalize
        return request.render("custom_crm_client.add_family_member_form")

    @http.route('/crm/client/final_submit', type='http', auth='user', methods=['GET', 'POST'], website=True)
    def final_submit(self):
        try:
            client_form_data = request.session.pop('client_form_data', None)
            if client_form_data:
                new_client = request.env['crm.client'].sudo().create(client_form_data)
                family_members = client_form_data.get('family_members', [])
                for member_data in family_members:
                    member_data['family_id'] = new_client.id
                    request.env['crm.client'].sudo().create(member_data)
            return request.redirect('/thank_you')
        except Exception as e:
            _logger.error("Error during final submission: %s", e)
            return request.render("custom_crm_client.error_template", {'error': str(e)})

    @http.route('/thank_you', auth='public', website=True)
    def thank_you(self, **kwargs):
        return request.render("custom_crm_client.thank_you_template")
