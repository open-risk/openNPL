# Copyright (c) 2020 - 2024 Open Risk (https://www.openriskmanagement.com)
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

from . import views as api_views

app_name = 'sflp_portfolio'

urlpatterns = [
    re_path(r'^', api_views.sflp_api_root, name='sflp_api_root'),
    re_path(r'^counterparties$',
            api_views.sflp_counterparty_api,
            name='sflp_counterparty_api'),
    re_path(r'^counterparties/(?P<pk>[0-9]+)/$',
            api_views.sflp_counterparty_detail,
            name='sflp_counterparty_detail'),
    re_path(r'^property_collateral$',
            api_views.sflp_property_collateral_api,
            name='sflp_property_collateral_api'),
    re_path(r'^property_collateral/(?P<pk>[0-9]+)/$',
            api_views.sflp_property_collateral_detail,
            name='sflp_property_collateral_detail'),
    re_path(r'^loans$',
            api_views.sflp_loan_api,
            name='sflp_loan_api'),
    re_path(r'^loans/(?P<pk>[0-9]+)/$',
            api_views.sflp_loan_detail,
            name='sflp_loan_detail'),
    re_path(r'^enforcement$',
            api_views.sflp_enforcement_api,
            name='sflp_enforcement_api'),
    re_path(r'^enforcement/(?P<pk>[0-9]+)/$',
            api_views.sflp_enforcement_detail,
            name='sflp_enforcement_detail'),
    re_path(r'^forbearance$',
            api_views.sflp_forbearance_api,
            name='sflp_forbearance_api'),
    re_path(r'^forbearance/(?P<pk>[0-9]+)/$',
            api_views.sflp_forbearance_detail,
            name='sflp_forbearance_detail'),
    #
    #  DATA IMPORT URL's
    #
    # re_path(
    #     r"^import/",
    #     CreateImportView.as_view(),
    #     name="import_create"
    # ),
    # re_path(
    #     r"^import/<str:uuid>/setup/",
    #     SetupImportView.as_view(),
    #     name="import_setup",
    # ),
    # re_path(
    #     r"^import/<str:uuid>/dry-run/",
    #     DryRunImportView.as_view(),
    #     name="import_dry_run",
    # ),
    # re_path(
    #     r"^import/<str:uuid>/run/",
    #     ExecuteImportView.as_view(),
    #     name="import_execute",
    # ),
]
