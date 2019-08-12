
# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    sale_fiscal_type = fields.Selection([
        ("final", "Consumo"),
        ("fiscal", "Crédito Fiscal"),
        ("gov", "Gubernamental"),
        ("special", "Regímenes Especiales"),
        ("unico", "Único Ingreso"),
        ("export", "Exportaciones"),
    ],
        string="Tipo de comprobante",
        default="final")

    ncf_control = fields.Boolean(
        compute='check_ncf_control',
        store=True
    )

    @api.one
    @api.depends('template_id', 'template_id.journal_id', 'template_id.journal_id.ncf_control')
    def check_ncf_control(self):
        ncf_control = self.template_id and self.template_id.journal_id.ncf_control
        self.ncf_control = ncf_control
        return ncf_control

    @api.onchange('partner_id', 'template_id')
    def update_fiscal_type(self):
        if self.ncf_control:
            self.sale_fiscal_type = self.partner_id.sale_fiscal_type

    def _prepare_invoice_data(self):
        res = super(SaleSubscription, self)._prepare_invoice_data()
        if self.ncf_control:
            res['sale_fiscal_type'] = self.sale_fiscal_type
        return res