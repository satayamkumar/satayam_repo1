# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class BaseDocumentLayout(models.TransientModel):
    _inherit = "base.document.layout"

    imagef = fields.Char(related='company_id.imagef', readonly=False,
                         default="This is a system generated report hence doesn't require any signature.")
