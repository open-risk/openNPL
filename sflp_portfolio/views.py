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

from rest_framework import viewsets

from openNPL.sflp_serializers import SFLP_CounterpartySerializer, SFLP_CounterpartyDetailSerializer
from openNPL.sflp_serializers import SFLP_EnforcementSerializer, SFLP_EnforcementDetailSerializer
from openNPL.sflp_serializers import SFLP_ForbearanceSerializer, SFLP_ForbearanceDetailSerializer
from openNPL.sflp_serializers import SFLP_LoanSerializer, SFLP_LoanDetailSerializer
from openNPL.sflp_serializers import SFLP_PropertyCollateralSerializer, SFLP_PropertyCollateralDetailSerializer
from sflp_portfolio.models.counterparty import Counterparty
from sflp_portfolio.models.enforcement import Enforcement
from sflp_portfolio.models.forbearance import Forbearance
from sflp_portfolio.models.loan import Loan
from sflp_portfolio.models.property_collateral import PropertyCollateral


class sflp_counterparty_api(viewsets.ModelViewSet):
    queryset = Counterparty.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SFLP_CounterpartyDetailSerializer
        elif self.action == 'list':
            return SFLP_CounterpartySerializer
        return SFLP_CounterpartyDetailSerializer


class sflp_loan_api(viewsets.ModelViewSet):
    queryset = Loan.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SFLP_LoanDetailSerializer
        elif self.action == 'list':
            return SFLP_LoanSerializer
        return SFLP_LoanDetailSerializer


class sflp_property_collateral_api(viewsets.ModelViewSet):
    queryset = PropertyCollateral.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SFLP_PropertyCollateralDetailSerializer
        elif self.action == 'list':
            return SFLP_PropertyCollateralSerializer
        return SFLP_PropertyCollateralDetailSerializer


class sflp_enforcement_api(viewsets.ModelViewSet):
    queryset = Enforcement.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SFLP_EnforcementDetailSerializer
        elif self.action == 'list':
            return SFLP_EnforcementSerializer
        return SFLP_EnforcementDetailSerializer


class sflp_forbearance_api(viewsets.ModelViewSet):
    queryset = Forbearance.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SFLP_ForbearanceDetailSerializer
        elif self.action == 'list':
            return SFLP_ForbearanceSerializer
        return SFLP_ForbearanceDetailSerializer
