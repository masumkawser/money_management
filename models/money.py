from odoo import fields, models, api

class MoneyManagement(models.Model):
    _name = 'money.management'
    
    name = fields.Char(string="Name")
    money_management_id = fields.Float(string="Money")  
  
    total_income = fields.Float(string='Total Income')
    total_expense = fields.Float(string='Total Expense')
    new_balance = fields.Float(string='New Balance', compute='_compute_new_balance', store=True)

    @api.depends('total_income', 'total_expense')
    def _compute_new_balance(self):
        for record in self:
            record.new_balance = record.total_income - record.total_expense

    @api.depends('income_ids.amount')
    def _compute_total_income(self):
        for record in self:
            record.total_income = sum(record.income_ids.mapped('amount'))

    @api.depends('expense_ids.amount')
    def _compute_total_expense(self):
        for record in self:
            record.total_expense = sum(record.expense_ids.mapped('amount'))

    @api.depends('total_income', 'total_expense')
    def _compute_new_balance(self):
        for record in self:
            record.new_balance = record.total_income - record.total_expense

    # @api.depends('income_ids.amount')
    # def _compute_total_income(self):
    #     for record in self:
    #         record.total_income = sum(record.income_ids.mapped('amount'))

    # @api.depends('expense_ids.amount')
    # def _compute_total_expense(self):
    #     for record in self:
    #         record.total_expense = sum(record.expense_ids.mapped('amount'))

    # @api.depends('total_income', 'total_expense')
    # def _compute_available_balance(self):
    #     for record in self:
    #         record.avail