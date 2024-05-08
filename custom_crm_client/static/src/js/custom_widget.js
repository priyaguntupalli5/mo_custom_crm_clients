/** @odoo-module **/

import { useState, onMounted } from '@odoo/owl';
import { FormRenderer } from '@web/views/form/form_renderer';
import { registry } from '@web/core/registry';

class DynamicNotebook extends FormRenderer {
    setup() {
        super.setup();
        this.state = useState({ departments: [] });
    }

    async willStart() {
        super.willStart();
        await this.loadDepartments();
    }

    async loadDepartments() {
        const departments = await this.env.services.rpc({
            model: 'crm.client',
            method: 'get_departments',
            args: [[]],
        });
        this.state.departments = departments;
    }

    render() {
        super.render(); // Ensures parent renderings are handled
        this.addDynamicTabs(); // Add dynamic tabs after rendering
    }

    addDynamicTabs() {
        const $notebook = this.el.querySelector('.oe_notebook');
        if ($notebook && this.state.departments.length > 0) {
            this.state.departments.forEach(dept => {
                const page = document.createElement('div');
                page.className = 'oe_notebook_page';
                const header = document.createElement('h3');
                header.textContent = dept.name;
                page.appendChild(header);
                $notebook.appendChild(page);
            });
        } else {
            console.error("Notebook element not found or no departments available.");
        }
    }
}

registry.category('views').add('dynamic_notebook', DynamicNotebook);
