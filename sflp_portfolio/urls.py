# Copyright (c) 2020 - 2022 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from django.urls import re_path
from openNPL import sflp_views as views

app_name = 'sflp_portfolio'

urlpatterns = [
    re_path(r'^counterparties$', views.sflp_counterparty_api, name='sflp_counterparty_api'),
    re_path(r'^counterparties/(?P<pk>[0-9]+)/$', views.sflp_counterparty_detail, name='sflp_counterparty_detail'),
    re_path(r'^property_collateral$', views.sflp_property_collateral_api, name='sflp_property_collateral_api'),
    re_path(r'^property_collateral/(?P<pk>[0-9]+)/$', views.sflp_property_collateral_detail,
            name='sflp_property_collateral_detail'),
    re_path(r'^repayment_schedules$', views.sflp_repayment_schedule_api, name='sflp_repayment_schedule_api'),
    re_path(r'^repayment_schedules/(?P<pk>[0-9]+)/$', views.sflp_repayment_schedule_detail, name='sflp_repayment_schedule_detail'),
    re_path(r'^loans$', views.sflp_loan_api, name='sflp_loan_api'),
    re_path(r'^loans/(?P<pk>[0-9]+)/$', views.sflp_loan_detail, name='sflp_loan_detail'),
    re_path(r'^enforcement$', views.sflp_enforcement_api, name='sflp_enforcement_api'),
    re_path(r'^enforcement/(?P<pk>[0-9]+)/$', views.sflp_enforcement_detail, name='sflp_enforcement_detail'),
    re_path(r'^forbearance$', views.sflp_forbearance_api, name='sflp_forbearance_api'),
    re_path(r'^forbearance/(?P<pk>[0-9]+)/$', views.sflp_forbearance_detail, name='sflp_forbearance_detail'),
]
