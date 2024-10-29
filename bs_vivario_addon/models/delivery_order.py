from odoo import models, fields, api
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    closed_by_documents = fields.Boolean(string="Закрито документами", default=False)
    original_document_number = fields.Char(string="Номер документу")

    @api.onchange('closed_by_documents')
    def _onchange_closed_by_documents(self):
        if self.closed_by_documents:
            self.original_document_number = ''

    def action_done(self):
        # Check if the 'Закрито документами' is checked and document number is not filled
        if self.closed_by_documents and not self.original_document_number:
            raise UserError("Будь ласка, заповніть оригінальний номер документу.")
        return super(StockPicking, self).action_done()
