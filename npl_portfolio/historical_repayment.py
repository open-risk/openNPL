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

from npl_portfolio.eba_field_helpers import mandatory_help, recommended_help
from npl_portfolio.historical_repayment_choices import *
from npl_portfolio.loan import Loan
from npl_portfolio.models import PortfolioSnapshot, Portfolio


class HistoricalRepayment(models.Model):
    """
    The HistoricalRepayment model holds Historical Collection of Repayments data conforming to the
    EBA NPL Template specification (Template 5)
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Template>`_

    Ref: Commission Implementing Regulation (EU) 2023/2083, Annex I (Template 5) + Annex II (Data Glossary).

    .. note:: EBA Template 5 presents the repayment history as a monthly matrix (minimum 36 months
              before the NPL Portfolio Cut-Off Date, aggregated per month in separate columns). This
              model normalises that matrix to long format: one record per Loan per reference month.
              This follows the openNPL convention for schedule / history tables (cfr. github issue 21).

    """

    #
    # IDENTIFICATION FIELDS
    #
    # EBA NPL ITS 5.00 — Loan Identifier is modelled as the loan_identifier foreign key below.

    #
    # FOREIGN KEYS
    #

    # EBA NPL ITS 5.00 — Loan Identifier
    loan_identifier = models.ForeignKey(
        Loan, on_delete=models.CASCADE, null=True, blank=True,
        help_text=mandatory_help(
            '5.00',
            "Institution internal identifier of the loan. Join key with the Loan table (Template 3)."
        )
    )

    # Portfolio ID Foreign Key
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE, blank=True, null=True,
                                     help_text="The portfolio ID to which the Historical Repayment belongs")

    # Snapshot ID Foreign Key
    snapshot_id = models.ForeignKey(PortfolioSnapshot, on_delete=models.CASCADE, blank=True, null=True,
                                    help_text="The snapshot ID to which the Historical Repayment belongs")

    #
    # EBA DATA PROPERTIES
    #

    reference_year = models.IntegerField(blank=True, null=True,
                                         help_text='Year of the reference month for this repayment record (e.g. 2023).')

    reference_month = models.IntegerField(blank=True, null=True,
                                          help_text='Month of the reference month for this repayment record (1–12, e.g. 9 = September). EBA Template 5 requires a minimum of 36 months before the Cut-Off Date.')

    # EBA NPL ITS 5.01 — Type of Collection
    type_of_collection = models.IntegerField(
        blank=True, null=True, choices=TYPE_OF_COLLECTION_CHOICES,
        help_text=recommended_help(
            '5.01',
            "Indication whether the collection of repayments occurred internally or via external collection agencies."
        )
    )

    # EBA NPL ITS 5.02 — Name of External Collection Agent
    name_of_external_collection_agent = models.TextField(
        blank=True, null=True,
        help_text=recommended_help(
            '5.02',
            "Name of the external collection agent. Required only when Type of Collection (5.01) is External."
        )
    )

    # EBA NPL ITS 5.03 — History of Total Repayments
    # NOTE: EBA field type is 'Number', which per Annex III, Part 1, Section 3 (Conventions)
    # is to be expressed to two decimal places. We use BigIntegerField for consistency with
    # the rest of openNPL, where every monetary 'Number' field is modelled as an integer
    # amount (e.g. balance_at_default, origination_amount). Switch to
    # DecimalField(decimal_places=2) only if strict EBA decimal precision is required.
    history_of_total_repayments = models.BigIntegerField(
        blank=True, null=True,
        help_text=mandatory_help(
            '5.03',
            "Total repayment amount received by the institution in the reference month, irrespective of the source of repayment (including collections by external collection agencies). Aggregated per month for a minimum of 36 months before the cut-off date."
        )
    )

    # EBA NPL ITS 5.04 — History of Repayments - From Collateral Sales
    # NOTE: EBA field type is 'Number' (two decimal places per Annex III conventions).
    # Modelled as BigIntegerField for consistency with the openNPL monetary field convention;
    # use DecimalField(decimal_places=2) if strict EBA decimal precision is required.
    history_of_repayments_from_collateral_sales = models.BigIntegerField(
        blank=True, null=True,
        help_text=recommended_help(
            '5.04',
            "Repayment amount derived from collateral disposal in the reference month. Applicable to secured loans. Aggregated per month for a minimum of 36 months before the cut-off date."
        )
    )

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s / %s-%02d' % (self.loan_identifier, self.reference_year, self.reference_month or 0)

    def get_absolute_url(self):
        return reverse('npl_portfolio:historical_repayment_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Historical Repayment"
        verbose_name_plural = "Historical Repayments"
        unique_together = [['snapshot_id', 'loan_identifier', 'reference_year', 'reference_month']]
