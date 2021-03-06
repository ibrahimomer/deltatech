# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
# See README.rst file on addons root folder for license details

from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp


class account_invoice(models.Model):
    _inherit = "account.invoice"

    weight = fields.Float('Gross Weight', digits=dp.get_precision('Stock Weight'), help="The gross weight in Kg.")
    weight_net = fields.Float('Net Weight', digits=dp.get_precision('Stock Weight'), help="The net weight in Kg.")
    weight_package = fields.Float('Package Weight', digits=dp.get_precision('Stock Weight'))
