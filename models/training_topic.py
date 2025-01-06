from odoo import models, fields

class TrainingTopic(models.Model):
    _name = 'training.topic'
    _description = 'Training Topic'

    name = fields.Char('Topic Name', required=True)
    description = fields.Text('Description')