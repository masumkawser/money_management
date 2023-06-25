from odoo import fields, models

class Expense(models.Model):
    _name = 'money.management.expense'

    name = fields.Char(string='Expense Name')
    amount = fields.Float(string='Amount')
    money_management_id = fields.Many2one('money.management', string='Money Management')