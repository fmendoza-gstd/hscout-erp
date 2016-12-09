# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Mailbox(models.Model):
    _inherit = 'project.project'

    is_hscout = fields.Boolean('HelpDesk')
    from_name = fields.Selection([('mailbox', 'Mailbox Name'), ('user', 'User name'), ('custom', 'Custom Name')], 'From Name', default='mailbox')
    default_status = fields.Selection([('active', 'Active'), ('pending', 'Pending'), ('closed', 'Closed')], 'Default Status')
    default_assignee = fields.Selection([('anyone', 'Active'), ('person_unassigned', 'Person Replying (if Unassigned)'), ('person_unassigned', 'Person Replying')], 'Default Assignee')
    email_template = fields.Selection([('plain', 'Plain Template'), ('fancy', 'Fancy Template')], 'Email Template')
    email_signature = fields.Html('Email Signature')
    