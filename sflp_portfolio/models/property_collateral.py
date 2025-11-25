# Copyright (c) 2020 - 2025 Open Risk (https://www.openriskmanagement.com)
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

from django.db import models
from django.urls import reverse

from sflp_portfolio.models.loan import Loan
from sflp_portfolio.models.model_choices import *


class PropertyCollateral(models.Model):
    """
    The PropertyCollateral model object holds static Real Estate Property Collateral data. There is no unique collateral ID, it links to the related Loan ID.


    """

    #
    # IDENTIFICATION FIELDS
    #

    #
    # FOREIGN KEYS
    #

    loan_identifier = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True,
                                        help_text='The loan ID to which the property collateral links.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Loan_Identifier">Documentation</a>')
    """The loan ID to which the property collateral links."""

    #
    # STATIC DATA PROPERTIES
    #
    metropolitan_statistical_area = models.TextField(blank=True, null=True,
                                                     help_text='The numeric Metropolitan Statistical Area Code for the property securing the mortgage loan. MSAs are established by the US Office of Management and Budget. An area usually qualifies as an MSA if it is defined by the Bureau of the Census as an urbanized area and has a population of 50,000 or more in a total metropolitan area of at least 100,000. An MSA may consist of one or more counties.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Metropolitan_Statistical_Area">Documentation</a>')
    """"""

    number_of_units = models.FloatField(blank=True, null=True,
                                        help_text='The number of units comprising the related mortgaged property (one, two, three, or four).<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Number_of_Units">Documentation</a>')
    """"""

    occupancy_status = models.IntegerField(blank=True, null=True, choices=OCCUPANCY_STATUS_CHOICES,
                                           help_text='The classification describing the property occupancy status at the time the loan was originated.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Occupancy_Status">Documentation</a>')
    """"""

    property_state = models.TextField(blank=True, null=True,
                                      help_text='A two-letter abbreviation indicating the state or territory within which the property securing the mortgage loan is located.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Property_State">Documentation</a>')
    """"""

    property_type = models.IntegerField(blank=True, null=True, choices=PROPERTY_TYPE_CHOICES,
                                        help_text='An indicator that denotes whether the property type secured by the mortgage loan is a condominium, co-operative, planned urban development (PUD), manufactured home, or single-family home.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Property_Type">Documentation</a>')
    """"""

    zip_code_short = models.TextField(blank=True, null=True,
                                      help_text='Limited to the first three digits of the code designated by the U.S. Postal Service where the subject property is located.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Zip_Code_Short">Documentation</a>')
    """"""

    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    """The first insertion date of the data point"""

    last_change_date = models.DateTimeField(auto_now=True)
    """The last change date of the data point"""

    def __str__(self):
        """String representing the data object"""
        return "Collateral of Loan " + str(self.loan_identifier)

    def get_absolute_url(self):
        """Absolute URL where the data point can be edited"""
        return reverse('sflp_portfolio:property_collateral_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Property Collateral"
        verbose_name_plural = "Property Collateral"
