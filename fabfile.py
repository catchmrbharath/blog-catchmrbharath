import os
from fabric.api import local, task

BASEDIR = os.path.abspath(os.path.curdir)
OUTPUTDIR = os.path.join(BASEDIR, 'output')
THEMEDIR = os.path.join(BASEDIR, 'theme')
INPUTDIR = os.path.join(BASEDIR, 'markdown')
CONFFILE = os.path.join(BASEDIR, 'pelicanconf.py')


def build():
    #local('find {} -type f -not -name ".git" |xargs rm'.format(OUTPUTDIR))
    local('pelican -d {} -t {} -o {} -s {}'.format(INPUTDIR, THEMEDIR, OUTPUTDIR, CONFFILE))


def push():
    local('cd {} && git init && git add . && git commit -m "build" '
            '&& git remote add origin https://github.com/catchmrbharath/catchmrbharath.github.com.git'
          ' && git push -f origin master'.format(OUTPUTDIR))


def all():
    build()
    push()
