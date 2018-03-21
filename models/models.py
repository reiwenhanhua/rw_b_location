# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Location(models.Model):
    _name = 'rw_b_location.location'
    
    name = fields.Char(string='省区', required=True)
    code = fields.Char(string='邮编')
