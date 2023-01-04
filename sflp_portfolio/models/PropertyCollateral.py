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

from django.db import models
from django.urls import reverse

from sflp_portfolio.models.Loan import Loan
from sflp_portfolio.models.model_choices import *


class PropertyCollateral(models.Model):
    """
    The PropertyCollateral model object holds Property Collateral data

    .. note:: The Agency Single Family Loan Performance Template does not explicitly segment data attributes into Counterparty, Loan etc. The assignment into tables (models) in openNPL is based on the interpretation and main function of different data fields

    """

    #
    # IDENTIFICATION FIELDS
    #

    #
    # FOREIGN KEYS
    #

    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True)

    #
    # DATA PROPERTIES
    #

    associated_taxes_for_holding_property = models.FloatField(blank=True, null=True,
                                                              help_text='Payment of taxes associated with holding the property.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    metropolitan_statistical_area = models.TextField(blank=True, null=True,
                                                     help_text='The numeric Metropolitan Statistical Area Code for the property securing the mortgage loan. MSAs are established by the US Office of Management and Budget. An area usually qualifies as an MSA if it is defined by the Bureau of the Census as an urbanized area and has a population of 50,000 or more in a total metropolitan area of at least 100,000. An MSA may consist of one or more counties.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    miscellaneous_holding_expenses_and_credits = models.FloatField(blank=True, null=True,
                                                                   help_text='Expenses and credits associated with preserving the property, including Homeowners Association and other dues; flood, hazard, and MI premiums and refunds; rental income; and title insurance costs.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    number_of_units = models.FloatField(blank=True, null=True,
                                        help_text='The number of units comprising the related mortgaged property (one, two, three, or four).<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    occupancy_status = models.IntegerField(blank=True, null=True, choices=OCCUPANCY_STATUS_CHOICES,
                                           help_text='The classification describing the property occupancy status at the time the loan was originated.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    property_preservation_and_repair_costs = models.FloatField(blank=True, null=True,
                                                               help_text='The expenses associated with securing and preserving the property including two major categories:  maintenance and repairs. Maintenance costs are associated with preserving the property through normal upkeep, while repairs are associated with either avoiding deterioration of the asset or a marketing decision to help maximize sales proceeds upon final disposition.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    property_state = models.TextField(blank=True, null=True,
                                      help_text='A two-letter abbreviation indicating the state or territory within which the property securing the mortgage loan is located.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    property_type = models.IntegerField(blank=True, null=True, choices=PROPERTY_TYPE_CHOICES,
                                        help_text='An indicator that denotes whether the property type secured by the mortgage loan is a condominium, co-operative, planned urban development (PUD), manufactured home, or single-family home.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    property_valuation_method = models.IntegerField(blank=True, null=True, choices=PROPERTY_VALUATION_METHOD_CHOICES,
                                                    help_text='An indicator that denotes the method by which the value of the subject property was obtained. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    zip_code_short = models.TextField(blank=True, null=True,
                                      help_text='Limited to the first three digits of the code designated by the U.S. Postal Service where the subject property is located.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('sflp_portfolio:property_collateral_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Property Collateral"
        verbose_name_plural = "Property Collateral"
