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


from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse

from npl_portfolio.models import CounterpartyGroup, Counterparty, Loan, \
    Enforcement, Forbearance, NonPropertyCollateral, PropertyCollateral, \
    ExternalCollection
from openNPL.serializers import NPL_CounterpartyGroupSerializer, NPL_CounterpartyGroupDetailSerializer
from openNPL.serializers import NPL_CounterpartySerializer, NPL_CounterpartyDetailSerializer
from openNPL.serializers import NPL_EnforcementSerializer, NPL_EnforcementDetailSerializer
from openNPL.serializers import NPL_ExternalCollectionSerializer, NPL_ExternalCollectionDetailSerializer
from openNPL.serializers import NPL_ForbearanceSerializer, NPL_ForbearanceDetailSerializer
from openNPL.serializers import NPL_LoanSerializer, NPL_LoanDetailSerializer
from openNPL.serializers import NPL_NonPropertyCollateralSerializer, NPL_NonPropertyCollateralDetailSerializer
from openNPL.serializers import NPL_PropertyCollateralSerializer, NPL_PropertyCollateralDetailSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    """
    Returns a list of all active API endpoints in the OpenNPL installation, grouped by functionality:

    - **NPL Data Endpoints** implements a REST CRUD interface to EBA Templated NPL Data


    """

    data = [
        {'NPL Template Endpoints':
            [
                {'npl_counterparty_group': reverse('npl_portfolio:npl_counterparty_group_api', request=request,
                                                   format=format)},
                {'npl_counterparty': reverse('npl_portfolio:npl_counterparty_api', request=request, format=format)},
                {'npl_loan': reverse('npl_portfolio:npl_loan_api', request=request, format=format)},
                {'npl_enforcement': reverse('npl_portfolio:npl_enforcement_api', request=request, format=format)},
                {'npl_forbearance': reverse('npl_portfolio:npl_forbearance_api', request=request, format=format)},
                {'npl_nonproperty_collateral': reverse('npl_portfolio:npl_nonproperty_collateral_api', request=request,
                                                       format=format)},
                {'npl_property_collateral': reverse('npl_portfolio:npl_property_collateral_api', request=request,
                                                    format=format)},
                {'npl_external_collection': reverse('npl_portfolio:npl_external_collection_api', request=request,
                                                    format=format)},
            ]},
    ]

    return Response(data)


#
# API ENDPOINTS
#

@api_view(['GET'])
def npl_api_root(request, format=None):
    """
    Returns a list of all active API endpoints for EBA NPL Template Data

    """

    data = [
        {'EBA Template Endpoints':
            [
                {'npl_counterparty_group': reverse('npl_counterparty_group_api', request=request, format=format)},
                {'npl_counterparty': reverse('npl_counterparty_api', request=request, format=format)},
                {'npl_loan': reverse('npl_loan_api', request=request, format=format)},
                {'npl_enforcement': reverse('npl_enforcement_api', request=request, format=format)},
                {'npl_forbearance': reverse('npl_forbearance_api', request=request, format=format)},
                {'npl_nonproperty_collateral': reverse('npl_nonproperty_collateral_api', request=request,
                                                       format=format)},
                {'npl_property_collateral': reverse('npl_property_collateral_api', request=request, format=format)},
                {'npl_external_collection': reverse('npl_external_collection_api', request=request, format=format)},
            ]}
    ]
    return Response(data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def npl_counterparty_api(request):
    """
    List Counterparties (EBA Template)
    """
    if request.method == 'GET':
        counterparty = Counterparty.objects.all()
        serializer = NPL_CounterpartySerializer(counterparty, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create a new Counterparty
        """
        data = JSONParser().parse(request)
        serializer = NPL_CounterpartyDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def npl_counterparty_detail(request, pk):
    if request.method == 'GET':
        """
        List the data a specific Counterparty
        """
        try:
            counterparty = Counterparty.objects.get(pk=pk)
        except Counterparty.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NPL_CounterpartyDetailSerializer(counterparty)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def npl_loan_api(request):
    """
    List Loans (EBA Template)
    """
    if request.method == 'GET':
        loan = Loan.objects.all()
        serializer = NPL_LoanSerializer(loan, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create a new Loan
        """
        data = JSONParser().parse(request)
        serializer = NPL_LoanDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def npl_loan_detail(request, pk):
    """
    List the data a specific EBA Loan
    """
    try:
        loan = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NPL_LoanDetailSerializer(loan)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def npl_property_collateral_api(request):
    """
    List Property Collateral (EBA Template)
    """
    if request.method == 'GET':
        property_collateral = PropertyCollateral.objects.all()
        serializer = NPL_PropertyCollateralSerializer(property_collateral, many=True,
                                                      context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create new property collateral
        """
        data = JSONParser().parse(request)
        serializer = NPL_PropertyCollateralDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def npl_property_collateral_detail(request, pk):
    """
    List the data a specific EBA Property Collateral
    """
    try:
        property_collateral = PropertyCollateral.objects.get(pk=pk)
    except PropertyCollateral.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NPL_PropertyCollateralDetailSerializer(property_collateral)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def npl_counterparty_group_api(request):
    """
    List Counterparty Groups (EBA Template)
    """
    if request.method == 'GET':
        counterparty_group = CounterpartyGroup.objects.all()
        serializer = NPL_CounterpartyGroupSerializer(counterparty_group, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create new counterparty group
        """
        data = JSONParser().parse(request)
        serializer = NPL_CounterpartyGroupDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def npl_counterparty_group_detail(request, pk):
    """
    List the data a specific EBA Counterparty Group
    """
    try:
        counterparty_group = CounterpartyGroup.objects.get(pk=pk)
    except CounterpartyGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NPL_CounterpartyGroupDetailSerializer(counterparty_group)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def npl_enforcement_api(request):
    """
    List Enforcements (EBA Template)
    """
    if request.method == 'GET':
        enforcement = Enforcement.objects.all()
        serializer = NPL_EnforcementSerializer(enforcement, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create new Enforcement entry
        """
        data = JSONParser().parse(request)
        serializer = NPL_EnforcementDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def npl_enforcement_detail(request, pk):
    """
    List the data a specific EBA Enforcement entry
    """
    try:
        enforcement = Enforcement.objects.get(pk=pk)
    except Enforcement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NPL_EnforcementDetailSerializer(enforcement)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def npl_forbearance_api(request):
    """
    List Forbearance (EBA Template)
    """
    if request.method == 'GET':
        forbearance = Forbearance.objects.all()
        serializer = NPL_ForbearanceSerializer(forbearance, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create new Forbearance entry
        """
        data = JSONParser().parse(request)
        serializer = NPL_ForbearanceDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def npl_forbearance_detail(request, pk):
    """
    List the data a specific EBA Forbearance entry
    """
    try:
        forbearance = Forbearance.objects.get(pk=pk)
    except Forbearance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NPL_ForbearanceDetailSerializer(forbearance)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def npl_nonproperty_collateral_api(request):
    """
    List NonProperty Collateral (EBA Template)
    """
    if request.method == 'GET':
        nonproperty_collateral = NonPropertyCollateral.objects.all()
        serializer = NPL_NonPropertyCollateralSerializer(nonproperty_collateral, many=True,
                                                         context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create new Non Property Collateral entry
        """
        data = JSONParser().parse(request)
        serializer = NPL_NonPropertyCollateralSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def npl_nonproperty_collateral_detail(request, pk):
    """
    List the data a specific EBA Non Property Collateral
    """
    try:
        nonproperty_collateral = NonPropertyCollateral.objects.get(pk=pk)
    except NonPropertyCollateral.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NPL_NonPropertyCollateralDetailSerializer(nonproperty_collateral)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def npl_external_collection_api(request):
    """
    List External Collections (EBA Template)
    """
    if request.method == 'GET':
        external_collection = ExternalCollection.objects.all()
        serializer = NPL_ExternalCollectionSerializer(external_collection, many=True,
                                                      context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        """
        Create a new External Collection data
        """
        data = JSONParser().parse(request)
        serializer = NPL_ExternalCollectionDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def npl_external_collection_detail(request, pk):
    if request.method == 'GET':
        """
        List the data of an external collection
        """
        try:
            external_collection = ExternalCollection.objects.get(pk=pk)
        except ExternalCollection.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NPL_ExternalCollectionSerializer(external_collection)
        return Response(serializer.data)
