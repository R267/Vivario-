from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    closed_by_documents = fields.Boolean(string=_("Closed by documents"), default=False)
    original_document_number = fields.Char(string=_("Document number"))

    @api.onchange('closed_by_documents')
    def _onchange_closed_by_documents(self):
        if self.closed_by_documents:
            self.original_document_number = ''

    def action_done(self):
        # Check if the 'Closed by documents' is checked and document number is not filled
        if self.closed_by_documents and not self.original_document_number:
            raise UserError(_("Please fill in the original document number."))
        return super(StockPicking, self).action_done()
