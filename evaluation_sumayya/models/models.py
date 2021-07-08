# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class customerdetails(models.Model):
    _name = 'customer.details'
    _description = 'customer.details'

    name = fields.Char('Customer Name', required=True)
    # cust_name = fields.Many2one('res.partner', string='Customer')
    check_number = fields.Char('Check Number')
    amount = fields.Char('Amount')
    phone_no = fields.Char('Phone Number')
    email = fields.Char('email id')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('registered', 'Registered'), ('cancelled', 'Cancelled')],
        string='State', default='draft')

    def btn_confirm(self):
        print('button..........')
        self.state = 'confirmed'

    def btn_cancel(self):
        self.state = 'cancelled'

    def btn_register(self):
        self.state = 'registered'

# class partner(models.Model):
#     _inherit = 'res.partner'
#     a = fields.One2many('customer.details', 'cust_name', string='a')

    # @api.onchange('name')
    # def _onchange_res_partner(self):
    #     self.phone_no = self.name.phone_no
    #     self.email = self.name.email
