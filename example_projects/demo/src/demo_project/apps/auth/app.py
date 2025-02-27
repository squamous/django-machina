# -*- coding: utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

# Third party imports
from django.conf.urls import include
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from machina.core.app import Application

# Local application / specific library imports
from demo_project.apps.auth import views


class AuthApp(Application):
    name = None

    user_create_view = views.UserCreateView
    user_parameters_update_view = views.UserAccountParametersUpdateView
    user_password_update_view = views.UserPasswordUpdateView

    def get_urls(self):
        return [
            url(r'^', include('django.contrib.auth.urls')),
            url(_(r'^parameters/edit/'), self.user_parameters_update_view.as_view(), name='account-parameters'),
            url(_(r'^password/edit/'), self.user_password_update_view.as_view(), name='account-password'),
            url(_(r'^register/'), self.user_create_view.as_view(), name='register'),
        ]


application = AuthApp()
