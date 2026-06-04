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

from npl_portfolio.eba_field_helpers import mandatory_help, recommended_help, legacy_help
from npl_portfolio.loan import Loan
from npl_portfolio.non_property_collateral_choices import *


class NonPropertyCollateral(models.Model):
    """
    The NonPropertyCollateral model holds Non-Property Collateral data conforming to the EBA NPL Template specification
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Non-Property_Collateral_Table>`_

    """

    #
    # IDENTIFICATION FIELDS
    #

    protection_identifier = models.TextField(blank=True, null=True,
                                             help_text=mandatory_help('4.00', "Institution's internal identifier to uniquely identify each protection (collateral or guarantee) used to secure the loan."))

    #
    # FOREIGN KEYS (Template 2 — Relationship)
    #

    loan_identifier = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True,
                                        help_text=mandatory_help('2.01', "Institution's internal identifier of the loan secured by this non-property collateral."))

    #
    # EBA ITS 2023/2083 — MANDATORY FIELDS (Template 4)
    #

    collateral_type = models.IntegerField(blank=True, null=True, choices=COLLATERAL_TYPE_CHOICES,
                                          help_text=mandatory_help('4.02', "Type of movable property, other collateral or guarantee (e.g. vehicles, industrial equipment, financial guarantees, equity and debt securities)."))

    currency_of_collateral = models.TextField(blank=True, null=True,
                                              help_text=mandatory_help('4.18', "Currency that the valuation and cash flows related to the collateral or guarantee are expressed in, per ISO 4217."))

    latest_valuation_amount = models.FloatField(blank=True, null=True,
                                                help_text=mandatory_help('4.19', "Value of the collateral as established following the chosen internal valuation approach when last assessed at or prior to Cut-Off Date, without regulatory haircuts."))

    date_of_latest_valuation = models.DateField(
        blank=True, null=True,
        help_text=mandatory_help('4.20', "Date that the latest internal valuation took place at or prior to Cut-Off Date.")
    )

    # --- 4.21: Mandatory ---
    type_of_appraisal_amount_internal = models.IntegerField(
        blank=True, null=True,
        choices=TYPE_OF_APPRAISAL_AMOUNT_CHOICES,
        help_text=mandatory_help('4.21',
            "Type of appraisal amount for the latest internal valuation "
            "(market value, liquidation value, book value, other).")
    )

    # --- 4.23: Mandatory ---
    latest_external_valuation_amount = models.FloatField(
        blank=True, null=True,
        help_text=mandatory_help('4.23',
            "Value of the collateral as established following the chosen "
            "external valuation approach when last assessed at or prior to "
            "Cut-Off Date, without regulatory haircuts.")
    )

    # --- 4.24: Mandatory ---
    date_of_latest_external_valuation = models.DateField(
        blank=True, null=True,
        help_text=mandatory_help('4.24',
            "Date that the latest external valuation took place at or prior "
            "to Cut-Off Date.")
    )

    # --- 4.25: Mandatory ---
    type_of_appraisal_amount_external = models.IntegerField(
        blank=True, null=True,
        choices=TYPE_OF_APPRAISAL_AMOUNT_CHOICES,
        help_text=mandatory_help('4.25',
            "Type of appraisal amount for the latest external valuation "
            "(market value, liquidation value, book value, other).")
    )

    # --- 4.26: Recommended ---
    type_of_latest_external_valuation = models.IntegerField(
        blank=True, null=True,
        choices=TYPE_OF_LATEST_VALUATION_CHOICES,
        help_text=recommended_help('4.26',
            "Type of the latest external valuation (e.g. Full Appraisal, "
            "Drive-by, Automated Valuation Model, Desktop, Purchase Price).")
    )

    type_of_latest_valuation = models.IntegerField(blank=True, null=True, choices=TYPE_OF_LATEST_VALUATION_CHOICES,
                                                   help_text=recommended_help('4.22', "Type of the latest internal valuation (e.g. Full Appraisal, Drive-by, Automated Valuation Model, Desktop, Purchase Price)."))

    guarantee_amount = models.FloatField(blank=True, null=True,
                                         help_text=mandatory_help('4.27', "Maximum amount of the guarantee per paragraph 119 of Annex V Part 2 to Reg. (EU) 2021/451. Applicable when 'Financial Guarantees' is selected in 'Collateral Type'."))

    enforcement_status = models.BooleanField(blank=True, null=True,
                                             help_text=mandatory_help('4.29', "Indicator as to whether the collateral has entered into the enforcement process at Cut-Off Date."))

    enforcement_status_third_parties = models.BooleanField(blank=True, null=True,
                                                           help_text=recommended_help('4.30', "Indicator as to whether any other secured creditors have taken steps to enforce security over the collateral at Cut-Off Date."))

    isin = models.TextField(blank=True, null=True,
                            help_text=recommended_help('4.28', "ISIN number per ISIN Holdings data. Applicable when 'Equity and debt Securities' is selected in 'Collateral Type'."))

    #
    # LEGACY DATA PROPERTIES (pre-2023 EBA draft — not in EU 2023/2083)
    #

    activation_of_guarantee = models.BooleanField(blank=True, null=True,
                                                  help_text=legacy_help('Indicator as to whether the guarantee has been activated when "Guarantee" is selected in "Collateral Type".'))

    collateral_insurance = models.BooleanField(blank=True, null=True,
                                               help_text=legacy_help('Indicator as to whether there is an insurance on the collateral.'))

    collateral_insurance_coverage_amount = models.FloatField(blank=True, null=True,
                                                             help_text=legacy_help('Amount that the collateral insurance covers.'))

    collateral_insurance_provider = models.TextField(blank=True, null=True,
                                                     help_text=legacy_help('Name of the collateral insurance provider.'))

    estimated_useful_life = models.IntegerField(blank=True, null=True,
                                                help_text=legacy_help('Estimated remaining useful life at cut-off date.'))

    configuration = models.TextField(blank=True, null=True,
                                     help_text=legacy_help('Specification and option list of the collateral.'))

    original_country_of_registration = models.TextField(blank=True, null=True,
                                                        help_text=legacy_help('Country that the collateral was originally registered in.'))

    current_country_of_registration = models.TextField(blank=True, null=True,
                                                       help_text=legacy_help('Country that the collateral is currently registered in at cut-off date.'))

    current_opex_and_overheads = models.FloatField(blank=True, null=True,
                                                   help_text=legacy_help('Current annual operational expenses and overheads of running the collateral at cut-off date.'))

    date_of_initial_valuation = models.DateField(blank=True, null=True,
                                                 help_text=legacy_help('Date at which the initial valuation was assessed.'))

    description = models.TextField(blank=True, null=True,
                                   help_text=legacy_help('Detailed description of the collateral.'))

    enforcement_description = models.TextField(blank=True, null=True,
                                               help_text=legacy_help('Comments/description of the stage of enforcement that the collateral is in at cut-off date.'))

    engine_size = models.FloatField(blank=True, null=True,
                                    help_text=legacy_help('Engine size (litres) of the collateral.'))

    initial_valuation_amount = models.FloatField(blank=True, null=True,
                                                 help_text=legacy_help('Value of the collateral assessed at loan origination.'))

    initial_residual_value = models.FloatField(blank=True, null=True,
                                               help_text=legacy_help('Estimated residual value of the collateral at loan origination (how much it will be worth at end of loan term).'))

    date_of_the_latest_residual_valuation = models.DateField(blank=True, null=True,
                                                             help_text=legacy_help('Date that the latest residual value of the collateral was assessed.'))

    initial_residual_valuation_date = models.DateField(blank=True, null=True,
                                                       help_text=legacy_help('Date at which the initial residual value of the collateral was assessed.'))

    latest_residual_value = models.FloatField(blank=True, null=True,
                                              help_text=legacy_help('Estimated residual value of the collateral when last assessed.'))

    legal_owner = models.TextField(blank=True, null=True,
                                   help_text=legacy_help('Legal owner of the collateral.'))

    manufacturer_of_collateral = models.TextField(blank=True, null=True,
                                                  help_text=legacy_help('Name of the manufacturer of the collateral.'))

    name_or_model_of_collateral = models.TextField(blank=True, null=True,
                                                   help_text=legacy_help('Name/model of the collateral.'))

    new_or_used = models.IntegerField(blank=True, null=True, choices=NEW_OR_USED_CHOICES,
                                      help_text=legacy_help('Condition of the collateral at loan origination.'))

    registration_number = models.TextField(blank=True, null=True,
                                           help_text=legacy_help('Registration number of the collateral.'))

    type_of_initial_valuation = models.IntegerField(blank=True, null=True, choices=TYPE_OF_INITIAL_VALUATION_CHOICES,
                                                    help_text=legacy_help('Type of the initial valuation.'))

    type_of_legal_owner = models.IntegerField(blank=True, null=True, choices=TYPE_OF_LEGAL_OWNER_CHOICES,
                                              help_text=legacy_help('Type of the legal owner (Private Individual, Listed Corporate, Unlisted Corporate, Partnership).'))

    asset_purchase_obligation = models.BooleanField(blank=True, null=True,
                                                    help_text=legacy_help('Indicator as to whether there is an obligation for the borrower to purchase the collateral at the end of the lease.'))

    option_to_buy_price = models.FloatField(blank=True, null=True,
                                            help_text=legacy_help('Amount the borrower will pay at the end of the lease to take ownership of the collateral.'))

    year_of_manufacture = models.DateField(blank=True, null=True,
                                           help_text=legacy_help('Year that the collateral was manufactured/first sold.'))

    year_of_registration = models.DateField(blank=True, null=True,
                                            help_text=legacy_help('Year that the collateral was registered.'))

    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.protection_identifier)

    def get_absolute_url(self):
        return reverse('npl_portfolio:non_property_collateral_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Non-Property Collateral"
        verbose_name_plural = "Non-Property Collateral"
