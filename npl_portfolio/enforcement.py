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

from npl_portfolio.counterparty import Counterparty
from npl_portfolio.eba_field_helpers import mandatory_help, recommended_help, legacy_help
from npl_portfolio.enforcement_choices import *
from npl_portfolio.non_property_collateral import NonPropertyCollateral
from npl_portfolio.property_collateral import PropertyCollateral


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
                                             help_text=mandatory_help('4.00', "Institution's internal identifier to uniquely identify each protection (collateral or guarantee) subject to enforcement."))

    #
    # FOREIGN KEYS (Template 2 — Relationship)
    #

    property_collateral_identifier = models.ForeignKey(PropertyCollateral, on_delete=models.CASCADE, null=True,
                                                       blank=True,
                                                       help_text=mandatory_help('2.03', "Institution's internal identifier of the property collateral subject to enforcement."))

    non_property_collateral_identifier = models.ForeignKey(NonPropertyCollateral, on_delete=models.CASCADE, null=True,
                                                           blank=True,
                                                           help_text=mandatory_help('2.03', "Institution's internal identifier of the non-property collateral subject to enforcement."))

    counterparty_identifier = models.ForeignKey(Counterparty, on_delete=models.CASCADE, null=True, blank=True,
                                                help_text=mandatory_help('2.00', "Institution's internal identifier of the counterparty linked to this enforcement."))

    #
    # EBA ITS 2023/2083 — MANDATORY FIELDS (Template 4)
    #

    jurisdiction_of_court = models.TextField(blank=True, null=True,
                                             help_text=mandatory_help('4.31', "Country of the court responsible for execution of the enforcement process, per ISO 3166 ALPHA-2. Applicable when 'yes' is selected in 'Enforcement status'."))

    court_appraisal_amount = models.FloatField(blank=True, null=True,
                                               help_text=mandatory_help('4.34', "Court appraisal amount of the collateral. Applicable when 'yes' is selected in 'Enforcement status'."))

    date_of_court_appraisal = models.DateField(blank=True, null=True,
                                               help_text=mandatory_help('4.35', "Date that the court appraisal happened. Applicable if a court appraisal has occurred when 'yes' is selected in 'Enforcement status'."))

    sale_agreed_price = models.FloatField(blank=True, null=True,
                                          help_text=mandatory_help('4.37', "Agreed price for the disposal of the collateral. Applicable when 'yes' is selected in 'Enforcement status'."))

    next_auction_date = models.DateField(blank=True, null=True,
                                         help_text=mandatory_help('4.38', "Date of the next intended auction to sell the collateral. Applicable when 'yes' is selected in 'Enforcement status'."))

    court_auction_reserve_price_for_next_auction = models.FloatField(blank=True, null=True,
                                                                     help_text=mandatory_help('4.39', "Court set reserve price for next auction — minimum price required by the court. Applicable when 'yes' is selected in 'Enforcement status'."))

    last_auction_date = models.DateField(blank=True, null=True,
                                         help_text=mandatory_help('4.40', "Date that the last auction was performed to sell the collateral. Applicable when 'yes' is selected in 'Enforcement status'."))

    #
    # EBA ITS 2023/2083 — RECOMMENDED FIELDS (Template 4)
    #

    currency_of_enforcement = models.TextField(blank=True, null=True,
                                               help_text=recommended_help('4.32', "Currency that the enforcement items are expressed in, per ISO 4217. Applicable when 'yes' is selected in 'Enforcement status'."))

    indicator_of_enforcement = models.BooleanField(blank=True, null=True,
                                                   help_text=recommended_help('4.33', "Indicator as to whether the enforcement process has been entered into by the corporate or private individual counterparty. Applicable when 'yes' is selected in 'Enforcement status'."))

    cash_in_court = models.FloatField(blank=True, null=True,
                                      help_text=recommended_help('4.36', "Cash deposited in court from sold assets awaiting disbursement to the institution."))

    court_auction_reserve_price_for_last_auction = models.FloatField(blank=True, null=True,
                                                                     help_text=recommended_help('4.41', "Court set reserve price for last auction — minimum price required by the court."))

    number_of_failed_auctions = models.FloatField(blank=True, null=True,
                                                  help_text=recommended_help('4.42', "Number of failed previous auctions for the collateral. Applicable when 'yes' is selected in 'Enforcement status'."))

    #
    # LEGACY DATA PROPERTIES (pre-2023 EBA draft — not in EU 2023/2083)
    #

    amount_of_outstanding_liabilities = models.FloatField(blank=True, null=True,
                                                          help_text=legacy_help('Amount of accrued costs and fees paid by the receiver and to be invoiced to the institution.'))

    annual_insurance_payment = models.FloatField(blank=True, null=True,
                                                 help_text=legacy_help('Annual insurance payment to be paid by the receiver.'))

    contracted_date = models.DateField(blank=True, null=True,
                                       help_text=legacy_help('Contracted date.'))

    collateral_repossessed_date = models.DateField(blank=True, null=True,
                                                   help_text=legacy_help('Date that the collateral was repossessed.'))

    costs_accrued_to_buyer = models.FloatField(blank=True, null=True,
                                               help_text=legacy_help('Costs accrued to the buyer.'))

    costs_at_end_of_sale = models.FloatField(blank=True, null=True,
                                             help_text=legacy_help('Total costs accrued to the seller at end of sale process.'))

    court_auction_identifier = models.TextField(blank=True, null=True,
                                                help_text=legacy_help('Unique identifier for the auction process.'))

    court_auction_reserve_price_for_first_auction = models.FloatField(blank=True, null=True,
                                                                      help_text=legacy_help('Court set reserve price for first auction — minimum price required by the court.'))

    current_market_status = models.IntegerField(blank=True, null=True, choices=CURRENT_MARKET_STATUS_CHOICES,
                                                help_text=legacy_help('Current market status of the collateral at cut-off date.'))

    date_next_insurance_payment_is_due = models.DateField(blank=True, null=True,
                                                          help_text=legacy_help('Date that the next insurance payment is due.'))

    date_of_receiver_appointment = models.DateField(blank=True, null=True,
                                                    help_text=legacy_help('Date that the receiver was appointed.'))

    enforcement_description = models.TextField(blank=True, null=True,
                                               help_text=legacy_help('Comments or description of the stage of enforcement.'))

    fees_of_receivership = models.FloatField(blank=True, null=True,
                                             help_text=legacy_help('Annual fees charged by the receiver.'))

    first_auction_date = models.DateField(blank=True, null=True,
                                          help_text=legacy_help('Date that the first auction was performed to sell the collateral.'))

    funds_remitted_full_date = models.DateField(blank=True, null=True,
                                                help_text=legacy_help('Date that the funds were remitted fully.'))

    funds_remitted_partial_date = models.DateField(blank=True, null=True,
                                                   help_text=legacy_help('Date that the funds were remitted partially.'))

    gross_sale_proceeds = models.FloatField(blank=True, null=True,
                                            help_text=legacy_help('Gross sale proceeds including costs incurred from the disposal.'))

    indicator_of_receivership = models.BooleanField(blank=True, null=True,
                                                    help_text=legacy_help('Indicator as to whether the counterparty is in receivership.'))

    insurance = models.BooleanField(blank=True, null=True,
                                    help_text=legacy_help('Indicator as to whether the receiver has insured the collateral.'))

    insurance_coverage_amount = models.FloatField(blank=True, null=True,
                                                  help_text=legacy_help('Amount that the insurance covers.'))

    insurance_provider = models.TextField(blank=True, null=True,
                                          help_text=legacy_help('Name of the insurance provider.'))

    name_of_legal_firm = models.TextField(blank=True, null=True,
                                          help_text=legacy_help('Name of the legal firm acting on behalf of the institution.'))

    name_of_receiver = models.TextField(blank=True, null=True,
                                        help_text=legacy_help('Name of the receiver appointed.'))

    net_sale_proceeds = models.FloatField(blank=True, null=True,
                                          help_text=legacy_help('Net sale proceeds.'))

    offer_price = models.FloatField(blank=True, null=True,
                                    help_text=legacy_help('The highest price offered by potential buyers.'))

    on_market_offer_date = models.DateField(blank=True, null=True,
                                            help_text=legacy_help('Date the collateral was put on market with an offer price.'))

    on_market_price = models.FloatField(blank=True, null=True,
                                        help_text=legacy_help('Price of the collateral for which it is on the market.'))

    other_ongoing_enforcement_proceedings = models.TextField(blank=True, null=True,
                                                             help_text=legacy_help('Further comments / details if there are other proceedings in place.'))

    prepare_property_for_sale_date = models.DateField(blank=True, null=True,
                                                      help_text=legacy_help('Date that the property was prepared for sale.'))

    property_on_market_date = models.DateField(blank=True, null=True,
                                               help_text=legacy_help('Date that the property was put on the market.'))

    sale_agreed_date = models.DateField(blank=True, null=True,
                                        help_text=legacy_help('Date that the sale was agreed.'))

    sold_date = models.DateField(blank=True, null=True,
                                 help_text=legacy_help('Date that the collateral was sold.'))

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
