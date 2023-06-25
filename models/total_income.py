from odoo import fields, models

class Income(models.Model):
    _name = 'money.management.income'

    name = fields.Char(string='Income Name')
    amount = fields.Float(string='Amount')
    money_management_id = fields.Many2one('money.management', string='Money Management')