# -*- coding: utf-8 -*-
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models


class MedicalOperationalSector(models.Model):
    _name = 'medical.operational.sector'
    _description = 'Medical Operational Sector'

    name = fields.Char(string='Name', required=True)
    area_id = fields.Many2one(
        string='Operational Area', required=True,
        comodel_name='medical.operational.area', index=1)
    notes = fields.Text(string='Notes')

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(area_id, name)',
         'Sector name must be unique per area!'),
    ]

    def copy_data(self, cr, uid, id, default=None, context=None):
        res = super(MedicalOperationalSector, self).copy_data(
            cr, uid, id, default=default, context=context)
        res = dict(res or {})
        res['name'] = _('%s (copy)') % res.get('name', '?')
        return res
