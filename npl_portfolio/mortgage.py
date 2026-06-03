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

from npl_portfolio.eba_field_helpers import mandatory_help, recommended_help, legacy_help, deprecated_help
from npl_portfolio.loan import Loan


class Mortgage(models.Model):
    """
    The Mortgage model holds Mortgage Guarantee data conforming to the EBA NPL Template specification (Template 4.2)
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Template>`_

    Ref: Commission Implementing Regulation (EU) 2023/2083, Annex I (Template 4.2) + Annex II (Data Glossary).
    """

    #
    # IDENTIFICATION FIELDS
    #

    mortgage_identifier = models.TextField(
        blank=True, null=True,
        help_text=mandatory_help('4.43', "Institution's internal identifier of the mortgage agreement.")
    )

    protection_identifier = models.ForeignKey(
        'PropertyCollateral', on_delete=models.CASCADE, blank=True, null=True,
        help_text=mandatory_help('4.00', "Institution's internal identifier to uniquely identify each protection (collateral or guarantee) used to secure the loan.")
    )

    #
    # FOREIGN KEYS
    #

    loan_identifier = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True,
                                        help_text=mandatory_help('2.01', "Institution's internal identifier of the loan secured by this mortgage."))

    #
    # DATA PROPERTIES
    #

    mortgage_amount = models.FloatField(
        blank=True, null=True,
        help_text=mandatory_help('4.44', "Maximum amount (including fees, expenses and liens) the institution is entitled to receive in a foreclosure, as registered in the official deed register.")
    )

    lien_position = models.IntegerField(
        blank=True, null=True,
        help_text=mandatory_help('4.45', "Highest lien position held by the institution on the immovable property collateral. Applicable if a mortgage lien is recorded in the official deed records.")
    )

    higher_ranking_loan = models.FloatField(
        blank=True, null=True,
        help_text=mandatory_help('4.46', "Amount that higher-ranking creditors/first-position lien holders are entitled to receive before the institution in a foreclosure. Applicable if the institution does not hold the first mortgage lien.")
    )

    register_of_deeds_number = models.TextField(
        blank=True, null=True,
        help_text=recommended_help('4.47', "Registration number under which the institution's mortgage lien is recorded in the official deed records. Applicable if the institution has a mortgage lien on the collateral.")
    )

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.mortgage_identifier)

    def get_absolute_url(self):
        return reverse('npl_portfolio:mortgage_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Mortgage"
        verbose_name_plural = "Mortgages"
