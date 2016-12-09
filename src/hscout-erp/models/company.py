# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Company(models.Model):
    _inherit = 'res.company'
    
    company_id = fields.Many2one('res.company', 'Company')
    next_conversation = fields.Integer('Next Conversation')
    open_tracking = fields.Boolean('Open Tracking')
    conversation_lock = fields.Integer('Conversation Lock')
    time_zone = fields.Char('Time Zone')
    time_format = fields.Selection([('12hour', '12-hour clock'), ('24hour', '24-hour clock')], 'Time Format', default='12hour')
