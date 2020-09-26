# Copyright (c) 2020 Open Risk (https://www.openriskmanagement.com)
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

app_name = 'eba_portfolio'

urlpatterns = [
    # url(r'^$', views.eba_api_root, name='eba_api_root'),
    url(r'^counterparty_groups$', views.eba_counterparty_group_api, name='eba_counterparty_group_api'),
    url(r'^counterparties$', views.eba_counterparty_api, name='eba_counterparty_api'),
    url(r'^counterparties/(?P<pk>[0-9]+)/$', views.eba_counterparty_detail, name='eba_counterparty_detail'),
    url(r'^property_collateral$', views.eba_property_collateral_api, name='eba_property_collateral_api'),
    url(r'^property_collateral/(?P<pk>[0-9]+)/$', views.eba_property_collateral_detail, name='eba_property_collateral_detail'),
    url(r'^loans$', views.eba_loan_api, name='eba_loan_api'),
    url(r'^loans/(?P<pk>[0-9]+)/$', views.eba_loan_detail, name='eba_loan_detail'),
    url(r'^enforcements$', views.eba_enforcement_api, name='eba_enforcement_api'),
    url(r'^forbearance$', views.eba_forbearance_api, name='eba_forbearance_api'),
    url(r'^nonproperty_collateral$', views.eba_nonproperty_collateral_api, name='eba_nonproperty_collateral_api'),
    url(r'^external_collections$', views.eba_external_collection_api, name='eba_external_collection_api'),
]