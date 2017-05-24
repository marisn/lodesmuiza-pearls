# -*- coding: utf8 -*-
import os
import sys
import site
sys.stdout = sys.stderr

site.addsitedir('/home/django_projekti/virtuals/lodesmuiza/lib/python2.6/site-packages/')

#path = '/home/django_projekti/django-trunk'
#if path not in sys.path:
#    sys.path.append(path)

sys.path.append('/home/lodesmuiza/djlodesmuiza/')
activate_env=os.path.expanduser('/home/django_projekti/virtuals/lodesmuiza/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

os.environ['DJANGO_SETTINGS_MODULE'] = 'djlodesmuiza.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
