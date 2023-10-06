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
from sflp_portfolio.models.models import Portfolio


class Loan(models.Model):
    """
    The Loan model holds Static (Acquistion) Loan data

    .. note:: For some fields the static nature might not be entirely respected if historical data overwrite values in the case of modifications


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
    """The portfolio ID to which the Loan belongs"""

    # NOTE: Seller is captured in Portfolio name
    # seller_name = models.TextField(blank=True, null=True,
    #                                help_text='The name of the entity that delivered the mortgage loan to Fannie Mae.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # STATIC DATA PROPERTIES
    #

    arm_balloon_indicator = models.BooleanField(blank=True, null=True,
                                                help_text='For an adjustable-rate mortgage loan, a code that denotes if the loan has a balloon feature.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    arm_cap_structure = models.TextField(blank=True, null=True,
                                         help_text='For an adjustable-rate mortgage loan, a numeric string that explains the interest rate caps on the ARM. The first number is the Initial Interest Rate Cap Up Percent (i.e., the maximum percentage points the interest rate can adjust upward at the initial rate change date). The second number is the Periodic Interest Rate Cap Up Percent (i.e., the maximum percentage points the interest rate can adjust upward at each interest rate change date after the initial interest rate change date). The third number is the Lifetime Interest Rate Cap Up Percent (i.e., the maximum percentage points that the interest rate can adjust upward over the life of the loan relative to the initial interest rate).<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    arm_initial_fixed_rate_period_less_than_5_yr = models.BooleanField(blank=True, null=True,
                                                                       help_text='For an adjustable-rate mortgage loan, an indicator that denotes if the Initial Fixed-Rate Period is less than or equal to five years.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    arm_plan_number = models.FloatField(blank=True, null=True,
                                        help_text='For an adjustable-rate mortgage loan, a code identifying the standardized plan under which the mortgage loan was delivered to Fannie Mae. The ARM plan outlines the characteristics of the adjustable-rate mortgage loan, including the ARM Index, the Initial Fixed-Rate Period, the Cap Structure, look-back days, assumability, and the option to convert to a fixed-rate mortgage loan..<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    arm_product_type = models.TextField(blank=True, null=True,
                                        help_text='For an adjustable-rate mortgage loan, a string that denotes the Initial Fixed-Rate Period, the subsequent Interest Rate Adjustment Frequency, and the Original Loan Term.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    channel = models.IntegerField(blank=True, null=True, choices=CHANNEL_CHOICES,
                                  help_text='The origination channel used by the party that delivered the loan to the issuer.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Channel">Documentation</a>')
    """The origination channel used by the party that delivered the loan to the issuer"""

    original_interest_rate = models.FloatField(blank=True, null=True,
                                               help_text='The original interest rate on a mortgage loan as identified in the original mortgage note.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Original_Interest_Rate">Documentation</a>')
    """The original interest rate on a mortgage loan as identified in the original mortgage note"""

    original_loan_term = models.FloatField(blank=True, null=True,
                                           help_text='For fixed-rate, adjustable-rate and Interest-only mortgages, the number of months in which regularly scheduled borrower payments are due at the time the loan was originated.<a class="risk_manual_url" href="FM SFLP.Original Loan Term">Documentation</a>')
    """The number of months in which regularly scheduled borrower payments are due."""

    original_upb = models.FloatField(blank=True, null=True,
                                     help_text='The dollar amount of the loan as stated on the note at the time the loan was originated.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Original_UPB">Documentation</a>')
    """The dollar amount of the loan as stated on the note at the time the loan was originated"""

    origination_date = models.DateField(blank=True, null=True,
                                        help_text='The date of each individual note.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Origination_Date">Documentation</a>')
    """The date of each individual note"""

    first_payment_date = models.DateField(blank=True, null=True,
                                          help_text='The date of the first scheduled mortgage loan payment to be made by the borrower under the terms of the mortgage loan documents.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.First_Payment_Date">Documentation</a>')
    """The date of the first scheduled mortgage loan payment to be made by the borrower under the terms of the mortgage loan documents"""

    original_loan_to_value_ratio = models.FloatField(blank=True, null=True,
                                                     help_text='The ratio, expressed as a percentage, obtained by dividing the amount of the loan at origination by the value of the property.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Original_Loan_to_Value_Ratio">Documentation</a>')
    """The ratio, expressed as a percentage, obtained by dividing the amount of the loan at origination by the value of the property"""

    original_combined_loan_to_value_ratio = models.FloatField(blank=True, null=True,
                                                              help_text='The ratio, expressed as a percentage, obtained by dividing the amount of all known outstanding loans at origination by the value of the property.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Original_Combined_Loan_to_Value_Ratio">Documentation</a>')
    """"""

    loan_purpose = models.IntegerField(blank=True, null=True, choices=LOAN_PURPOSE_CHOICES,
                                       help_text='An indicator that denotes whether the mortgage loan is either a refinance mortgage or a purchase money mortgage. Purpose may be the purchase of a new property or refinance of an existing lien (with cash out or with no cash out).<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Loan_Purpose">Documentation</a>')
    """"""

    mortgage_insurance_percentage = models.FloatField(blank=True, null=True,
                                                      help_text='The original percentage of mortgage insurance coverage obtained for an insured conventional mortgage loan and used following the occurrence of an event of default to calculate the insurance benefit, as defined by the underlying master primary insurance policy.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Mortgage_Insurance_Percentage">Documentation</a>')
    """"""

    mortgage_insurance_type = models.IntegerField(blank=True, null=True, choices=MORTGAGE_INSURANCE_TYPE_CHOICES,
                                                  help_text='The entity that is responsible for the Mortgage Insurance premium payment. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Mortgage_Insurance_Type">Documentation</a>')
    """"""

    amortization_type = models.IntegerField(blank=True, null=True, choices=AMORTIZATION_TYPE_CHOICES,
                                            help_text='The classification of the loan as having either a fixed- or an adjustable-interest rate at the time the loan was originated.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Amortization_Type">Documentation</a>')
    """"""

    relocation_mortgage_indicator = models.BooleanField(blank=True, null=True,
                                                        help_text='An indicator that denotes whether or not the type of mortgage loan is a relocation mortgage loan, made to borrowers whose employers relocate their employees.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Relocation_Mortgage_Indicator">Documentation</a>')
    """"""

    high_balance_loan_indicator = models.BooleanField(blank=True, null=True,
                                                      help_text='An indicator that denotes if the original principal balance of a mortgage loan is greater than the general conforming loan limit and up to the high-cost area loan limit.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.High_Balance_Loan_Indicator">Documentation</a>')
    """"""

    initial_fixed_rate_period = models.FloatField(blank=True, null=True,
                                                  help_text='For an adjustable-rate mortgage loan, the number of months between the first full month the mortgage loan accrues interest and the initial interest rate change date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Initial_Fixed-Rate_Period">Documentation</a>')
    """"""

    initial_interest_rate_cap = models.FloatField(blank=True, null=True,
                                                  help_text='For an adjustable-rate mortgage loan, the maximum percentage points the interest rate can adjust upward at the initial interest rate change date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Initial_Interest_Rate_Cap">Documentation</a>')
    """"""

    special_eligibility_program = models.IntegerField(blank=True, null=True,
                                                      choices=SPECIAL_ELIGIBILITY_PROGRAM_CHOICES,
                                                      help_text='A mortgage program with expanded eligibility criteria designed to increase and maintain home ownership.<a class ="risk_manual_url" href="https://www.openriskmanual.org/wiki"> Documentation</a>')
    """"""

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    """The first insertion date of the data point"""

    last_change_date = models.DateTimeField(auto_now=True)
    """The last change date of the data point"""

    def __str__(self):
        """String representing the data object"""
        return self.loan_identifier

    def get_absolute_url(self):
        """Absolute URL where the data point can be edited"""
        return reverse('sflp_portfolio:loan_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
