# -*- coding: utf-8 -*-

from odoo import api, fields, models


class akspurchaseorder(models.Model):
     _inherit = 'purchase.order'

     
     aks_newname = fields.Char('Order')

class purchaseorderline(models.Model):
     _inherit = 'purchase.order.line'  

     pro_cat = fields.Char('Product Catogary')   
     