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
    The Enforcement model holds Enforcement related data

     note:: The Agency Single Family Loan Performance Template does not explicitly segment data attributes into Counterparty, Loan etc. The assignment into tables (models) in openNPL is based on the interpretation and main function of different data fields

     .. note:: Fields are currently segmented into static and dynamic. In the future dynamic attributes may move to new models. The distinction is not always clear and may depend on the availability of updated date

    """

    #
    # IDENTIFICATION FIELDS
    #

    #
    # FOREIGN KEYS
    #

    property_collateral_identifier = models.ForeignKey(PropertyCollateral, on_delete=models.CASCADE, null=True,
                                                       blank=True)

    # Loan ID Foreign Key
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True,
                                help_text="The portfolio ID to which the Counterparty belongs (can be more than one)")

    #
    # DYNAMIC DATA PROPERTIES
    #

    asset_recovery_costs = models.FloatField(blank=True, null=True,
                                             help_text='Expenses associated with removing occupants and personal property from an occupied property post foreclosure. Such expenses include relocation assistance, deed-in-lieu fee, and fees and costs associated with eviction actions.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    credit_enhancement_proceeds = models.FloatField(blank=True, null=True,
                                                    help_text='Proceeds from claims on primary and certain other limited mortgage insurance policies, and recourse and indemnification payments from lenders under arrangements designed to limit credit exposure to Fannie Mae.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_list_price = models.FloatField(blank=True, null=True,
                                           help_text='The price at which a real property is offered for sale.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_list_start_date = models.DateField(blank=True, null=True,
                                               help_text='The agreed upon date, between a property seller and a broker, authorizing the broker to begin the process to procure a buyer or tenant for the property seller’s real property.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    disposition_date = models.DateField(blank=True, null=True,
                                        help_text='The date on which Fannie Mae’s interest in a property ends through either the transfer of the property to a third party or the satisfaction of the mortgage obligation.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    foreclosure_costs = models.FloatField(blank=True, null=True,
                                          help_text='Expenses associated with obtaining title to property from the mortgagor, valuing the property, and maintaining utility services to the property. Such costs include costs and fees associated with bankruptcy and foreclosure.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    foreclosure_date = models.DateField(blank=True, null=True,
                                        help_text='The date on which the completion of the legal action of foreclosure occurred.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    foreclosure_principal_writeoff_amount = models.FloatField(blank=True, null=True,
                                                              help_text='Amounts that Fannie Mae or its loan servicers have determined to be uncollectable under applicable state laws, due to foreclosure statute of limitations.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    net_sales_proceeds = models.FloatField(blank=True, null=True,
                                           help_text='Total cash received from the sale of the property net of any applicable selling expenses, such as fees and commissions, allowable for inclusion under the terms of the property sale, as currently reported on the HUD-1 or other settlement statement.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_list_price = models.FloatField(blank=True, null=True,
                                            help_text='The initial price at which a real property is offered for sale by the property seller. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_list_start_date = models.DateField(blank=True, null=True,
                                                help_text='The agreed upon date, between a property seller and a broker, authorizing the broker to begin the process to procure a buyer or tenant for the property seller’s real property.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    other_foreclosure_proceeds = models.FloatField(blank=True, null=True,
                                                   help_text='Amounts, other than sale proceeds, received by Fannie Mae following foreclosure of a property, including redemption proceeds received from the mortgagor.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    repurchase_make_whole_proceeds = models.FloatField(blank=True, null=True,
                                                       help_text='Amounts received by Fannie Mae under the terms of our representation and warranty arrangements for the repurchase of the mortgage loan or the subject property or loss reimbursement subsequent to property disposition.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('sflp_portfolio:Enforcement_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Enforcement"
        verbose_name_plural = "Enforcements"
