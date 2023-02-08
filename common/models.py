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

'''
common abstract openNPL models

Entity
    PrivatePerson
    CorporateEntity
    PublicEntity

Contract
    Loan
    Swap
    Lease
    
Asset
    CommercialRealEstate
    ResidentialRealEstate
    
Collateral
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

    class Meta:
        abstract = True
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class PortfolioSnapshot(models.Model):
    """
    The Portfolio_Snapshot object groups Portfolio generated portfolio data for a given cutoff date. The Snapshot may be named to facilitate recognition.

    .. note:: The actual Snapshot data are stored in the various Data Models (with foreign key to a Snapshot)

    """

    creation_date = models.DateTimeField(auto_now_add=True,
                                         help_text="Date at which the snapshot has been created. Different from the cutoff date")
    last_change_date = models.DateTimeField(auto_now=True)

    cutoff_date = models.DateTimeField(blank=True, null=True,
                                       help_text="Portfolio Cutoff Date (If available). Different from the creation date")

    name = models.CharField(blank=True, null=True, max_length=200,
                            help_text="An assigned name to help identify the snapshot. By convention the name of the portfolio plus the cutoff date")

    class Meta:
        abstract = True
        verbose_name = "Portfolio Snapshot"
        verbose_name_plural = "Portfolio Snapshots"
