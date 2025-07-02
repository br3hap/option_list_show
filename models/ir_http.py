# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class IrHttp(models.Model):
    _inherit = 'ir.http'

    def session_info(self):
        session_info = super().session_info()
        session_info["option_show"] = self.env.user.option_show
        return session_info
