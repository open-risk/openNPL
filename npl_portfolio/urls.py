# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
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

from django.urls import path, include
from html5lib.constants import namespaces
from rest_framework.routers import DefaultRouter

app_name = 'npl_portfolio'

from .views import npl_counterparty_api, npl_counterpartygroup_api, npl_property_collateral_api, npl_loan_api, \
    npl_enforcement_api, npl_forbearance_api, npl_nonproperty_collateral_api, npl_external_collection_api, \
    npl_historical_repayment_api

router = DefaultRouter()
router.register(r'counterparties', npl_counterparty_api, basename='counterparty')
router.register(r'counterparty_groups', npl_counterpartygroup_api, basename='counterpartygroup')
router.register(r'propertycollateral', npl_property_collateral_api, basename='propertycollateral')
router.register(r'loans', npl_loan_api, basename='loan')
router.register(r'enforcement', npl_enforcement_api, basename='enforcement')
router.register(r'forbearance', npl_forbearance_api, basename='forbearance')
router.register(r'nonpropertycollateral', npl_nonproperty_collateral_api, basename='nonpropertycollateral')
router.register(r'externalcollection', npl_external_collection_api, basename='externalcollection')
router.register(r'historicalrepayment', npl_historical_repayment_api, basename='historicalrepayment')

urlpatterns = [
    path('', include(router.urls)),
]
