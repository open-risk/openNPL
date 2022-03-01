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

from npl_portfolio.enforcement_choices import *
from npl_portfolio.non_property_collateral import NonPropertyCollateral
from npl_portfolio.property_collateral import PropertyCollateral
from npl_portfolio.counterparty import Counterparty


class Enforcement(models.Model):
    """
    The Enforcement model holds Enforcement data conforming to the EBA NPL Template specification
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Enforcement_Table>`_

    """

    #
    # IDENTIFICATION FIELDS
    #

    enforcement_identifier = models.TextField(blank=True, null=True)

    protection_identifier = models.TextField(blank=True, null=True,
                                             help_text='Unique Institution internal identifier for the Property / Collateral as defined in sections "Property Collateral" and "Non-Property Collateral". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Protection_identifier">Documentation</a>')

    #
    # FOREIGN KEYS
    #

    property_collateral_identifier = models.ForeignKey(PropertyCollateral, on_delete=models.CASCADE, null=True,
                                                       blank=True)

    non_property_collateral_identifier = models.ForeignKey(NonPropertyCollateral, on_delete=models.CASCADE, null=True,
                                                           blank=True)

    counterparty_identifier = models.ForeignKey(Counterparty, on_delete=models.CASCADE, null=True, blank=True)

    #
    # DATA PROPERTIES
    #

    amount_of_outstanding_liabilities = models.FloatField(blank=True, null=True,
                                                          help_text='Amount of accrued costs and fees paid by the receiver and to be invoiced to the Institution. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Amount_of_Outstanding_Liabilities">Documentation</a>')

    annual_insurance_payment = models.FloatField(blank=True, null=True,
                                                 help_text='Annual insurance payment to be paid by receiver. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Annual_Insurance_Payment">Documentation</a>')

    contracted_date = models.DateField(blank=True, null=True,
                                       help_text='Contracted date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Contracted_Date">Documentation</a>')

    collateral_repossessed_date = models.DateField(blank=True, null=True,
                                                   help_text='Date that the collateral is repossessed. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Collateral_Repossessed_Date">Documentation</a>')

    costs_accrued_to_buyer = models.FloatField(blank=True, null=True,
                                               help_text='Costs accrued to the buyer. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Costs_Accrued_to_Buyer">Documentation</a>')

    costs_at_end_of_sale = models.FloatField(blank=True, null=True,
                                             help_text='Total costs accrued to the seller at end of sale process. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Costs_at_End_of_Sale">Documentation</a>')

    court_appraisal_amount = models.FloatField(blank=True, null=True,
                                               help_text='Court appraisal amount of the Property / Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Court_Appraisal_Amount">Documentation</a>')

    court_auction_identifier = models.TextField(blank=True, null=True,
                                                help_text='Unique identifier for the auction process. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Court_Auction_identifier">Documentation</a>')

    court_auction_reserve_price_for_first_auction = models.FloatField(blank=True, null=True,
                                                                      help_text='Court set reserve price for first auction, i.e. minimum price required by the court. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Court_Auction_Reserve_Price_for_First_Auction">Documentation</a>')

    court_auction_reserve_price_for_last_auction = models.FloatField(blank=True, null=True,
                                                                     help_text='Court set reserve price for last auction, i.e. minimum price required by the court. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Court_Auction_Reserve_Price_for_Last_Auction">Documentation</a>')

    court_auction_reserve_price_for_next_auction = models.FloatField(blank=True, null=True,
                                                                     help_text='Court set reserve price for next auction, i.e. minimum price required by the court. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Court_Auction_Reserve_Price_for_Next_Auction">Documentation</a>')

    currency_of_enforcement = models.TextField(blank=True, null=True,
                                               help_text='Currency that the items related to enforcement are expressed in. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Currency_of_Enforcement">Documentation</a>')

    current_market_status = models.IntegerField(blank=True, null=True, choices=CURRENT_MARKET_STATUS_CHOICES,
                                                help_text='Current market status of the Property / Collateral as at cut-off date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Current_Market_Status">Documentation</a>')

    date_next_insurance_payment_is_due = models.DateField(blank=True, null=True,
                                                          help_text='Date that the next insurance payment is due. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Date_Next_Insurance_Payment_Is_Due">Documentation</a>')

    date_of_court_appraisal = models.DateField(blank=True, null=True,
                                               help_text='Date that the court appraisal happened. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Date_of_Court_Appraisal">Documentation</a>')

    date_of_receiver_appointment = models.DateField(blank=True, null=True,
                                                    help_text='Date that the receiver was appointed. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Date_of_Receiver_Appointment">Documentation</a>')

    enforcement_description = models.TextField(blank=True, null=True,
                                               help_text='Comments or description of the stage of enforcement. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Enforcement_Description">Documentation</a>')

    fees_of_receivership = models.FloatField(blank=True, null=True,
                                             help_text='Annual fees charged by the receiver. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Fees_of_Receivership">Documentation</a>')

    first_auction_date = models.DateField(blank=True, null=True,
                                          help_text='Date that the first auction has been performed in order to sell the Property / Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.First_Auction_Date">Documentation</a>')

    funds_remitted_full_date = models.DateField(blank=True, null=True,
                                                help_text='Date that the funds were remitted fully. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Funds_Remitted_Full_Date">Documentation</a>')

    funds_remitted_partial_date = models.DateField(blank=True, null=True,
                                                   help_text='Date that the funds were remitted partially. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Funds_Remitted_Partial_Date">Documentation</a>')

    gross_sale_proceeds = models.FloatField(blank=True, null=True,
                                            help_text='Gross sale proceeds, i.e. sales proceeds and costs incurred from the disposal. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Gross_Sale_Proceeds">Documentation</a>')

    indicator_of_enforcement = models.BooleanField(blank=True, null=True,
                                                       help_text='Indicator as to whether the Enforcement process has been entered into by a Corporate or Private Individual Counterparty. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Indicator_of_Enforcement">Documentation</a>')

    indicator_of_receivership = models.BooleanField(blank=True, null=True,
                                                        help_text='Indicator as to whether the Corporate or Private Individual Counterparty is in Receivership. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Indicator_of_Receivership">Documentation</a>')

    insurance = models.BooleanField(blank=True, null=True,
                                        help_text='Indicator as to whether the receiver has insured the Property / Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Insurance">Documentation</a>')

    insurance_coverage_amount = models.FloatField(blank=True, null=True,
                                                  help_text='Amount that the insurance covers. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Insurance_Coverage_Amount">Documentation</a>')

    insurance_provider = models.TextField(blank=True, null=True,
                                          help_text='Name of the insurance provider. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Insurance_Provider">Documentation</a>')

    jurisdiction_of_court = models.TextField(blank=True, null=True,
                                             help_text='Location of the court where the case is being heard in. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Jurisdiction_of_Court">Documentation</a>')

    last_auction_date = models.DateField(blank=True, null=True,
                                         help_text='Date that the last auction was performed in order to sell the Property / Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Last_Auction_Date">Documentation</a>')

    name_of_legal_firm = models.TextField(blank=True, null=True,
                                          help_text='Name of legal firm acting on behalf of the Institution. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Name_of_Legal_Firm">Documentation</a>')

    name_of_receiver = models.TextField(blank=True, null=True,
                                        help_text='Name of the receiver appointed. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Name_of_Receiver">Documentation</a>')

    net_sale_proceeds = models.FloatField(blank=True, null=True,
                                          help_text='Net sale proceeds. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Net_Sale_Proceeds">Documentation</a>')

    next_auction_date = models.DateField(blank=True, null=True,
                                         help_text='Date that the next intended auction has been performed in order to sell the Property / Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Next_Auction_Date">Documentation</a>')

    number_of_failed_auctions = models.FloatField(blank=True, null=True,
                                                  help_text='Number of failed previous auctions for the Property / Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Number_of_Failed_Auctions">Documentation</a>')

    offer_price = models.FloatField(blank=True, null=True,
                                    help_text='The highest price offered by potential buyers. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Offer_Price">Documentation</a>')

    on_market_offer_date = models.DateField(blank=True, null=True,
                                            help_text='On market offer date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.On_Market_Offer_Date">Documentation</a>')

    on_market_price = models.FloatField(blank=True, null=True,
                                        help_text='Price of the Property / Collateral for which it is on the market. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.On_Market_Price">Documentation</a>')

    other_ongoing_enforcement_proceedings = models.TextField(blank=True, null=True,
                                                             help_text='Further comments / details if there is other proceedings in place. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Other_ongoing_enforcement_proceedings">Documentation</a>')

    prepare_property_for_sale_date = models.DateField(blank=True, null=True,
                                                      help_text='Prepare property for sale date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Prepare_Property_for_Sale_Date">Documentation</a>')

    property_on_market_date = models.DateField(blank=True, null=True,
                                               help_text='Property on market date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Property_on_Market_Date">Documentation</a>')

    sale_agreed_date = models.DateField(blank=True, null=True,
                                        help_text='Sale agreed date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Sale_Agreed_Date">Documentation</a>')

    sale_agreed_price = models.FloatField(blank=True, null=True,
                                          help_text='Agreed price for the disposal of the Property / Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Sale_Agreed_Price">Documentation</a>')

    sold_date = models.DateField(blank=True, null=True,
                                 help_text='Sold date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Enforcement.Sold_Date">Documentation</a>')

    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.enforcement_identifier

    def get_absolute_url(self):
        return reverse('npl_portfolio:Enforcement_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Enforcement"
        verbose_name_plural = "Enforcements"
