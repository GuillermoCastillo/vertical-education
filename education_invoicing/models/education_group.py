
# Copyright 2017 Pesol (<http://pesol.es>)
#                Angel Moya <angel.moya@pesol.es>
#                Luis Adan Jimenez Hernandez <luis.jimenez@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class EducationGroup(models.Model):
    _inherit = 'education.group'

    invoicing_method_ids = fields.One2many(
        comodel_name='education.invoicing.method',
        inverse_name='group_id',
        string='Invoicing Methods')
