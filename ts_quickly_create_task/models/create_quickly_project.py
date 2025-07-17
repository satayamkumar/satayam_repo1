from odoo import models, fields, api,_


class QuickCreateTask(models.Model):
    _name = "quick.task.wizard"
    _description = "Create quick task"

    name = fields.Char(string='Task')
    project_id = fields.Many2one('project.project', string='Project')
    deadline_date = fields.Date(string='Deadline')
    user_ids = fields.Many2many('res.users', relation='project_quickly_task_user_rel', column1='quickly_task_id',
                                column2='users_id', string='Assignees', context={'active_test': False}, tracking=True)
    task_stage_id = fields.Many2one('project.task.type', string='Stage')

    def create_project(self):
        task_vals = {
            'name': self.name,
            'project_id': self.project_id.id,
            'date_deadline': self.deadline_date,
            'stage_id': self.task_stage_id.id,
            'user_ids': [(6, 0, self.user_ids.ids)]
        }
        self.env['project.task'].create(task_vals)

    def create_and_edit_project(self):
        """Create task and return an action to open it in edit mode"""
        task_vals = {
            'name': self.name,
            'project_id': self.project_id.id,
            'date_deadline': self.deadline_date,
            'stage_id': self.task_stage_id.id,
            'user_ids': [(6, 0, self.user_ids.ids)]
        }
        task = self.env['project.task'].create(task_vals)

        # Return an action to open the newly created task in form view
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'view_mode': 'form',
            'res_id': task.id,
            'target': 'current',
        }


class User(models.Model):
    _inherit = 'res.users'

    task_id = fields.Many2one('project.task')