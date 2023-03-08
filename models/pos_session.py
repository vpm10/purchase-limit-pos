from odoo import models


class AddCustomer(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_partner(self):
        result = super()._loader_params_res_partner()

        result['search_params']['fields'].append('set_limit')
        result['search_params']['fields'].append('purchase_limit')
        # print(result)
        return result
