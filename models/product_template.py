# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    standard_price = fields.Float(
        groups='users_prices_security.standard_price',
    )
