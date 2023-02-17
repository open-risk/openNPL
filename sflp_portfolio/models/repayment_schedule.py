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


class RepaymentSchedule(models.Model):
    """
    The RepaymentSchedule model holds Repayment Schedule data (Code String)

    .. note:: The Agency Single Family Loan Performance Template does not explicitly segment data attributes into Counterparty, Loan etc. The assignment into tables (models) in openNPL is based on the interpretation and main function of different data fields

    .. note:: Fields are currently segmented into static and dynamic. In the future dynamic attributes may move to new models. The distinction is not always clear and may depend on the availability of updated date

    """

    #
    # IDENTIFICATION FIELDS
    #

    #
    # FOREIGN KEYS
    #

    # Loan ID Foreign Key
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True,
                                help_text="The load ID to which the repayment schedule refers")

    #
    # DATA PROPERTIES
    #

    loan_payment_history = models.TextField(blank=True, null=True,
                                            help_text='The coded string of values that describes the payment performance of the loan over the most recent 24 months.  The most recent month is located to the right.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

















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
