# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Customer(models.Model):
    _inherit = 'ir.partner'

    hscout_first_name = fields.Char('First Name')
    hscout_last_name = fields.Char('Last Name')
