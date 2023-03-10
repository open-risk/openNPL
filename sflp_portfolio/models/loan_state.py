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

from sflp_portfolio.models.loan import Loan
from sflp_portfolio.models.model_choices import *
from sflp_portfolio.models.models import PortfolioSnapshot


class LoanState(models.Model):
    """
    The Loan State model holds variable Loan Portfolio data


    """

    #
    # FOREIGN KEYS
    #

    # Portfolio Snapshot ID Foreign Key
    portfolio_snapshot_id = models.ForeignKey(PortfolioSnapshot, on_delete=models.CASCADE, blank=True, null=True,
                                              help_text="The portfolio snapshot ID to which the Loan State belongs")

    # Loan ID Foreign Key
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True,
                                help_text='The loan ID to which the loan state links.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Loan_Identifier">Documentation</a>')
    """The loan ID to which the loan state links."""

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
                                                      help_text='A mortgage program with expanded eligibility criteria designed to increase and maintain home ownership.<a class ="risk_manual_url" href="https://www.openriskmanual.org/wiki"> Documentation</a>')

    upb_at_issuance = models.FloatField(blank=True, null=True,
                                        help_text='The unpaid principal balance of the loan as of the cut-off date of the reference pool.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    zero_balance_code = models.IntegerField(blank=True, null=True, choices=ZERO_BALANCE_CODE_CHOICES,
                                            help_text='A code indicating the reason the loans balance was reduced to zero or experienced a credit event, if applicable. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    upb_at_the_time_of_removal = models.FloatField(blank=True, null=True,
                                                   help_text='The unpaid principal balance of the loan at the time of removal.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    zero_balance_code_change_date = models.DateField(blank=True, null=True,
                                                     help_text='The most recent date in which a loan status change was identified, resulting from corresponding change to the Zero Balance Code.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    zero_balance_effective_date = models.DateField(blank=True, null=True,
                                                   help_text='Date on which the mortgage loan balance was reduced to zero.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    scheduled_principal_current = models.FloatField(blank=True, null=True,
                                                    help_text='The minimum principal payment the borrower is obligated to pay for the corresponding reporting period, based on the terms provided in the related mortgage loan documents, provided that the payment is collected from the borrower by the servicer and reported to Fannie Mae for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    unscheduled_principal_current = models.FloatField(blank=True, null=True,
                                                      help_text='The principal amount received in excess of the scheduled principal payment collected from the borrower by the servicer and reported to Fannie Mae for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    total_principal_current = models.FloatField(blank=True, null=True,
                                                help_text='The change between the prior reporting period’s disclosed Current Actual UPB and the current reporting period’s disclosed Current Actual UPB.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    months_to_amortization = models.IntegerField(blank=True, null=True,
                                                 help_text='For interest-only loans, the number of months from the current month to the first scheduled principal and interest payment date.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    remaining_months_to_legal_maturity = models.IntegerField(blank=True, null=True,
                                                             help_text='The number of calendar months remaining until the mortgage loan is due to be paid in full based on the maturity date as defined in the mortgage documents.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    remaining_months_to_maturity = models.IntegerField(blank=True, null=True,
                                                       help_text='The number of calendar months remaining until the outstanding unpaid principal balance of the mortgage loan amortizes to a zero balance, taking into account any additional prepayments, which could lead to the loan paying off earlier than its maturity date.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    last_paid_installment_date = models.DateField(blank=True, null=True,
                                                  help_text='The due date of the last paid installment that was collected for the mortgage loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.loan_id)

    def get_absolute_url(self):
        return reverse('sflp_portfolio:LoanState_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Loan State"
        verbose_name_plural = "Loan States"
