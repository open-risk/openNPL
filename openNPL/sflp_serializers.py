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

from rest_framework import serializers

from openNPL.settings import ROOT_VIEW
from sflp_portfolio.models.counterparty import Counterparty
from sflp_portfolio.models.loan import Loan
from sflp_portfolio.models.enforcement import Enforcement
from sflp_portfolio.models.forbearance import Forbearance
from sflp_portfolio.models.property_collateral import PropertyCollateral


#
#  SFLP_TEMPLATE ENDPOINTS
#


class SFLP_ForbearanceSerializer(serializers.ModelSerializer):
    """
    Serialize SFLP_Forbearance Data (List)
    """
    link = serializers.SerializerMethodField()

    class Meta:
        model = Forbearance
        fields = ('id', 'link')

    def get_link(self, obj):
        link = ROOT_VIEW + "/api/SFLP_data/forbearance/" + str(obj.pk)
        return link


class SFLP_ForbearanceDetailSerializer(serializers.ModelSerializer):
    """
    Serialize SFLP_Forbearance Data (Detail)
    """

    class Meta:
        model = Forbearance
        fields = '__all__'


class SFLP_EnforcementSerializer(serializers.ModelSerializer):
    """
    Serialize SFLP_Enforcement Data (List)
    """
    link = serializers.SerializerMethodField()

    class Meta:
        model = Enforcement
        fields = ('id', 'link')

    def get_link(self, obj):
        link = ROOT_VIEW + "/api/SFLP_data/enforcement/" + str(obj.pk)
        return link


class SFLP_EnforcementDetailSerializer(serializers.ModelSerializer):
    """
    Serialize SFLP_Enforcement Data (Detail)
    """

    class Meta:
        model = Enforcement
        fields = '__all__'


class SFLP_CounterpartySerializer(serializers.ModelSerializer):
    """
    Serialize SFLP_Counterparty Data
    """
    link = serializers.SerializerMethodField()

    class Meta:
        model = Counterparty
        fields = ('id', 'counterparty_identifier', 'link')

    def get_link(self, obj):
        link = ROOT_VIEW + "/api/SFLP_data/counterparties/" + str(obj.pk)
        return link


class SFLP_CounterpartyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counterparty
        fields = '__all__'


class SFLP_LoanSerializer(serializers.ModelSerializer):
    """
    Serialize SFLP_Loan Data
    """
    link = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = ('id', 'contract_identifier', 'link')

    def get_link(self, obj):
        link = ROOT_VIEW + "/api/SFLP_data/loans/" + str(obj.pk)
        return link


class SFLP_LoanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'


class SFLP_PropertyCollateralSerializer(serializers.ModelSerializer):
    """
    Serialize SFLP_Property Collateral Data
    """
    link = serializers.SerializerMethodField()

    class Meta:
        model = PropertyCollateral
        fields = ('id', 'protection_identifier', 'link')

    def get_link(self, obj):
        link = ROOT_VIEW + "/api/SFLP_data/property_collateral/" + str(obj.pk)
        return link


class SFLP_PropertyCollateralDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyCollateral
        fields = '__all__'
