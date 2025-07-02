# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'


    option_show = fields.Boolean(
        string="Opcion de Mostrar botón",
        default=False
    )
