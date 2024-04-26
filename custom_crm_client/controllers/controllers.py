from odoo import http
from odoo.http import request


class ClientController(http.Controller):
    @http.route('/crm/client/new', auth='user', website=True)
    def new_client_form(self, **kwargs):
        # Initialize or clear any existing session data for the form
        request.session['client_form_data'] = {}
        return request.render("custom_crm_client.client_form")

    @http.route('/crm/client/save_temp', type='http', auth='user', methods=['POST'], website=True)
    def save_temp_client(self, **post):
        # Temporarily save data in session
        client_form_data = request.session.get('client_form_data', {})
        client_form_data.update(post)
        request.session['client_form_data'] = client_form_data
        if post.get('household') == 'family':
            # Redirect to add family members if household type is 'family'
            return request.redirect('/crm/client/add_family_member')
        return request.redirect('/thank_you')  # Redirect if no family members to add

    @http.route('/crm/client/add_family_member', type='http', auth='user', methods=['GET', 'POST'], website=True)
    def add_family_member(self, **post):
        if request.httprequest.method == 'POST':
            # Add family member data to session
            client_form_data = request.session.get('client_form_data', {})
            family_members = client_form_data.get('family_members', [])
            family_members.append(post)
            client_form_data['family_members'] = family_members
            request.session['client_form_data'] = client_form_data
            return request.redirect('/thank_you')  # Redirect to final submit or add more members
        return request.render("custom_crm_client.add_family_member_form")

    @http.route('/crm/client/final_submit', type='http', auth='user', methods=['POST'], website=True)
    def final_submit(self):
        client_form_data = request.session.pop('client_form_data', None)
        if client_form_data:
            new_client = request.env['crm.client'].sudo().create(client_form_data)
            for member_data in client_form_data.get('family_members', []):
                member_data['family_id'] = new_client.id
                request.env['crm.client'].sudo().create(member_data)
        return request.redirect('/thank_you')
