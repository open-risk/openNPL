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
from npl_portfolio.eba_field_helpers import mandatory_help, recommended_help, legacy_help
from npl_portfolio.forbearance_choices import *
from npl_portfolio.loan import Loan


class Forbearance(models.Model):
    """
    The Forbearance model holds Forbearance data conforming to the EBA NPL Template specification
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Forbearance_Table>`_

    .. note:: Forbearance can be either the Counterparty of Loan level. At present only Loan Level is implemented

    """

    #
    # IDENTIFICATION FIELDS
    #

    forbearance_identifier = models.TextField(blank=True, null=True)

    #
    # FOREIGN KEYS (Template 2 — Relationship)
    #

    loan_identifier = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True,
                                        help_text=mandatory_help('2.01', "Institution's internal identifier of the loan to which this forbearance applies."))

    counterparty_identifier = models.ForeignKey(Counterparty, on_delete=models.CASCADE, null=True, blank=True,
                                                help_text=mandatory_help('2.00', "Institution's internal identifier of the counterparty linked to this forbearance."))

    #
    # EBA ITS 2023/2083 — MANDATORY FIELDS (Template 3)
    #

    type_of_forbearance = models.IntegerField(
        blank=True, null=True, choices=TYPE_OF_FORBEARANCE_CHOICES,
        help_text=mandatory_help(
            '3.39',
            "Types of forbearance per paragraphs 357–358 of Part 2 of Annex V to Reg. (EU) 2021/451. Applicable when 'yes' is selected in 'Forbearance measure'. Multiple choices permitted."
        )
    )

    end_date_of_forbearance = models.DateField(
        blank=True, null=True,
        help_text=mandatory_help(
            '3.40',
            "Date the current forbearance measure ends. In case of multiple forbearance measures, the most recent end date is used. Applicable when 'yes' is selected in 'Forbearance measure'."
        )
    )

    #
    # EBA ITS 2023/2083 — RECOMMENDED FIELDS (Template 3)
    #

    description_of_forbearance = models.TextField(
        blank=True, null=True,
        help_text=recommended_help(
            '3.41',
            "Further comments/details on the forbearance measures, including any clause to stop forbearance and multiple forbearance measures applied. Applicable when 'yes' is selected in 'Forbearance measure'."
        )
    )

    principal_forgiveness = models.FloatField(
        blank=True, null=True,
        help_text=recommended_help(
            '3.42',
            "Gross carrying amount of the loan partially forgiven as part of current forbearance measure, including principal forgiveness agreed by external collection agencies. Applicable when category (e) debt forgiveness is selected in 'Type of Forbearance'."
        )
    )

    number_of_historical_forbearance = models.FloatField(
        blank=True, null=True,
        help_text=recommended_help(
            '3.43',
            "Number of forbearances that happened in the last two years. Applicable when 'yes' is selected in 'Forbearance measure'."
        )
    )

    #
    # LEGACY DATA PROPERTIES (pre-2023 EBA draft — not in EU 2023/2083)
    #

    type_of_identifier = models.IntegerField(blank=True, null=True, choices=TYPE_OF_IDENTIFIER_CHOICES,
                                             help_text=legacy_help('Indicator as to whether forbearance has been prepared on a Counterparty level or a Loan level.'))

    institutions_internal_identifier_for_the_loan_or_counterparty = models.TextField(blank=True, null=True,
                                                                                     help_text=legacy_help('Institution internal identifier for the Counterparty or the Loan.'))

    instrument_identifier = models.TextField(blank=True, null=True,
                                             help_text=legacy_help('Institution internal identifier for the Loan part (sub-instrument level).'))

    amount_of_repayment_step_up = models.FloatField(blank=True, null=True,
                                                    help_text=legacy_help('Additional amount that the current agreed forbearance amount is increased by.'))

    clause_to_stop_forbearance = models.BooleanField(blank=True, null=True,
                                                     help_text=legacy_help('Indicator as to whether a clause exists to allow the institution to stop the current forbearance.'))

    date_of_first_forbearance = models.DateField(blank=True, null=True,
                                                 help_text=legacy_help('Date that the first forbearance happened.'))

    date_of_principal_forgiveness = models.DateField(blank=True, null=True,
                                                     help_text=legacy_help('Date that the principal forgiveness happened.'))

    date_of_repayment_step_up = models.DateField(blank=True, null=True,
                                                 help_text=legacy_help('Date at which the current agreed forbearance amount is increased.'))

    description_of_the_forbearance_clause = models.TextField(blank=True, null=True,
                                                             help_text=legacy_help('Further comments / details on the clause if "Yes" is selected in "Clause to Stop Forbearance".'))

    interest_rate_under_forbearance = models.FloatField(blank=True, null=True,
                                                        help_text=legacy_help('Interest rate agreed between the institution and counterparty under the current forbearance terms.'))

    repayment_amount_under_forbearance = models.FloatField(blank=True, null=True,
                                                           help_text=legacy_help('Periodic repayment amount agreed under the current forbearance terms.'))

    repayment_frequency_under_forbearance = models.IntegerField(blank=True, null=True,
                                                                choices=REPAYMENT_FREQUENCY_UNDER_FORBEARANCE_CHOICES,
                                                                help_text=legacy_help('Frequency that the repayment under current forbearance terms is made.'))

    start_date_of_forbearance = models.DateField(blank=True, null=True,
                                                 help_text=legacy_help('Date that the current forbearance arrangement starts.'))

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.forbearance_identifier

    def get_absolute_url(self):
        return reverse('npl_portfolio:forbearance_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Forbearance"
        verbose_name_plural = "Forbearances"
