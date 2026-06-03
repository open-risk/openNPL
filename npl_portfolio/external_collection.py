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

from npl_portfolio.counterparty import Counterparty
from npl_portfolio.eba_field_helpers import mandatory_help, legacy_help
from npl_portfolio.external_collection_choices import *
from npl_portfolio.loan import Loan


class ExternalCollection(models.Model):
    """
    The ExternalCollection model holds External Collection data conforming to the pre-2023 EBA NPL Template.

    .. note:: This model is Legacy — external collection data was folded into Template 5
              (Historical Repayments, fields 5.01–5.02) in the final EU 2023/2083 regulation.
    """

    #
    # IDENTIFICATION FIELDS
    #

    external_collection_identifier = models.TextField(blank=True, null=True)

    institutions_internal_identifier_for_the_loan_or_counterparty = models.TextField(blank=True, null=True,
                                                                                     help_text=legacy_help('Institution internal identifier for the counterparty or the loan.'))

    instrument_identifier = models.TextField(blank=True, null=True,
                                             help_text=legacy_help('Institution internal identifier for the loan part (sub-instrument level).'))

    type_of_identifier = models.IntegerField(blank=True, null=True, choices=TYPE_OF_IDENTIFIER_CHOICES,
                                             help_text=legacy_help('Indicator as to whether the external collections have been prepared on a counterparty level or on a loan level.'))

    #
    # FOREIGN KEYS (Template 2 — Relationship)
    #

    loan_identifier = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True,
                                        help_text=mandatory_help('2.01', "Institution's internal identifier of the loan to which this external collection applies."))

    counterparty_identifier = models.ForeignKey(Counterparty, on_delete=models.CASCADE, null=True, blank=True,
                                                help_text=mandatory_help('2.00', "Institution's internal identifier of the counterparty linked to this external collection."))

    #
    # LEGACY DATA PROPERTIES (pre-2023 EBA draft — not in EU 2023/2083)
    #

    balance_amount_sent_to_agent = models.FloatField(blank=True, null=True,
                                                     help_text=legacy_help('The balance that was sent to the external debt collection agent.'))

    cash_recoveries = models.FloatField(blank=True, null=True,
                                        help_text=legacy_help('Total cash recoveries collected by the external collection agent.'))

    costs_accrued = models.FloatField(blank=True, null=True,
                                      help_text=legacy_help('Total amount of costs accrued for external collection at Cut-Off Date.'))

    date_returned_from_agent = models.DateField(blank=True, null=True,
                                                help_text=legacy_help('Date that the loan was received back from the external collection agent (when the agent stopped recovery efforts).'))

    date_sent_to_agent = models.DateField(blank=True, null=True,
                                          help_text=legacy_help('Date that the loan was sent to the external collection agent.'))

    legal_entity_identifier = models.TextField(blank=True, null=True,
                                               help_text=legacy_help('Global standard 20-character LEI of the external collection agent.'))

    name_of_external_debt_collection_agent = models.TextField(blank=True, null=True,
                                                              help_text=legacy_help('Name of the external collection agent.'))

    debt_forgiveness = models.FloatField(blank=True, null=True,
                                              help_text=legacy_help('Amount of principal forgiven by the external collection agent as part of recovery negotiations.'))

    quantity_returned_from_agent = models.FloatField(blank=True, null=True,
                                                     help_text=legacy_help('Number of times the loan was received back from the external debt collection agent.'))

    registration_number = models.TextField(blank=True, null=True,
                                           help_text=legacy_help('Company registration number of the external collection agent per the country-specific registration office.'))

    repayment_plan = models.BooleanField(blank=True, null=True,
                                         help_text=legacy_help('Indicator as to whether a repayment plan has been agreed with the external collection agency.'))

    repayment_plan_description = models.TextField(blank=True, null=True,
                                                  help_text=legacy_help('Description of the repayment plan agreed with the external collection agency.'))

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.external_collection_identifier

    def get_absolute_url(self):
        return reverse('npl_portfolio:external_collection_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "External Collection"
        verbose_name_plural = "External Collections"
