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

'''
openNPL models implement the core relations (Tables) of the Single Family Loan Performance Template
`Single Family Loan Performance Templates <https://www.openriskmanual.org/wiki/AGENCY_SFLP_Template>`_

Each model is implemented in a separate file using the convention **TABLE_NAME.py** in the sflp_portfolio directory. 
In addition there is a Portfolio model and a Portfolio_Snapshot model in this (models.py) file. 
Choice lists for categorical attributes are collected in separate fields using the convention **TABLE_NAME_CHOICES.py**. 

.. NOTE:: CAS, CIRT and Single-Family (SF) Loan Performance share a common vocabulary with some differences currently not highlighted

'''

from common.models import Portfolio as _Portfolio
from common.models import PortfolioSnapshot as _PortfolioSnapshot


class Portfolio(_Portfolio):
    """
    The portfolio data object is useful to aggregate datasets belonging to the same actual credit portfolio. A portfolio may be optionally named to facilitate recognition and a longer description provides further details.

    .. note:: The actual Portfolio data are stored in the various NPL models (with foreign key to Portfolio)

    """
    deal_name = models.TextField(blank=True, null=True,
                                 help_text='The title of the series issuance.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    reference_pool_id = models.TextField(blank=True, null=True,
                                         help_text='A unique identifier for the reference pool.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sflp_portfolio:Portfolio_edit', kwargs={'pk': self.pk})


class PortfolioSnapshot(_PortfolioSnapshot):
    """
    The SFLP Portfolio_Snapshot object groups Portfolio generated portfolio data for a given cutoff date. The Snapshot may be named to facilitate recognition.

    .. note:: The actual Snapshot data are stored in the various Data Models (with foreign key to a Snapshot)

    """
    monthly_reporting_period = models.TextField(blank=True, null=True,
                                                help_text='The month and year that pertains to the servicer’s cut-off period for mortgage loan information.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.monthly_reporting_period)

    def get_absolute_url(self):
        return reverse('sflp_portfolio:PortfolioSnapshot_edit', kwargs={'pk': self.pk})


# ATTN Those imports MUST be placed after loading the Portfolio / PortfolioSnapshot classes
#
#   SFLP Models
#

from sflp_portfolio.models.counterparty import Counterparty
from sflp_portfolio.models.loan import Loan
from sflp_portfolio.models.property_collateral import PropertyCollateral
from sflp_portfolio.models.forbearance import Forbearance
from sflp_portfolio.models.enforcement import Enforcement
from sflp_portfolio.models.repayment_schedule import RepaymentSchedule
