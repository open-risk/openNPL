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

from django.db import models
from django.urls import reverse

from sflp_portfolio.models.model_choices import *
from sflp_portfolio.models.models import PortfolioSnapshot, Portfolio


class Loan(models.Model):
    """
    The Loan model holds Loan Portfolio data


    """

    #
    # IDENTIFICATION FIELDS
    #

    loan_identifier = models.TextField(blank=True, null=True,
                                       help_text='A unique identifier for the mortgage loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Loan_Identifier">Documentation</a>')
    "A unique identifier for the mortgage loan"

    #
    # FOREIGN KEYS
    #

    # Portfolio ID Foreign Key
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, blank=True, null=True,
                                     help_text="The portfolio ID to which the Loan belongs")

    # NOTE: Seller is captured in Portfolio name
    # seller_name = models.TextField(blank=True, null=True,
    #                                help_text='The name of the entity that delivered the mortgage loan to Fannie Mae.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    #
    # STATIC DATA PROPERTIES
    #

    channel = models.IntegerField(blank=True, null=True, choices=CHANNEL_CHOICES,
                                  help_text='The origination channel used by the party that delivered the loan to the issuer.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')



    original_interest_rate = models.FloatField(blank=True, null=True,
                                               help_text='The original interest rate on a mortgage loan as identified in the original mortgage note.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_loan_term = models.FloatField(blank=True, null=True,
                                           help_text='For fixed-rate, adjustable-rate and Interest-only mortgages, the number of months in which regularly scheduled borrower payments are due at the time the loan was originated.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_upb = models.FloatField(blank=True, null=True,
                                     help_text='The dollar amount of the loan as stated on the note at the time the loan was originated.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    origination_date = models.DateField(blank=True, null=True,
                                        help_text='The date of each individual note.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    first_payment_date = models.DateField(blank=True, null=True,
                                          help_text='The date of the first scheduled mortgage loan payment to be made by the borrower under the terms of the mortgage loan documents.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_loan_to_value_ratio = models.FloatField(blank=True, null=True,
                                                     help_text='The ratio, expressed as a percentage, obtained by dividing the amount of the loan at origination by the value of the property.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_combined_loan_to_value_ratio = models.FloatField(blank=True, null=True,
                                                              help_text='The ratio, expressed as a percentage, obtained by dividing the amount of all known outstanding loans at origination by the value of the property.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    loan_purpose = models.IntegerField(blank=True, null=True, choices=LOAN_PURPOSE_CHOICES,
                                       help_text='An indicator that denotes whether the mortgage loan is either a refinance mortgage or a purchase money mortgage. Purpose may be the purchase of a new property or refinance of an existing lien (with cash out or with no cash out).<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    mortgage_insurance_percentage = models.FloatField(blank=True, null=True,
                                                      help_text='The original percentage of mortgage insurance coverage obtained for an insured conventional mortgage loan and used following the occurrence of an event of default to calculate the insurance benefit, as defined by the underlying master primary insurance policy.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    mortgage_insurance_type = models.IntegerField(blank=True, null=True, choices=MORTGAGE_INSURANCE_TYPE_CHOICES,
                                                  help_text='The entity that is responsible for the Mortgage Insurance premium payment. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    amortization_type = models.IntegerField(blank=True, null=True, choices=AMORTIZATION_TYPE_CHOICES,
                                            help_text='The classification of the loan as having either a fixed- or an adjustable-interest rate at the time the loan was originated.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    relocation_mortgage_indicator = models.BooleanField(blank=True, null=True,
                                                        help_text='An indicator that denotes whether or not the type of mortgage loan is a relocation mortgage loan, made to borrowers whose employers relocate their employees.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    high_balance_loan_indicator = models.BooleanField(blank=True, null=True,
                                                      help_text='An indicator that denotes if the original principal balance of a mortgage loan is greater than the general conforming loan limit and up to the high-cost area loan limit.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')



    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.loan_identifier

    def get_absolute_url(self):
        return reverse('sflp_portfolio:loan_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
