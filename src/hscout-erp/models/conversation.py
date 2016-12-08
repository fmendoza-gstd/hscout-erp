# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Conversation(models.Model):
    _inherit = 'project.task'

    hscout = fields.Boolean()