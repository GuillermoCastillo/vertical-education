# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields, api


class OpClassroom(models.Model):
    _name = 'education.classroom'

    name = fields.Char('Name', size=16, required=True)
    code = fields.Char('Code', size=4, required=True)
    course_id = fields.Many2one('education.course', 'Course')
    batch_id = fields.Many2one('education.batch', 'Batch')
    capacity = fields.Integer(string='No of Person')
    facilities = fields.One2many(
        'education.facility.line', 'classroom_id', string='Facility Lines')
    asset_line = fields.One2many('education.asset', 'asset_id', 'Asset')

    @api.onchange('course_id')
    def onchange_course(self):
        self.batch_id = False
