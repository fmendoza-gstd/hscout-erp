# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Company(models.Model):
    _inherit = 'res.company'
    
    hs_next_conversation = fields.Integer('Next Conversation')
    hs_open_tracking = fields.Boolean('Open Tracking')
    hs_conversation_lock = fields.Integer('Conversation Lock')
    hs_time_zone = fields.Char('Time Zone')
    hs_time_format = fields.Selection([('12hour', '12-hour clock'), ('24hour', '24-hour clock')], 'Time Format', default='12hour')
