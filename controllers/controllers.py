# -*- coding: utf-8 -*-
# from odoo import http


# class MoneyManagement(http.Controller):
#     @http.route('/money_management/money_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/money_management/money_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('money_management.listing', {
#             'root': '/money_management/money_management',
#             'objects': http.request.env['money_management.money_management'].search([]),
#         })

#     @http.route('/money_management/money_management/objects/<model("money_management.money_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('money_management.object', {
#             'object': obj
#         })
