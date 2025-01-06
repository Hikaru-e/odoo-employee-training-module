from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SessionEnrollWizard(models.TransientModel):
    _name = 'session.enroll.wizard'
    _description = 'Enroll Employees Wizard'

    session_id = fields.Many2one('training.session', string='Session', required=True, default=lambda self: self._default_session())
    employee_ids = fields.Many2many('hr.employee', string='Employees')

    @api.model
    def _default_session(self):
        session = self.env['training.session'].search([], limit=1)
        if not session:
            topic = self.env['training.topic'].search([], limit=1)
            if not topic:
                topic = self.env['training.topic'].create({
                    'name': 'Default Topic',
                    'description': 'Default Description',
                })
            session = self.env['training.session'].create({
                'name': 'Default Session',
                'topic_id': topic.id,
                'start_date': fields.Datetime.now(),
                'end_date': fields.Datetime.now(),
            })
        return session.id

    def action_enroll_employees(self):
        Attendee = self.env['training.attendee']
        for wiz in self:
            if not wiz.session_id:
                raise ValidationError("Please specify a session.")
            for emp in wiz.employee_ids:
                Attendee.create({
                    'employee_id': emp.id,
                    'session_id': wiz.session_id.id,
                })