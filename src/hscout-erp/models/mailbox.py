# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Mailbox(models.Model):
    _inherit = 'project.project'

    hs_is_helpdesk = fields.Boolean('HelpDesk')
    hs_from_name = fields.Selection([('mailbox', 'Mailbox Name'), ('user', 'User name'), ('custom', 'Custom Name')], 'From Name', default='mailbox')
    hs_default_status = fields.Selection([('active', 'Active'), ('pending', 'Pending'), ('closed', 'Closed')], 'Default Status')
    hs_default_assignee = fields.Selection([('anyone', 'Active'), ('person_reply_unassigned', 'Person Replying (if Unassigned)'), ('person_reply', 'Person Replying')], 'Default Assignee')
    hs_email_template = fields.Selection([('plain', 'Plain Template'), ('fancy', 'Fancy Template')], 'Email Template')
    hs_email_signature = fields.Html('Email Signature')
    