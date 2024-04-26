from odoo import http
from odoo.http import request


class ClientController(http.Controller):
    @http.route('/crm/client/new', auth='user', website=True)
    def new_client_form(self, **kwargs):
        return request.render("custom_crm_client.client_form")

    @http.route('/crm/client/submit', type='http', auth='user', methods=['POST'], website=True)
    def submit_client(self, **post):
        try:
            client_vals = {
                'name': post.get('name'),
                'phone': post.get('phone'),
                'email': post.get('email'),
                'household': post.get('household'),
                # Assume family_id comes from the form if needed, or is handled by default logic
                'family_id': post.get('family_id', False)
            }
            new_client = request.env['crm.client'].sudo().create(client_vals)
            return request.redirect('/thank_you')
        except Exception as e:
            return request.render("custom_crm_client.error_template", {'error': str(e)})

    @http.route('/thank_you', auth='public', website=True)
    def thank_you(self, **kwargs):
        return request.render("custom_crm_client.thank_you_template")
