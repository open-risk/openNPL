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
from sflp_portfolio.models.property_collateral import PropertyCollateral


class Enforcement(models.Model):
    """
    The Enforcement model holds Enforcement related data. Enforcement is contingent action linked to a Loan and Collateral. There is no unique enforcement ID. Links to the collateral ID.


    """

    #
    # IDENTIFICATION FIELDS
    #

    #
    # FOREIGN KEYS
    #

    property_collateral_identifier = models.ForeignKey(PropertyCollateral, on_delete=models.CASCADE, null=True,
                                                       blank=True)


    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True,
                                help_text='The loan ID to which the Enforcement activity links.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Loan_Identifier">Documentation</a>')
    """The loan ID to which the Enforcement activity links."""

    #
    # DYNAMIC DATA PROPERTIES
    #

    asset_recovery_costs = models.FloatField(blank=True, null=True,
                                             help_text='Expenses associated with removing occupants and personal property from an occupied property post foreclosure. Such expenses include relocation assistance, deed-in-lieu fee, and fees and costs associated with eviction actions.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Asset_Recovery_Costs">Documentation</a>')
    """"""

    credit_enhancement_proceeds = models.FloatField(blank=True, null=True,
                                                    help_text='Proceeds from claims on primary and certain other limited mortgage insurance policies, and recourse and indemnification payments from lenders under arrangements designed to limit credit exposure to Fannie Mae.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Credit_Enhancement_Proceeds">Documentation</a>')
    """"""

    current_list_price = models.FloatField(blank=True, null=True,
                                           help_text='The price at which a real property is offered for sale.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Current_List_Price">Documentation</a>')
    """"""

    current_list_start_date = models.DateField(blank=True, null=True,
                                               help_text='The agreed upon date, between a property seller and a broker, authorizing the broker to begin the process to procure a buyer or tenant for the property seller’s real property.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Current_List_Start_Date">Documentation</a>')
    """"""

    cumulative_credit_event_net_gain_or_loss = models.FloatField(blank=True, null=True,
                                                                 help_text='The cumulative net realized gain or loss amounts for a mortgage loan resulting from a credit event.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    disposition_date = models.DateField(blank=True, null=True,
                                        help_text='The date on which Fannie Mae’s interest in a property ends through either the transfer of the property to a third party or the satisfaction of the mortgage obligation.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Disposition_Date">Documentation</a>')
    """"""

    foreclosure_costs = models.FloatField(blank=True, null=True,
                                          help_text='Expenses associated with obtaining title to property from the mortgagor, valuing the property, and maintaining utility services to the property. Such costs include costs and fees associated with bankruptcy and foreclosure.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Foreclosure_Costs">Documentation</a>')
    """"""

    foreclosure_date = models.DateField(blank=True, null=True,
                                        help_text='The date on which the completion of the legal action of foreclosure occurred.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Foreclosure_Date">Documentation</a>')
    """"""

    foreclosure_principal_writeoff_amount = models.FloatField(blank=True, null=True,
                                                              help_text='Amounts that Fannie Mae or its loan servicers have determined to be uncollectable under applicable state laws, due to foreclosure statute of limitations.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Foreclosure_Principal_Write-off_Amount">Documentation</a>')
    """"""

    net_sales_proceeds = models.FloatField(blank=True, null=True,
                                           help_text='Total cash received from the sale of the property net of any applicable selling expenses, such as fees and commissions, allowable for inclusion under the terms of the property sale, as currently reported on the HUD-1 or other settlement statement.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Net_Sales_Proceeds">Documentation</a>')
    """"""

    original_list_price = models.FloatField(blank=True, null=True,
                                            help_text='The initial price at which a real property is offered for sale by the property seller. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Original_List_Price">Documentation</a>')
    """"""

    original_list_start_date = models.DateField(blank=True, null=True,
                                                help_text='The agreed upon date, between a property seller and a broker, authorizing the broker to begin the process to procure a buyer or tenant for the property seller’s real property.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Original_List_Start_Date">Documentation</a>')
    """"""

    other_foreclosure_proceeds = models.FloatField(blank=True, null=True,
                                                   help_text='Amounts, other than sale proceeds, received by Fannie Mae following foreclosure of a property, including redemption proceeds received from the mortgagor.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Other_Foreclosure_Proceeds">Documentation</a>')
    """"""

    repurchase_make_whole_proceeds = models.FloatField(blank=True, null=True,
                                                       help_text='Amounts received by Fannie Mae under the terms of our representation and warranty arrangements for the repurchase of the mortgage loan or the subject property or loss reimbursement subsequent to property disposition.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Repurchase_Make_Whole_Proceeds">Documentation</a>')
    """"""

    repurchase_make_whole_proceeds_flag = models.BooleanField(blank=True, null=True,
                                                              help_text='Indicates if Fannie Mae received proceeds under the terms of its representation and warranty arrangements for the repurchase of the mortgage loan. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Repurchase_Make_Whole_Proceeds_Flag">Documentation</a>')

    repurchase_date = models.DateField(blank=True, null=True,
                                       help_text='The date on which a Reversed Credit Event Reference Obligation occurs with respect to a loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Repurchase_Date">Documentation</a>')
    """"""

    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    """The first insertion date of the data point"""

    last_change_date = models.DateTimeField(auto_now=True)
    """The last change date of the data point"""

    def __str__(self):
        """String representing the data object"""
        return "Enforcement of " + str(self.property_collateral_identifier)


    def get_absolute_url(self):
        """Absolute URL where the data point can be edited"""
        return reverse('sflp_portfolio:Enforcement_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Enforcement"
        verbose_name_plural = "Enforcement"
