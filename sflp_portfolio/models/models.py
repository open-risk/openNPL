# Copyright (c) 2020 - 2024 Open Risk (https://www.openriskmanagement.com)
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
openNPL implements the core relations (Tables) of the Single Family Loan Performance Template
`Single Family Loan Performance Templates <https://www.openriskmanual.org/wiki/FM_SFLP_Template>`_. 

.. NOTE:: The SFLP data template is distinct from the EBA NPL template. While the EBA NPL template is formally defined and is a legal requirement, the SFLP template is merely reflecting the current data structures of published mortgage data. You can learn more about similarities and differences here. (TODO)

Each data model is implemented in a separate file using the convention **TABLE_NAME.py** in the sflp_portfolio directory. In addition there is a Portfolio model and a Portfolio Snapshot model in this (models.py) file. 

Choice lists for categorical attributes are collected in separate files using the convention **TABLE_NAME_CHOICES.py**. 

.. NOTE:: CAS, CIRT and Single-Family (SF) Loan Performance share a common vocabulary with some differences currently not highlighted.

'''

from common.models import Portfolio as _Portfolio
from common.models import PortfolioSnapshot as _PortfolioSnapshot


class Portfolio(_Portfolio):
    """
    The Portfolio data object is useful to aggregate datasets belonging to the same credit portfolio. A Portfolio may be (optionally) named to facilitate recognition. A longer description may provide further details.

    .. note:: The actual Portfolio data are stored in various specific data models (with foreign key to Portfolio).

    """

    deal_name = models.TextField(blank=True, null=True,
                                 help_text='The title of the series issuance.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Deal_Name">Documentation</a>')

    # ALPHA-NUMERIC as TEXT
    reference_pool_id = models.TextField(blank=True, null=True,
                                         help_text='A unique identifier for the reference pool.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Reference_Pool_ID">Documentation</a>')

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sflp_portfolio:Portfolio_edit', kwargs={'pk': self.pk})


class PortfolioSnapshot(_PortfolioSnapshot):
    """
    The SFLP Portfolio_Snapshot object groups Portfolio generated portfolio data for a given cutoff date. The Snapshot may be named to facilitate recognition.

    .. note:: The actual Snapshot data are stored in the various specific Data Models (with foreign key to a Snapshot)

    """
    monthly_reporting_period = models.TextField(blank=True, null=True,
                                                help_text='The month and year that pertains to the servicer’s cut-off period for mortgage loan information.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Monthly_Reporting_Period">Documentation</a>')

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
