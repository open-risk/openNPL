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

from npl_portfolio.models import CounterpartyGroup, Counterparty, Loan, \
    Enforcement, Forbearance, NonPropertyCollateral, PropertyCollateral, \
    ExternalCollection, HistoricalRepayment, Mortgage
from openNPL.npl_serializers import NPL_CounterpartyGroupSerializer, NPL_CounterpartyGroupDetailSerializer
from openNPL.npl_serializers import NPL_CounterpartySerializer, NPL_CounterpartyDetailSerializer
from openNPL.npl_serializers import NPL_EnforcementSerializer, NPL_EnforcementDetailSerializer
from openNPL.npl_serializers import NPL_ExternalCollectionSerializer, NPL_ExternalCollectionDetailSerializer
from openNPL.npl_serializers import NPL_ForbearanceSerializer, NPL_ForbearanceDetailSerializer
from openNPL.npl_serializers import NPL_LoanSerializer, NPL_LoanDetailSerializer
from openNPL.npl_serializers import NPL_NonPropertyCollateralSerializer, NPL_NonPropertyCollateralDetailSerializer
from openNPL.npl_serializers import NPL_PropertyCollateralSerializer, NPL_PropertyCollateralDetailSerializer
from openNPL.npl_serializers import NPL_HistoricalRepaymentSerializer, NPL_HistoricalRepaymentDetailSerializer
from openNPL.npl_serializers import NPL_MortgageSerializer, NPL_MortgageDetailSerializer


class npl_counterparty_api(viewsets.ModelViewSet):
    queryset = Counterparty.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NPL_CounterpartyDetailSerializer
        elif self.action == 'list':
            return NPL_CounterpartySerializer
        return NPL_CounterpartyDetailSerializer


class npl_counterpartygroup_api(viewsets.ModelViewSet):
    queryset = CounterpartyGroup.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NPL_CounterpartyGroupDetailSerializer
        elif self.action == 'list':
            return NPL_CounterpartyGroupSerializer
        return NPL_CounterpartyGroupDetailSerializer


class npl_loan_api(viewsets.ModelViewSet):
    queryset = Loan.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NPL_LoanDetailSerializer
        elif self.action == 'list':
            return NPL_LoanSerializer
        return NPL_LoanDetailSerializer


class npl_property_collateral_api(viewsets.ModelViewSet):
    queryset = PropertyCollateral.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NPL_PropertyCollateralDetailSerializer
        elif self.action == 'list':
            return NPL_PropertyCollateralSerializer
        return NPL_PropertyCollateralDetailSerializer


class npl_enforcement_api(viewsets.ModelViewSet):
    queryset = Enforcement.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NPL_EnforcementDetailSerializer
        elif self.action == 'list':
            return NPL_EnforcementSerializer
        return NPL_EnforcementDetailSerializer


class npl_forbearance_api(viewsets.ModelViewSet):
    queryset = Forbearance.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NPL_ForbearanceDetailSerializer
        elif self.action == 'list':
            return NPL_ForbearanceSerializer
        return NPL_ForbearanceDetailSerializer


class npl_nonproperty_collateral_api(viewsets.ModelViewSet):
    queryset = NonPropertyCollateral.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NPL_NonPropertyCollateralDetailSerializer
        elif self.action == 'list':
            return NPL_NonPropertyCollateralSerializer
        return NPL_NonPropertyCollateralDetailSerializer


class npl_external_collection_api(viewsets.ModelViewSet):
    queryset = ExternalCollection.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NPL_ExternalCollectionDetailSerializer
        elif self.action == 'list':
            return NPL_ExternalCollectionSerializer
        return NPL_ExternalCollectionDetailSerializer


class npl_historical_repayment_api(viewsets.ModelViewSet):
    queryset = HistoricalRepayment.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NPL_HistoricalRepaymentDetailSerializer
        elif self.action == 'list':
            return NPL_HistoricalRepaymentSerializer
        return NPL_HistoricalRepaymentDetailSerializer


class npl_mortgage_api(viewsets.ModelViewSet):
    queryset = Mortgage.objects.all().order_by('pk')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NPL_MortgageDetailSerializer
        elif self.action == 'list':
            return NPL_MortgageSerializer
        return NPL_MortgageDetailSerializer

