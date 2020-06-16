# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    standard_price = fields.Float(
        groups='users_prices_security.standard_price',
    )
