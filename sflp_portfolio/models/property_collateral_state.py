# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
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

from sflp_portfolio.models.model_choices import *
from sflp_portfolio.models.models import PortfolioSnapshot
from sflp_portfolio.models.property_collateral import PropertyCollateral


class PropertyCollateralState(models.Model):
    """
    The PropertyCollateralState model object holds dynamic (temporally varying) Property Collateral state data. There is no unique collateral state ID. Links to the underlying Property Collateral



    """

    #
    # FOREIGN KEYS
    #

    # Portfolio Snapshot ID Foreign Key
    portfolio_snapshot_id = models.ForeignKey(PortfolioSnapshot, on_delete=models.CASCADE, blank=True, null=True,
                                              help_text="The portfolio snapshot ID to which the Property Collateral State belongs")
    """"""

    # Portfolio ID Foreign Key
    property_collateral_id = models.ForeignKey(PropertyCollateral, on_delete=models.CASCADE, blank=True, null=True,
                                               help_text="The loan ID to which the Property Collateral corresponds.")
    """"""

    #
    # DYNAMIC DATA PROPERTIES
    #
    associated_taxes_for_holding_property = models.FloatField(blank=True, null=True,
                                                              help_text='Payment of taxes associated with holding the property.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Associated_Taxes_for_Holding_Property">Documentation</a>')
    """"""

    miscellaneous_holding_expenses_and_credits = models.FloatField(blank=True, null=True,
                                                                   help_text='Expenses and credits associated with preserving the property, including Homeowners Association and other dues; flood, hazard, and MI premiums and refunds; rental income; and title insurance costs.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Miscellaneous_Holding_Expenses_and_Credits">Documentation</a>')
    """"""

    property_preservation_and_repair_costs = models.FloatField(blank=True, null=True,
                                                               help_text='The expenses associated with securing and preserving the property including two major categories:  maintenance and repairs. Maintenance costs are associated with preserving the property through normal upkeep, while repairs are associated with either avoiding deterioration of the asset or a marketing decision to help maximize sales proceeds upon final disposition.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Property_Preservation_and_Repair_Costs">Documentation</a>')
    """"""

    property_valuation_method = models.IntegerField(blank=True, null=True, choices=PROPERTY_VALUATION_METHOD_CHOICES,
                                                    help_text='An indicator that denotes the method by which the value of the subject property was obtained.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    """The first insertion date of the data point"""

    last_change_date = models.DateTimeField(auto_now=True)
    """The last change date of the data point"""

    def __str__(self):
        """String representing the data object"""
        return "State of Collateral " + str(self.property_collateral_id)

    def get_absolute_url(self):
        """Absolute URL where the data point can be edited"""
        return reverse('sflp_portfolio:property_collateral_state_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Property Collateral State"
        verbose_name_plural = "Property Collateral States"
