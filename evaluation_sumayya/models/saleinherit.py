# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    cust_ref_field = fields.Char("Custom Reference Field")
