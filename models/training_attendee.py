from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TrainingAttendee(models.Model):
    _name = 'training.attendee'
    _description = 'Training Attendee'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    session_id = fields.Many2one('training.session', string='Session', required=True)
    check_in = fields.Boolean('Checked In', default=False)

    @api.model
    def create(self, vals):
        session = self.env['training.session'].browse(vals.get('session_id'))
        if session.seat_limit and len(session.attendee_ids) >= session.seat_limit:
            raise ValidationError("No more seats available for this session.")
        return super().create(vals)