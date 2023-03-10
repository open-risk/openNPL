# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
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


from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse

from sflp_portfolio.models.models import Counterparty, CounterpartyState, Loan, \
    LoanState, Enforcement, Forbearance, PropertyCollateral, PropertyCollateralState

from openNPL.sflp_serializers import SFLP_CounterpartySerializer, SFLP_CounterpartyDetailSerializer
from openNPL.sflp_serializers import SFLP_EnforcementSerializer, SFLP_EnforcementDetailSerializer
from openNPL.sflp_serializers import SFLP_ForbearanceSerializer, SFLP_ForbearanceDetailSerializer
from openNPL.sflp_serializers import SFLP_LoanSerializer, SFLP_LoanDetailSerializer
from openNPL.sflp_serializers import SFLP_PropertyCollateralSerializer, SFLP_PropertyCollateralDetailSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    """
    Returns a list of all active API endpoints in the OpenNPL installation, grouped by functionality:

    - **NPL Data Endpoints** implements a REST CRUD interface to EBA Templated NPL Data


    """

    data = [
        {'SFPL Template Endpoints':
            [
                {'sflp_counterparty': reverse('sflp_portfolio:sflp_counterparty_api', request=request, format=format)},
                {'sflp_loan': reverse('sflp_portfolio:sflp_loan_api', request=request, format=format)},
                {'sflp_enforcement': reverse('sflp_portfolio:sflp_enforcement_api', request=request, format=format)},
                {'sflp_forbearance': reverse('sflp_portfolio:sflp_forbearance_api', request=request, format=format)},
                {'sflp_property_collateral': reverse('sflp_portfolio:sflp_property_collateral_api', request=request,
                                                     format=format)},
                {'sflp_repayment_schedule': reverse('sflp_portfolio:sflp_repayment_schedule_api', request=request,
                                                    format=format)},
            ]},
    ]

    return Response(data)


#
# API ENDPOINTS
#

@api_view(['GET'])
def sflp_api_root(request, format=None):
    """
    Returns a list of all active API endpoints for EBA NPL Template Data

    """

    data = [
        {'EBA Template Endpoints':
            [
                {'sflp_counterparty': reverse('sflp_counterparty_api', request=request, format=format)},
                {'sflp_loan': reverse('sflp_loan_api', request=request, format=format)},
                {'sflp_enforcement': reverse('sflp_enforcement_api', request=request, format=format)},
                {'sflp_forbearance': reverse('sflp_forbearance_api', request=request, format=format)},
                {'sflp_property_collateral': reverse('sflp_property_collateral_api', request=request, format=format)},
                {'sflp_repayment_schedule': reverse('sflp_repayment_schedule_api', request=request, format=format)},
            ]}
    ]
    return Response(data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def sflp_counterparty_api(request):
    """
    List Counterparties (EBA Template)
    """
    if request.method == 'GET':
        counterparty = Counterparty.objects.all()
        serializer = SFLP_CounterpartySerializer(counterparty, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create a new Counterparty
        """
        data = JSONParser().parse(request)
        serializer = SFLP_CounterpartyDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sflp_counterparty_detail(request, pk):
    if request.method == 'GET':
        """
        List the data a specific Counterparty
        """
        try:
            counterparty = Counterparty.objects.get(pk=pk)
        except Counterparty.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SFLP_CounterpartyDetailSerializer(counterparty)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def sflp_loan_api(request):
    """
    List Loans (EBA Template)
    """
    if request.method == 'GET':
        loan = Loan.objects.all()
        serializer = SFLP_LoanSerializer(loan, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create a new Loan
        """
        data = JSONParser().parse(request)
        serializer = SFLP_LoanDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sflp_loan_detail(request, pk):
    """
    List the data a specific EBA Loan
    """
    try:
        loan = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SFLP_LoanDetailSerializer(loan)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def sflp_property_collateral_api(request):
    """
    List Property Collateral (EBA Template)
    """
    if request.method == 'GET':
        property_collateral = PropertyCollateral.objects.all()
        serializer = SFLP_PropertyCollateralSerializer(property_collateral, many=True,
                                                       context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create new property collateral
        """
        data = JSONParser().parse(request)
        serializer = SFLP_PropertyCollateralDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sflp_property_collateral_detail(request, pk):
    """
    List the data a specific EBA Property Collateral
    """
    try:
        property_collateral = PropertyCollateral.objects.get(pk=pk)
    except PropertyCollateral.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SFLP_PropertyCollateralDetailSerializer(property_collateral)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def sflp_enforcement_api(request):
    """
    List Enforcements (EBA Template)
    """
    if request.method == 'GET':
        enforcement = Enforcement.objects.all()
        serializer = SFLP_EnforcementSerializer(enforcement, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create new Enforcement entry
        """
        data = JSONParser().parse(request)
        serializer = SFLP_EnforcementDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sflp_enforcement_detail(request, pk):
    """
    List the data a specific EBA Enforcement entry
    """
    try:
        enforcement = Enforcement.objects.get(pk=pk)
    except Enforcement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SFLP_EnforcementDetailSerializer(enforcement)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def sflp_forbearance_api(request):
    """
    List Forbearance (EBA Template)
    """
    if request.method == 'GET':
        forbearance = Forbearance.objects.all()
        serializer = SFLP_ForbearanceSerializer(forbearance, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create new Forbearance entry
        """
        data = JSONParser().parse(request)
        serializer = SFLP_ForbearanceDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sflp_forbearance_detail(request, pk):
    """
    List the data a specific EBA Forbearance entry
    """
    try:
        forbearance = Forbearance.objects.get(pk=pk)
    except Forbearance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SFLP_ForbearanceDetailSerializer(forbearance)
    return Response(serializer.data)


