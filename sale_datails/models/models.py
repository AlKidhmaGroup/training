# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    mobile = fields.Char("Mobile")
    customer_uniq_id = fields.Char("Customer ID")
    payment_date = fields.Date("Payment Date")

    @api.model_create_multi
    def create(self, vals):
        print("sale order is debugging.....................................")
        print(vals)
        val_dict = vals and vals[0]
        val_dict['signed_by'] = 'sheza'
        val_dict['signed_on'] = datetime.now()
        val_dict['mobile'] = '555566655'
        return super(SaleOrder, self).create(vals)

    # def split_char(self, word):
    #     word_list = [ch for ch in word]
    #     print(word_list)
    #     return word_list and word_list[1]
    #
    # def write(self, vals):
    #     print(
    #         "HI  i am debugging when sale order edit from sale inherit module>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    #     ver = self.customer_uniq_id
    #     ver_no = self.split_char(ver) or 0
    #     ver_no = int(ver_no) + 1
    #     if ver_no:
    #         new_ver = 'v' + str(ver_no)
    #         vals['customer_uniq_id'] = new_ver
    #     return super(SaleOrder, self).write(vals)


class SaleOrderLines(models.Model):
    _inherit = 'sale.order.line'

    prod_ref_date = fields.Date("Product Ref Date")
    prod_ref_no = fields.Char("Product Ref")

class aksrespartner(models.Model):
    _inherit = 'res.partner'

    aks_record = fields.Char("Customer Record")
