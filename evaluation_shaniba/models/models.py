# -*- coding: utf-8 -*-

from odoo import api, fields, models


class evaluationcustomer(models.Model):
     _name = 'evaluation.customer'
     _description = 'evaluation.customer'


     name= fields.Char('Customer')
     ch_number = fields.Integer('Check Number')
     amount = fields.Integer('Amount')
     state = fields.Selection([('confirm', 'confirm'), ('cancel', 'cancelled'), ('none', 'none')], default='none')


def my_confirm(self):
     self.state = 'confirm'

