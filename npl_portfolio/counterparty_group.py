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

from django.db import models
from django.urls import reverse

from npl_portfolio.counterparty_group_choices import *
from npl_portfolio.eba_field_helpers import mandatory_help, legacy_help


class CounterpartyGroup(models.Model):
    """
    The CounterpartyGroup model holds Counterparty Group data conforming to the EBA NPL Template specification
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Counterparty_Group_Table>`_

    """

    #
    # IDENTIFICATION FIELDS
    #

    counterparty_group_identifier = models.TextField(blank=True, null=True,
                                                     help_text=mandatory_help('1.00', "Institution's internal identifier to uniquely identify each counterparty group. Each counterparty group should have one Counterparty Group Identifier."))

    #
    # EBA ITS 2023/2083 — MANDATORY FIELDS (Template 1)
    #

    name_of_counterparty_group = models.TextField(blank=True, null=True,
                                                  help_text=mandatory_help('1.01', "Name used to refer to the counterparty group."))

    #
    # LEGACY DATA PROPERTIES (pre-2023 EBA draft — not in EU 2023/2083)
    #

    cross_collateralisation_in_counterparty_group = models.IntegerField(blank=True, null=True,
                                                                        choices=CROSS_COLLATERALISATION_IN_COUNTERPARTY_GROUP_CHOICES,
                                                                        help_text=legacy_help('Indicator as to whether all/some of the loans in the Counterparty Group are secured by all/some of the collaterals within the Counterparty Group.'))

    cross_default_in_counterparty_group = models.IntegerField(blank=True, null=True,
                                                              choices=CROSS_DEFAULT_IN_COUNTERPARTY_GROUP_CHOICES,
                                                              help_text=legacy_help('Indicator as to whether contractual breach of any loans in the Counterparty Group would trigger the contractual default event of the other loans.'))

    description_of_cross_collateralisation = models.TextField(blank=True, null=True,
                                                              help_text=legacy_help('Description of cross collateralisation when "Partial" is selected in "Cross Collateralisation in Counterparty Group".'))

    description_of_cross_default = models.TextField(blank=True, null=True,
                                                    help_text=legacy_help('Description of cross default when "Partial" is selected in "Cross Default in Counterparty Group".'))

    description_of_sponsor = models.TextField(blank=True, null=True,
                                              help_text=legacy_help('Description and related narrative on the Sponsor.'))

    industry_segment_of_counterparty_group = models.TextField(blank=True, null=True,
                                                              help_text=legacy_help('Industry in which the Counterparty Group mainly operates.'))

    name_of_sponsor = models.TextField(blank=True, null=True,
                                       help_text=legacy_help('Name used to refer to the main decision maker / key individual in relation to the Counterparty Group.'))

    type_of_sponsor = models.IntegerField(blank=True, null=True, choices=TYPE_OF_SPONSOR_CHOICES,
                                          help_text=legacy_help('Type of entity the sponsor is (Listed Corporate, Unlisted Corporate, Listed Fund, Unlisted Fund, High Net Worth Individual).'))

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.counterparty_group_identifier

    def get_absolute_url(self):
        return reverse('npl_portfolio:CounterpartyGroup_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Counterparty Group"
        verbose_name_plural = "Counterparty Groups"
