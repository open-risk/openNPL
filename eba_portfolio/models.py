# Copyright (c) 2020 Open Risk (https://www.openriskmanagement.com)
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
from django.contrib.auth.models import User
from django.urls import reverse

'''
Models are core Relations (Tables) of the EBA Portfolio Template
`EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Template>`_

Each model is implemented in a separate file EBA_TABLE_NAME.py
TODO Missing are the following: the Lease Table and schedule tables (swap cashflows and repayments)

In addition there is a Portfolio model and a Portfolio_Snapshot model

'''

class Portfolio(models.Model):
    """
    Data object holds workflow oriented entity data
    The object is read/write
    Includes reference to user creating the data set
    Portfolio is named to facilitate recognition

    """
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('eba_portfolio:Portfolio_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class Portfolio_Snapshot(models.Model):
    """
    EBA Portfolio_Snapshot object holds EBA Portfolio generated portfolio data
    The object is read/write
    Includes reference to user creating the data set
    Snapshot is named to facilitate recognition
    Actual Snapshot data stored in the EBA Portfolio Models (with foreign key to snapshot)

    """

    creation_date = models.DateTimeField(
        help_text="Date at which the snapshot has been created. Different from the cutoff date")

    cutoff_date = models.DateTimeField(blank=True, null=True,
                                       help_text="Portfolio Cutoff Date (If available). Different from the creation date")

    name = models.CharField(max_length=200, help_text="An assigned name to help identify the snapshot")

    notes = models.CharField(max_length=300, blank=True, null=True,
                             help_text="Description of the purpose or other relevant information about the portfolio")
    # user_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             help_text="The user that created the portfolio")

    def __str__(self):
        return str(self.creation_date)

    def get_absolute_url(self):
        return reverse('eba_portfolio:EBA Portfolio_Snapshot_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio Snapshot"
        verbose_name_plural = "Portfolio Snapshots"


from eba_portfolio.counterparty import Counterparty
from eba_portfolio.loan import Loan
from eba_portfolio.counterparty_group import CounterpartyGroup
from eba_portfolio.external_collection import ExternalCollection
from eba_portfolio.forbearance import Forbearance
from eba_portfolio.non_property_collateral import NonPropertyCollateral
from eba_portfolio.property_collateral import PropertyCollateral
from eba_portfolio.enforcement import Enforcement
