from odoo import models, fields


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    purchase_limit = fields.Boolean(string='Activate Purchase Limit')
    set_limit = fields.Monetary(string='Set Limit')
