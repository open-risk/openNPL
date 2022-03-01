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

'''
The openNPL models implement the core relations (Tables) of the EBA Portfolio Template
`EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Template>`_

Each model is implemented in a separate file using the convention **TABLE_NAME.py** in the npl_portfolio directory. In addition there is a Portfolio model and a Portfolio_Snapshot model in this (models.py) file. Choice lists for categorical attributes are collected in separate fiels using the convention **TABLE_NAME_CHOICES.py**. 

.. TODO:: Missing are the following: the Lease Table and schedule tables (swap cashflows and repayments)

.. NOTE:: The Relation Tables of the EBA Specification are not implemented (different schema)



'''


class Portfolio(models.Model):

    """
    The portfolio data object is useful to aggregate datasets belonging to the same actual credit portfolio. A portfolio may be optionally named to facilitate recognition and a longer description provides further details.

    .. note:: The actual Portfolio data are stored in the various NPL models (with foreign key to Portfolio)

    """
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True, help_text='Description of the portfolio')

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('npl_portfolio:Portfolio_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class PortfolioSnapshot(models.Model):
    """
    The NPL Portfolio_Snapshot object groups NPL Portfolio generated portfolio data for a given cutoff date. The Snapshot may be named to facilitate recognition.

    .. note:: The actual Snapshot data are stored in the various NPL Models (with foreign key to a snapshot)

    """

    creation_date = models.DateTimeField(auto_now_add=True,
        help_text="Date at which the snapshot has been created. Different from the cutoff date")
    last_change_date = models.DateTimeField(auto_now=True)

    cutoff_date = models.DateTimeField(blank=True, null=True,
                                       help_text="Portfolio Cutoff Date (If available). Different from the creation date")

    name = models.CharField(blank=True, null=True, max_length=200, help_text="An assigned name to help identify the snapshot. By convention the name of the portfolio plus the cutoff date")


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('npl_portfolio:PortfolioSnapshot_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio Snapshot"
        verbose_name_plural = "Portfolio Snapshots"


# ATTN Those imports MUST be placed after loading the Portfolio / PortfolioSnapshot classes
#
#   NPL Models
#

from npl_portfolio.counterparty_group import CounterpartyGroup
from npl_portfolio.counterparty import Counterparty
from npl_portfolio.loan import Loan
from npl_portfolio.non_property_collateral import NonPropertyCollateral
from npl_portfolio.property_collateral import PropertyCollateral
from npl_portfolio.external_collection import ExternalCollection
from npl_portfolio.forbearance import Forbearance
from npl_portfolio.enforcement import Enforcement
