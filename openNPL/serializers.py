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

# TODO Lease (non-SME)
from npl_portfolio.models import CounterpartyGroup, Counterparty, Loan, \
    Enforcement, Forbearance, NonPropertyCollateral, PropertyCollateral, \
    ExternalCollection
from rest_framework import serializers

from openNPL.settings import ROOT_VIEW


#
#  NPL TEMPLATE ENDPOINTS
#

class NPL_ExternalCollectionSerializer(serializers.ModelSerializer):
    """
    Serialize NPL ExternalCollection Data
    """

    class Meta:
        model = ExternalCollection
        fields = '__all__'


class NPL_NonPropertyCollateralSerializer(serializers.ModelSerializer):
    """
    Serialize NPL NonPropertyCollateral Data
    """

    class Meta:
        model = NonPropertyCollateral
        fields = '__all__'


class NPL_ForbearanceSerializer(serializers.ModelSerializer):
    """
    Serialize NPL Forbearance Data
    """

    class Meta:
        model = Forbearance
        fields = '__all__'


class NPL_EnforcementSerializer(serializers.ModelSerializer):
    """
    Serialize NPL Enforcement Data
    """

    class Meta:
        model = Enforcement
        fields = '__all__'


class NPL_CounterpartyGroupSerializer(serializers.ModelSerializer):
    """
    Serialize NPL CounterpartyGroups Data
    """

    class Meta:
        model = CounterpartyGroup
        fields = '__all__'


class NPL_CounterpartySerializer(serializers.ModelSerializer):
    """
    Serialize NPL Counterparty Data
    """
    link = serializers.SerializerMethodField()

    class Meta:
        model = Counterparty
        fields = ('id', 'counterparty_identifier', 'link')

    def get_link(self, obj):
        link = ROOT_VIEW + "/api/npl_data/counterparties/" + str(obj.pk)
        return link


class NPL_CounterpartyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counterparty
        fields = '__all__'


class NPL_LoanSerializer(serializers.ModelSerializer):
    """
    Serialize NPL Loan Data
    """
    link = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = ('id', 'contract_identifier', 'link')

    def get_link(self, obj):
        link = ROOT_VIEW + "/api/npl_data/loans/" + str(obj.pk)
        return link


class NPL_LoanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'


class NPL_PropertyCollateralSerializer(serializers.ModelSerializer):
    """
    Serialize NPL Property Collateral Data
    """
    link = serializers.SerializerMethodField()

    class Meta:
        model = PropertyCollateral
        fields = ('id', 'protection_identifier', 'link')

    def get_link(self, obj):
        link = ROOT_VIEW + "/api/npl_data/property_collateral/" + str(obj.pk)
        return link


class NPL_PropertyCollateralDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyCollateral
        fields = '__all__'
