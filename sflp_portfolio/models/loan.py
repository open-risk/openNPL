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

    .. note:: The Agency Single Family Loan Performance Template does not explicitly segment data attributes into Counterparty, Loan etc. The assignment into tables (models) in openNPL is based on the interpretation and main function of different data fields

    .. note:: Fields are currently segmented into static and dynamic. In the future dynamic attributes may move to new models. The distinction is not always clear and may depend on the availability of updated date

    """

    #
    # IDENTIFICATION FIELDS
    #

    loan_identifier = models.TextField(blank=True, null=True,
                                       help_text='A unique identifier for the mortgage loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    #
    # FOREIGN KEYS
    #

    # Portfolio ID Foreign Key
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, blank=True, null=True,
                                     help_text="The portfolio ID to which the Loan belongs")

    # NOTE: Seller is captured in Portfolio name
    # seller_name = models.TextField(blank=True, null=True,
    #                                help_text='The name of the entity that delivered the mortgage loan to Fannie Mae.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    # Snapshot ID  Foreign Key
    snapshot = models.ForeignKey(PortfolioSnapshot, on_delete=models.CASCADE, blank=True, null=True,
                                    help_text="The snapshot ID to which the Loan belongs")

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
    # DYNAMIC DATA PROPERTIES
    #


    arm_balloon_indicator = models.BooleanField(blank=True, null=True,
                                                help_text='For an adjustable-rate mortgage loan, a code that denotes if the loan has a balloon feature.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    arm_cap_structure = models.TextField(blank=True, null=True,
                                         help_text='For an adjustable-rate mortgage loan, a numeric string that explains the interest rate caps on the ARM. The first number is the Initial Interest Rate Cap Up Percent (i.e., the maximum percentage points the interest rate can adjust upward at the initial rate change date). The second number is the Periodic Interest Rate Cap Up Percent (i.e., the maximum percentage points the interest rate can adjust upward at each interest rate change date after the initial interest rate change date). The third number is the Lifetime Interest Rate Cap Up Percent (i.e., the maximum percentage points that the interest rate can adjust upward over the life of the loan relative to the initial interest rate).<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    arm_initial_fixed_rate_period_less_than_5_yr = models.BooleanField(blank=True, null=True,
                                                                       help_text='For an adjustable-rate mortgage loan, an indicator that denotes if the Initial Fixed-Rate Period is less than or equal to five years.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    arm_plan_number = models.FloatField(blank=True, null=True,
                                        help_text='For an adjustable-rate mortgage loan, a code identifying the standardized plan under which the mortgage loan was delivered to Fannie Mae. The ARM plan outlines the characteristics of the adjustable-rate mortgage loan, including the ARM Index, the Initial Fixed-Rate Period, the Cap Structure, look-back days, assumability, and the option to convert to a fixed-rate mortgage loan..<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    arm_product_type = models.TextField(blank=True, null=True,
                                        help_text='For an adjustable-rate mortgage loan, a string that denotes the Initial Fixed-Rate Period, the subsequent Interest Rate Adjustment Frequency, and the Original Loan Term.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')



    cumulative_credit_event_net_gain_or_loss = models.FloatField(blank=True, null=True,
                                                                 help_text='The cumulative net realized gain or loss amounts for a mortgage loan resulting from a credit event.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_actual_upb = models.FloatField(blank=True, null=True,
                                           help_text='The current actual outstanding unpaid principal balance of a mortgage loan, reflective of payments actually received from the related borrower.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_interest_rate = models.FloatField(blank=True, null=True,
                                              help_text='The rate of interest in effect for the periodic installment due.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_loan_delinquency_status = models.TextField(blank=True, null=True,
                                                       help_text='The number of months the obligor is delinquent as determined by the governing mortgage documents.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_period_credit_event_net_gain_or_loss = models.FloatField(blank=True, null=True,
                                                                     help_text='The net realized gain or loss amount calculated for a mortgage loan resulting from a credit event for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    delinquent_accrued_interest = models.FloatField(blank=True, null=True,
                                                    help_text='The lost accrued interest amount calculated for a mortgage loan that becomes subject to a credit event for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    high_loan_to_value_refinance_option_indicator = models.BooleanField(blank=True, null=True,
                                                                        help_text='An indicator that denotes if an eligible original reference loan is refinanced under Fannie Mae’s HLTV refinance option, which results in such mortgage loan remaining in the Reference Pool, as further defined in each individual CRT document, if applicable.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    index = models.TextField(blank=True, null=True,
                             help_text='For adjustable-rate loans, the description of the index on which adjustments to the interest rate are based.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    initial_fixed_rate_period = models.FloatField(blank=True, null=True,
                                                  help_text='For an adjustable-rate mortgage loan, the number of months between the first full month the mortgage loan accrues interest and the initial interest rate change date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    initial_interest_rate_cap = models.FloatField(blank=True, null=True,
                                                  help_text='For an adjustable-rate mortgage loan, the maximum percentage points the interest rate can adjust upward at the initial interest rate change date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    interest_only_first_principal_and_interest_payment_date = models.DateField(blank=True, null=True,
                                                                               help_text='For interest-only loans, the month and year that the first monthly scheduled fully amortizing principal and interest payment is due.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    interest_only_loan_indicator = models.BooleanField(blank=True, null=True,
                                                       help_text='An indicator that denotes whether the loan only requires interest payments for a specified period of time beginning with the first payment date.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    interest_rate_adjustment_frequency = models.FloatField(blank=True, null=True,
                                                           help_text='For an adjustable-rate mortgage loan, the number of months between scheduled rate changes. For loans with an Initial Fixed-Rate Period, the number of months between subsequent rate adjustments. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    lifetime_interest_rate_cap = models.FloatField(blank=True, null=True,
                                                   help_text='For an adjustable-rate mortgage loan, the maximum percentage points that the interest rate can adjust upward over the life of the loan relative to the initial interest rate.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    loan_age = models.FloatField(blank=True, null=True,
                                 help_text='The number of calendar months since the mortgage loans origination date. For purposes of calculating this data element, origination means the date on which the first full month of interest begins to accrue.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    loan_holdback_effective_date = models.DateField(blank=True, null=True,
                                                    help_text='The date of the latest Loan Holdback indicator change.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    loan_holdback_indicator = models.IntegerField(blank=True, null=True, choices=LOAN_HOLDBACK_INDICATOR_CHOICES,
                                                  help_text='An indicator that denotes if a loan has been moved temporarily into a ‘hold’ status to allow Fannie Mae to further evaluate unique situations that may otherwise result in a credit event or loan removal. Such situations may include loans with reported data anomalies, loans currently in forbearance due to a natural disaster or loans refinanced under the High LTV program that will continue to be included in the reference pool.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    master_servicer = models.TextField(blank=True, null=True,
                                       help_text='Fannie Mae.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    maturity_date = models.DateField(blank=True, null=True,
                                     help_text='The month and year in which a mortgage loan is scheduled to be paid in full as defined in the mortgage loan documents.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    mortgage_insurance_cancellation_indicator = models.TextField(blank=True, null=True,
                                                                 help_text='An indicator that denotes if the mortgage insurance (MI) has been cancelled since origination.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')



    mortgage_margin = models.FloatField(blank=True, null=True,
                                        help_text='For an adjustable-rate mortgage loan, the rate that is added to the index value to establish the new interest rate (after applying all applicable caps and floors) accruing on the loan at each interest rate change date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    next_interest_rate_adjustment_date = models.DateField(blank=True, null=True,
                                                          help_text='For adjustable-rate loans, the month and year that the interest rate is next subject to change.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    next_payment_change_date = models.DateField(blank=True, null=True,
                                                help_text='For an adjustable-rate mortgage loan, the next date on which the payment amount due from the borrower is subject to change. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    periodic_interest_rate_cap = models.FloatField(blank=True, null=True,
                                                   help_text='For an adjustable-rate mortgage loan, the maximum percentage points the interest rate can adjust upward at each interest rate change date after the initial interest rate change date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    prepayment_penalty_indicator = models.BooleanField(blank=True, null=True,
                                                       help_text='An indicator that denotes whether the borrower is subject to a penalty for early payment of principal.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')



    repurchase_make_whole_proceeds_flag = models.BooleanField(blank=True, null=True,
                                                              help_text='Indicates if Fannie Mae received proceeds under the terms of its representation and warranty arrangements for the repurchase of the mortgage loan. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    servicer_name = models.TextField(blank=True, null=True,
                                     help_text='The name of the entity that serves as the primary servicer of the mortgage loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    servicing_activity_indicator = models.BooleanField(blank=True, null=True,
                                                       help_text='An indicator that denotes a change in servicing activity during the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    special_eligibility_program = models.IntegerField(blank=True, null=True,
                                                      choices=SPECIAL_ELIGIBILITY_PROGRAM_CHOICES,
                                                      help_text='A mortgage program with expanded eligibility criteria designed to increase and maintain home ownership.<a class ="risk_manual_url" href="https://www.openriskmanual.org/wiki" > Documentation < / a > ')

    upb_at_issuance = models.FloatField(blank=True, null=True,
                                        help_text='The unpaid principal balance of the loan as of the cut-off date of the reference pool.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

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
