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

from sflp_portfolio.models.Loan import Loan
from sflp_portfolio.models.model_choices import *


class RepaymentSchedule(models.Model):
    #
    # IDENTIFICATION FIELDS
    #

    #
    # FOREIGN KEYS
    #

    # Loan ID Foreign Key
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True,
                                help_text="The portfolio ID to which the Counterparty belongs (can be more than one)")

    #
    # DATA PROPERTIES
    #
    last_paid_installment_date = models.DateField(blank=True, null=True,
                                                  help_text='The due date of the last paid installment that was collected for the mortgage loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    loan_payment_history = models.TextField(blank=True, null=True,
                                            help_text='The coded string of values that describes the payment performance of the loan over the most recent 24 months.  The most recent month is located to the right.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    months_to_amortization = models.IntegerField(blank=True, null=True,
                                               help_text='For interest-only loans, the number of months from the current month to the first scheduled principal and interest payment date.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    remaining_months_to_legal_maturity = models.IntegerField(blank=True, null=True,
                                                           help_text='The number of calendar months remaining until the mortgage loan is due to be paid in full based on the maturity date as defined in the mortgage documents.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    remaining_months_to_maturity = models.IntegerField(blank=True, null=True,
                                                     help_text='The number of calendar months remaining until the outstanding unpaid principal balance of the mortgage loan amortizes to a zero balance, taking into account any additional prepayments, which could lead to the loan paying off earlier than its maturity date.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    repurchase_date = models.DateField(blank=True, null=True,
                                       help_text='The date on which a Reversed Credit Event Reference Obligation occurs with respect to a loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    scheduled_principal_current = models.FloatField(blank=True, null=True,
                                                    help_text='The minimum principal payment the borrower is obligated to pay for the corresponding reporting period, based on the terms provided in the related mortgage loan documents, provided that the payment is collected from the borrower by the servicer and reported to Fannie Mae for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    total_principal_current = models.FloatField(blank=True, null=True,
                                                help_text='The change between the prior reporting period’s disclosed Current Actual UPB and the current reporting period’s disclosed Current Actual UPB.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    unscheduled_principal_current = models.FloatField(blank=True, null=True,
                                                      help_text='The principal amount received in excess of the scheduled principal payment collected from the borrower by the servicer and reported to Fannie Mae for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    upb_at_the_time_of_removal = models.FloatField(blank=True, null=True,
                                                   help_text='The unpaid principal balance of the loan at the time of removal.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    zero_balance_code = models.IntegerField(blank=True, null=True, choices=ZERO_BALANCE_CODE_CHOICES,
                                            help_text='A code indicating the reason the loans balance was reduced to zero or experienced a credit event, if applicable. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    zero_balance_code_change_date = models.DateField(blank=True, null=True,
                                                     help_text='The most recent date in which a loan status change was identified, resulting from corresponding change to the Zero Balance Code.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    zero_balance_effective_date = models.DateField(blank=True, null=True,
                                                   help_text='Date on which the mortgage loan balance was reduced to zero...<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('sflp_portfolio:RepaymentSchedule_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Repayment Schedule"
        verbose_name_plural = "Repayment Schedules"
