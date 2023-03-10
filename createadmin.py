#!/usr/bin/env python
"""Create a standard admin user for testing purposes"""
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'openNPL.settings'
django.setup()
from django.contrib.auth.models import User

User.objects.create_superuser('admin', 'admin@example.com', 'admin')
