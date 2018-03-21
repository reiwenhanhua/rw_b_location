# -*- coding: utf-8 -*-
from odoo import http

# class RwhhHeadhunter(http.Controller):
#     @http.route('/rwhh_headhunter/rwhh_headhunter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rwhh_headhunter/rwhh_headhunter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rwhh_headhunter.listing', {
#             'root': '/rwhh_headhunter/rwhh_headhunter',
#             'objects': http.request.env['rwhh_headhunter.rwhh_headhunter'].search([]),
#         })

#     @http.route('/rwhh_headhunter/rwhh_headhunter/objects/<model("rwhh_headhunter.rwhh_headhunter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rwhh_headhunter.object', {
#             'object': obj
#         })