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

from sflp_portfolio.models.loan import Loan
from sflp_portfolio.models.model_choices import *
from sflp_portfolio.models.models import PortfolioSnapshot


class LoanState(models.Model):
    """
    The Loan State model holds temporally variable Loan Portfolio data. There is no specific Loan State ID, it links to the underlying Loan ID


    """

    #
    # FOREIGN KEYS
    #

    # Portfolio Snapshot ID Foreign Key
    portfolio_snapshot_id = models.ForeignKey(PortfolioSnapshot, on_delete=models.CASCADE, blank=True, null=True,
                                              help_text="The portfolio snapshot ID to which the Loan State belongs")
    """The snapshot to which the loan state corresponds"""

    # Loan ID Foreign Key
    loan_identifier = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True,
                                        help_text='The loan ID to which the loan state links.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Loan_Identifier">Documentation</a>')
    """The loan ID to which the loan state links."""

    #
    # DYNAMIC DATA PROPERTIES
    #

    current_actual_upb = models.FloatField(blank=True, null=True,
                                           help_text='The current actual outstanding unpaid principal balance of a mortgage loan, reflective of payments actually received from the related borrower.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Current_Actual_UPB">Documentation</a>')
    """"""

    current_interest_rate = models.FloatField(blank=True, null=True,
                                              help_text='The rate of interest in effect for the periodic installment due.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Current_Interest_Rate">Documentation</a>')
    """"""

    high_loan_to_value_refinance_option_indicator = models.BooleanField(blank=True, null=True, help_text='An indicator that denotes if an eligible original reference loan is refinanced under Fannie Mae’s HLTV refinance option, which results in such mortgage loan remaining in the Reference Pool, as further defined in each individual CRT document, if applicable.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.High_Loan_to_Value_Refinance_Option_Indicator">Documentation</a>')
    """"""

    index = models.TextField(blank=True, null=True,
                             help_text='For adjustable-rate loans, the description of the index on which adjustments to the interest rate are based.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Index">Documentation</a>')
    """"""

    interest_only_first_principal_and_interest_payment_date = models.DateField(blank=True, null=True, help_text='For interest-only loans, the month and year that the first monthly scheduled fully amortizing principal and interest payment is due.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Interest_Only_First_Principal_And_Interest_Payment_Date">Documentation</a>')
    """"""

    interest_only_loan_indicator = models.BooleanField(blank=True, null=True,
                                                       help_text='An indicator that denotes whether the loan only requires interest payments for a specified period of time beginning with the first payment date.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Interest_Only_Loan_Indicator">Documentation</a>')
    """"""

    interest_rate_adjustment_frequency = models.FloatField(blank=True, null=True,
                                                           help_text='For an adjustable-rate mortgage loan, the number of months between scheduled rate changes. For loans with an Initial Fixed-Rate Period, the number of months between subsequent rate adjustments. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Interest_Rate_Adjustment_Frequency">Documentation</a>')
    """"""

    loan_age = models.FloatField(blank=True, null=True,
                                 help_text='The number of calendar months since the mortgage loans origination date. For purposes of calculating this data element, origination means the date on which the first full month of interest begins to accrue.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Loan_Age">Documentation</a>')
    """"""

    master_servicer = models.TextField(blank=True, null=True,
                                       help_text='Fannie Mae.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Master_Servicer">Documentation</a>')
    """"""

    maturity_date = models.DateField(blank=True, null=True,
                                     help_text='The month and year in which a mortgage loan is scheduled to be paid in full as defined in the mortgage loan documents.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Maturity_Date">Documentation</a>')
    """"""

    mortgage_insurance_cancellation_indicator = models.TextField(blank=True, null=True,
                                                                 help_text='An indicator that denotes if the mortgage insurance (MI) has been cancelled since origination.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Mortgage_Insurance_Cancellation_Indicator">Documentation</a>')
    """"""

    mortgage_margin = models.FloatField(blank=True, null=True,
                                        help_text='For an adjustable-rate mortgage loan, the rate that is added to the index value to establish the new interest rate (after applying all applicable caps and floors) accruing on the loan at each interest rate change date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Mortgage_Margin">Documentation</a>')
    """"""

    next_interest_rate_adjustment_date = models.DateField(blank=True, null=True,
                                                          help_text='For adjustable-rate loans, the month and year that the interest rate is next subject to change.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Next_Interest_Rate_Adjustment_Date">Documentation</a>')
    """"""

    next_payment_change_date = models.DateField(blank=True, null=True,
                                                help_text='For an adjustable-rate mortgage loan, the next date on which the payment amount due from the borrower is subject to change. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Next_Payment_Change_Date">Documentation</a>')
    """"""

    periodic_interest_rate_cap = models.FloatField(blank=True, null=True,
                                                   help_text='For an adjustable-rate mortgage loan, the maximum percentage points the interest rate can adjust upward at each interest rate change date after the initial interest rate change date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Periodic_Interest_Rate_Cap">Documentation</a>')
    """"""

    servicer_name = models.TextField(blank=True, null=True,
                                     help_text='The name of the entity that serves as the primary servicer of the mortgage loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Servicer_Name">Documentation</a>')
    """"""

    servicing_activity_indicator = models.BooleanField(blank=True, null=True,
                                                       help_text='An indicator that denotes a change in servicing activity during the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Servicing_Activity_Indicator">Documentation</a>')
    """"""

    zero_balance_code = models.IntegerField(blank=True, null=True, choices=ZERO_BALANCE_CODE_CHOICES,
                                            help_text='A code indicating the reason the loans balance was reduced to zero or experienced a credit event, if applicable. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Zero_Balance_Code">Documentation</a>')
    """"""

    upb_at_the_time_of_removal = models.FloatField(blank=True, null=True,
                                                   help_text='The unpaid principal balance of the loan at the time of removal.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.UPB_at_the_Time_of_Removal">Documentation</a>')
    """"""

    zero_balance_code_change_date = models.DateField(blank=True, null=True,
                                                     help_text='The most recent date in which a loan status change was identified, resulting from corresponding change to the Zero Balance Code.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Zero_Balance_Code_Change_Date">Documentation</a>')
    """"""

    zero_balance_effective_date = models.DateField(blank=True, null=True,
                                                   help_text='Date on which the mortgage loan balance was reduced to zero.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Zero_Balance_Effective_Date">Documentation</a>')
    """"""

    scheduled_principal_current = models.FloatField(blank=True, null=True,
                                                    help_text='The minimum principal payment the borrower is obligated to pay for the corresponding reporting period, based on the terms provided in the related mortgage loan documents, provided that the payment is collected from the borrower by the servicer and reported to Fannie Mae for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Scheduled_Principal_Current">Documentation</a>')
    """"""

    unscheduled_principal_current = models.FloatField(blank=True, null=True,
                                                      help_text='The principal amount received in excess of the scheduled principal payment collected from the borrower by the servicer and reported to Fannie Mae for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Unscheduled_Principal_Current">Documentation</a>')
    """"""

    total_principal_current = models.FloatField(blank=True, null=True,
                                                help_text='The change between the prior reporting period’s disclosed Current Actual UPB and the current reporting period’s disclosed Current Actual UPB.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Total_Principal_Current">Documentation</a>')
    """"""

    months_to_amortization = models.IntegerField(blank=True, null=True,
                                                 help_text='For interest-only loans, the number of months from the current month to the first scheduled principal and interest payment date.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Months_to_Amortization">Documentation</a>')
    """"""

    remaining_months_to_legal_maturity = models.IntegerField(blank=True, null=True,
                                                             help_text='The number of calendar months remaining until the mortgage loan is due to be paid in full based on the maturity date as defined in the mortgage documents.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Remaining_Months_to_Legal_Maturity">Documentation</a>')
    """"""

    remaining_months_to_maturity = models.IntegerField(blank=True, null=True,
                                                       help_text='The number of calendar months remaining until the outstanding unpaid principal balance of the mortgage loan amortizes to a zero balance, taking into account any additional prepayments, which could lead to the loan paying off earlier than its maturity date.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Remaining_Months_To_Maturity">Documentation</a>')
    """"""

    last_paid_installment_date = models.DateField(blank=True, null=True,
                                                  help_text='The due date of the last paid installment that was collected for the mortgage loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Last_Paid_Installment_Date">Documentation</a>')
    """"""

    loan_holdback_effective_date = models.DateField(blank=True, null=True,
                                                    help_text='The date of the latest Loan Holdback indicator change.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Loan_Holdback_Effective_Date">Documentation</a>')
    """"""

    loan_holdback_indicator = models.IntegerField(blank=True, null=True, choices=LOAN_HOLDBACK_INDICATOR_CHOICES,
                                                  help_text='An indicator that denotes if a loan has been moved temporarily into a hold status to allow Fannie Mae to further evaluate unique situations that may otherwise result in a credit event or loan removal.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Loan_Holdback_Indicator">Documentation</a>')
    """"""

    repayment_history = models.TextField(blank=True, null=True,
                                         help_text='The coded string of values that describes the payment performance of the loan over the most recent 24 months. The most recent month is located to the right.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Loan_Payment_History">Documentation</a>')
    """The coded string of values that describes the payment performance of the loan over the most recent 24 months"""

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    """The first insertion date of the data point"""

    last_change_date = models.DateTimeField(auto_now=True)
    """The last change date of the data point"""

    def __str__(self):
        """String representing the data object"""
        return "State of Loan " + str(self.loan_identifier)

    def get_absolute_url(self):
        """Absolute URL where the data point can be edited"""
        return reverse('sflp_portfolio:LoanState_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Loan State"
        verbose_name_plural = "Loan States"
