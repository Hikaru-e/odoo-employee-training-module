from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Session'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Existing fields with tracking
    name = fields.Char('Session Name', required=True, tracking=True)
    topic_id = fields.Many2one('training.topic', string='Topic', required=True, tracking=True)
    instructor_id = fields.Many2one('hr.employee', string='Instructor', tracking=True)
    start_date = fields.Datetime('Start Date', required=True, tracking=True)
    end_date = fields.Datetime('End Date', required=True, tracking=True)
    seat_limit = fields.Integer('Seat Limit', tracking=True)
    attendee_ids = fields.One2many('training.attendee', 'session_id', string='Attendees')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done'),
    ], default='draft', tracking=True)

    # Statistics fields
    attendance_rate = fields.Float(compute='_compute_statistics', store=True)
    checked_in_count = fields.Integer(compute='_compute_statistics', store=True)
    total_attendees = fields.Integer(compute='_compute_statistics', store=True)

    @api.depends('attendee_ids', 'attendee_ids.check_in', 'seat_limit')
    def _compute_statistics(self):
        for session in self:
            session.total_attendees = len(session.attendee_ids)
            session.checked_in_count = len(session.attendee_ids.filtered(lambda a: a.check_in))
            session.attendance_rate = (session.total_attendees / session.seat_limit * 100) if session.seat_limit else 0

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for rec in self:
            if rec.end_date < rec.start_date:
                raise ValidationError('End date cannot be before start date.')



    def action_open(self):
        for rec in self:
            if rec.state != 'draft':
                raise ValidationError("Only draft sessions can be opened.")
            rec.state = 'open'
            _logger.info(f"Session {rec.name} state changed to Open.")

    def action_done(self):
        for rec in self:
            if rec.state != 'open':
                raise ValidationError("Only open sessions can be marked as done.")
            rec.state = 'done'
            _logger.info(f"Session {rec.name} state changed to Done.")
