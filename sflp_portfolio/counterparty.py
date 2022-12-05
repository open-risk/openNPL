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

from sflp_portfolio.counterparty_choices import *

from sflp_portfolio.loan import Loan


class Counterparty(models.Model):
    """
    The Counterparty model holds Counterparty data

    .. note:: The Agency Single Family Loan Performance Template does not identify borrowers except implicitly through the loan identification

    .. note:: The Agency Single Family Loan Performance Template does not explicitly segment data attributes into Counterparty, Loan etc. The assignment into tables (models) in openNPL is based on the interpretation and main function of different data fields

    """


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




    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.counterparty_identifier

    def get_absolute_url(self):
        return reverse('sflp_portfolio:Counterparty_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Counterparty"
        verbose_name_plural = "Counterparties"
