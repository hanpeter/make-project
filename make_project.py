# -*- coding: utf-8 -*-

from __future__ import absolute_import
from os.path import join
import subprocess
import click
import simplejson


CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help']
}


class Application(object):
    DEFAULT_GITHUB_OWNER = 'krux'
    VERSION = '0.0.1'

    _GIT_CLONE = 'git clone git@github.com:{owner}/{repo}.git {project_home}/{repo}'
    _MKVIRTUALENV = 'virtualenv {workon_home}/{virtualenv}'
    _SUBLIME_PROJECT_FILE = '{project_name}.sublime-project'
    _SUBLIME_PROJECT_TEMPLATE = {
        'folders': [{
            'path': None,
            'folder_exclude_patterns': ['build', 'cover', 'dist', '*.egg-info'],
            'file_exclude_patterns': ['.coverage', '.noseids']
        }]
    }

    def __init__(self, name):
        self.name = name

    def git_clone(self, project_home, owner=DEFAULT_GITHUB_OWNER):
        return subprocess.call(
            self._GIT_CLONE.format(owner=owner, repo=self.name, project_home=project_home),
            shell=True
        )

    def virtualenv(self, workon_home, is_old_pip=False):
        return subprocess.call(
            self._MKVIRTUALENV.format(workon_home=workon_home, virtualenv=self.name),
            shell=True
        )

    def sublime_project(self, project_home):
        with open(join(project_home, self._SUBLIME_PROJECT_FILE.format(project_name=self.name)), 'w') as f:
            project = self._SUBLIME_PROJECT_TEMPLATE
            project['folders'][0]['path'] = self.name
            f.write(simplejson.dumps(project, indent='\t'))


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('name')
@click.option('--project-home', envvar='PROJECT_HOME', required=True, help='Directory to put all projects')
@click.option('--owner', default=Application.DEFAULT_GITHUB_OWNER, help='Owner of the GitHub repo')
@click.option('--workon-home', envvar='WORKON_HOME', required=True, help='Home directory for virtualenv')
@click.option('--use-old-pip', is_flag=True, help='If set, uses pip==1.4.1 instead of the latest')
@click.option('--no-git', is_flag=True, help='If set, skip git clone')
@click.option('--no-virtualenv', is_flag=True, help='If set, skip creating virtualenv')
@click.option('--no-sublime', is_flag=True, help='If set, skip creating sublime_project file')
@click.version_option(version=Application.VERSION)
def main(name, project_home, owner, workon_home, use_old_pip, no_git, no_virtualenv, no_sublime):
    app = Application(name=name)

    if not no_git:
        app.git_clone(project_home=project_home, owner=owner)

    if not no_virtualenv:
        app.virtualenv(workon_home=workon_home, is_old_pip=use_old_pip)

    if not no_sublime:
        app.sublime_project(project_home=project_home)


# Run the application stand alone
if __name__ == '__main__':
    main()
