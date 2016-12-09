# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Customer(models.Model):
    _inherit = 'res.partner'

    billing_email = fields.Char('Billing Email')
    time_zone = fields.Char('Time Zone')
    time_format = fields.Selection([('12hour', '12-hour clock'), ('24hour', '24-hour clock')], 'Time Format', default='12hour')
