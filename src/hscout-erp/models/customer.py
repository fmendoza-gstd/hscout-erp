# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SocialNetwork(models.Model):
    _name = 'hscout.social.network'
    _description = 'Social Network'

    name = fields.Char('Name')


class Customer(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    social_network_ids = fields.One2many('hscout.customer.social.network', 'customer_id', 'Social Networks')


class CustomerSocialNetwork(models.Model):
    _name = 'hscout.customer.social.network'
    _description = 'Customer Social Network'

    customer_id = fields.Many2one('res.partner', 'Customer')
    type = fields.Many2one('hscout.social.network', 'Type')
    url = fields.Char('URL')
    