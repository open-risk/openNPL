# Copyright (c) 2020 - 2022 Open Risk (https://www.openriskmanagement.com)
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

from sflp_portfolio.loan_choices import *

from sflp_portfolio.models import PortfolioSnapshot, Portfolio

class Loan(models.Model):
    """
    The Loan model holds Loan Portfolio data

    .. note:: The Agency Single Family Loan Performance Template does not explicitly segment data attributes into Counterparty, Loan etc. The assignment into tables (models) in openNPL is based on the interpretation and main function of different data fields

    """


    #
    # IDENTIFICATION FIELDS
    #


    loan_identifier = models.TextField(blank=True, null=True,
                                             help_text='Institution internal identifier for the Loan part. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Instrument_Identifier">Documentation</a>')

    #
    # FOREIGN KEYS
    #


    # Portfolio ID Foreign Key
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE, blank=True, null=True,
                                     help_text="The portfolio ID to which the Counterparty belongs (can be more than one)")

    # Snapshot ID  Foreign Key
    snapshot_id = models.ForeignKey(PortfolioSnapshot, on_delete=models.CASCADE, blank=True, null=True,
                                    help_text="The snapshot ID to which the Counterparty belongs")


    #
    # DATA PROPERTIES
    #



    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contract_identifier

    def get_absolute_url(self):
        return reverse('sflp_portfolio:loan_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
