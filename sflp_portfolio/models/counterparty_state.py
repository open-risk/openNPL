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

from sflp_portfolio.models.counterparty import Counterparty
from sflp_portfolio.models.models import PortfolioSnapshot


class CounterpartyState(models.Model):
    """
    The CounterpartyState model holds temporally changing Counterparty data. There is no unique ID, it links to the Counterparty object


    """

    #
    # FOREIGN KEYS
    #

    # Portfolio Snapshot ID Foreign Key
    portfolio_snapshot_id = models.ForeignKey(PortfolioSnapshot, on_delete=models.CASCADE, blank=True, null=True,
                                              help_text="The portfolio snapshot ID to which the Counterparty State corresponds.")

    # counterparty ID Foreign Key
    counterparty_id = models.ForeignKey(Counterparty, on_delete=models.CASCADE, blank=True, null=True,
                                        help_text="The counterparty ID to which the Counterparty State corresponds.")


    #
    # DYNAMIC DATA PROPERTIES
    #

    borrower_credit_score_current = models.FloatField(blank=True, null=True,
                                                      help_text='A numerical value used by the financial services industry to evaluate the quality of borrower credit. Credit scores are typically based on a proprietary statistical model that is developed for use by credit data repositories. These credit repositories apply the model to borrower credit information to arrive at a credit score. When this term is used by Fannie Mae, it is referring to FICO Score developed by Fair Isaac Corporation and provided by Equifax Inc and is distinct from the FICO Score referenced in Fannie Mae Selling Guide, which may be provided by any of the three major credit repositories.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Borrower_Credit_Score_Current">Documentation</a>')
    """A numerical value used by the financial services industry to evaluate the quality of borrower credit. The initial credit score value is tracked by the Counterparty model."""

    coborrower_credit_score_current = models.FloatField(blank=True, null=True,
                                                        help_text='A numerical value used by the financial services industry to evaluate the quality of borrower credit. Credit scores are typically based on a proprietary statistical model that is developed for use by credit data repositories. These credit repositories apply the model to borrower credit information to arrive at a credit score. When this term is used by Fannie Mae, it is referring to FICO Score developed by Fair Isaac Corporation and provided by Equifax Inc and is distinct from the FICO Score referenced in Fannie Mae Selling Guide.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Co-Borrower_Credit_Score_Current">Documentation</a>')
    """A numerical value used by the financial services industry to evaluate the quality of borrower credit. The initial credit score value is tracked by the Counterparty model."""

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    """The first insertion date of the data point"""

    last_change_date = models.DateTimeField(auto_now=True)
    """The last change date of the data point"""

    def __str__(self):
        """String representing the data object."""
        return "State of " + str(self.counterparty_id)

    def get_absolute_url(self):
        """Absolute URL where the data point can be edited"""
        return reverse('sflp_portfolio:CounterpartyState_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Counterparty State"
        verbose_name_plural = "Counterparty States"
