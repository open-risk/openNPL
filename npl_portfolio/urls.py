# Copyright (c) 2020 - 2021 Open Risk (https://www.openriskmanagement.com)
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

from django.conf.urls import url
from openNPL import views

app_name = 'npl_portfolio'

urlpatterns = [
    # url(r'^$', views.npl_api_root, name='npl_api_root'),
    url(r'^counterparty_groups$', views.npl_counterparty_group_api, name='npl_counterparty_group_api'),
    url(r'^counterparty_groups/(?P<pk>[0-9]+)/$', views.npl_counterparty_group_detail,
        name='npl_counterparty_group_detail'),
    url(r'^counterparties$', views.npl_counterparty_api, name='npl_counterparty_api'),
    url(r'^counterparties/(?P<pk>[0-9]+)/$', views.npl_counterparty_detail, name='npl_counterparty_detail'),
    url(r'^property_collateral$', views.npl_property_collateral_api, name='npl_property_collateral_api'),
    url(r'^property_collateral/(?P<pk>[0-9]+)/$', views.npl_property_collateral_detail,
        name='npl_property_collateral_detail'),
    url(r'^loans$', views.npl_loan_api, name='npl_loan_api'),
    url(r'^loans/(?P<pk>[0-9]+)/$', views.npl_loan_detail, name='npl_loan_detail'),
    url(r'^enforcement$', views.npl_enforcement_api, name='npl_enforcement_api'),
    url(r'^enforcement/(?P<pk>[0-9]+)/$', views.npl_enforcement_detail, name='npl_enforcement_detail'),
    url(r'^forbearance$', views.npl_forbearance_api, name='npl_forbearance_api'),
    url(r'^forbearance/(?P<pk>[0-9]+)/$', views.npl_forbearance_detail, name='npl_forbearance_detail'),
    url(r'^nonproperty_collateral$', views.npl_nonproperty_collateral_api, name='npl_nonproperty_collateral_api'),
    url(r'^nonproperty_collateral/(?P<pk>[0-9]+)/$', views.npl_nonproperty_collateral_detail,
        name='npl_nonproperty_collateral_detail'),
    url(r'^external_collection$', views.npl_external_collection_api, name='npl_external_collection_api'),
    url(r'^external_collection/(?P<pk>[0-9]+)/$', views.npl_external_collection_detail,
        name='npl_external_collection_detail'),
]
