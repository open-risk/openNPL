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

from npl_portfolio.non_property_collateral_choices import *
from npl_portfolio.loan import Loan


class NonPropertyCollateral(models.Model):
    """
    The NonPropertyCollateral model holds Non-Property Collateral data conforming to the EBA NPL Template specification
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Non-Property_Collateral_Table>`_

    """

    #
    # IDENTIFICATION FIELDS
    #

    protection_identifier = models.TextField(blank=True, null=True,
                                             help_text='Institution internal identifier for the Non-Property Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.14.0.Protection_identifier">Documentation</a>')

    #
    # FOREIGN KEYS
    #

    loan_identifier = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True)

    #
    # DATA PROPERTIES
    #

    activation_of_guarantee = models.BooleanField(blank=True, null=True,
                                                      help_text='Indicator as to whether the guarantee has been activated when "Guarantee" is selected in field "Collateral Type". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Activation_of_Guarantee">Documentation</a>')

    collateral_insurance = models.BooleanField(blank=True, null=True,
                                                   help_text='Indicator as to whether there is an insurance on the Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Collateral_Insurance">Documentation</a>')

    collateral_insurance_coverage_amount = models.FloatField(blank=True, null=True,
                                                             help_text='Amount that the collateral insurance covers. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Collateral_Insurance_Coverage_Amount">Documentation</a>')

    collateral_insurance_provider = models.TextField(blank=True, null=True,
                                                     help_text='Name of the collateral insurance provider. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Collateral_Insurance_Provider">Documentation</a>')

    collateral_type = models.IntegerField(blank=True, null=True, choices=COLLATERAL_TYPE_CHOICES,
                                          help_text='Physical type of the Collateral, e.g. Guarantee and Machinery. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Collateral_Type">Documentation</a>')

    estimated_useful_life = models.IntegerField(blank=True, null=True,
                                                help_text='Estimated remaining useful life as at cut-off date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty_Collateral.Estimated_Useful_Life">Documentation</a>')

    configuration = models.TextField(blank=True, null=True,
                                     help_text='Specification and option list of the Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty_Collateral.Configuration">Documentation</a>')

    original_country_of_registration = models.TextField(blank=True, null=True,
                                                        help_text='Country that the Collateral was originally registered in. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty_Collateral.Original_Country_of_Registration">Documentation</a>')

    current_country_of_registration = models.TextField(blank=True, null=True,
                                                       help_text='Country that the Collateral is currently registered in as at cut-off date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty_Collateral.Current_Country_of_Registration">Documentation</a>')

    currency_of_collateral = models.TextField(blank=True, null=True,
                                              help_text='Currency that the valuation and cash flows related to the Collateral are expressed in. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Currency_of_Collateral">Documentation</a>')

    current_opex_and_overheads = models.FloatField(blank=True, null=True,
                                                   help_text='Current annual operational expenses and overheads of running the Collateral as at cut-off date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Current_Opex_And_Overheads">Documentation</a>')

    date_of_initial_valuation = models.DateField(blank=True, null=True,
                                                 help_text='Date at which the initial valuation was assessed. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.14.01.Date_of_Initial_Valuation">Documentation</a>')

    date_of_latest_valuation = models.DateField(blank=True, null=True,
                                                help_text='Date that the latest valuation took place. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Date_of_Latest_Valuation">Documentation</a>')

    description = models.TextField(blank=True, null=True,
                                   help_text='Detailed description of the collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Description">Documentation</a>')

    enforcement_description = models.TextField(blank=True, null=True,
                                               help_text='Comments/Description of the stage of Enforcement that the Property Collateral is in as at cut-off date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Enforcement_Description">Documentation</a>')

    enforcement_status = models.BooleanField(blank=True, null=True,
                                                 help_text='Status of the enforcement process that the Collateral is currently in as at cut-off date, e.g. if it is in receivership. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Enforcement_Status">Documentation</a>')

    enforcement_status_third_parties = models.BooleanField(blank=True, null=True,
                                                               help_text='Indicator as to whether any other secured creditors have taken steps to enforce security over the asset? (Y/N). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Enforcement_Status_Third_Parties">Documentation</a>')

    engine_size = models.FloatField(blank=True, null=True,
                                    help_text='Engine size (litres) of the Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.14.03.Engine_Size">Documentation</a>')

    guarantee_amount = models.FloatField(blank=True, null=True,
                                         help_text='Claim amount of the guarantee when "Guarantee" is selected in field "Collateral Type". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Guarantee_Amount">Documentation</a>')

    initial_valuation_amount = models.FloatField(blank=True, null=True,
                                                 help_text='Value of the Collateral assessed at loan origination. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Initial_Valuation_Amount">Documentation</a>')

    initial_residual_value = models.FloatField(blank=True, null=True,
                                               help_text='Estimated residual value of the Collateral at loan origination, residual value refers to how much the Collateral will be worth at end of the loan term . <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty_Collateral.Initial_Residual_Value">Documentation</a>')

    date_of_the_latest_residual_valuation = models.DateField(blank=True, null=True,
                                                             help_text='Date that the latest residual value of the Collateral was assessed, residual value refers to how much the Collateral will be worth at end of the loan term. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty_Collateral.Date_of_the_Latest_Residual_Valuation">Documentation</a>')

    initial_residual_valuation_date = models.DateField(blank=True, null=True,
                                                       help_text='Date at which the initial residual value of the Collateral was assessed, residual value refers to how much the Collateral will be worth at end of the loan term. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty_Collateral.Initial_Residual_Valuation_Date">Documentation</a>')

    latest_residual_value = models.FloatField(blank=True, null=True,
                                              help_text='Estimated residual value of the Collateral when last assessed, residual value refers to how much the Collateral will be worth at end of the loan term. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty_Collateral.Latest_Residual_Value">Documentation</a>')

    latest_valuation_amount = models.FloatField(blank=True, null=True,
                                                help_text='Value of the Collateral when last assessed. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Latest_Valuation_Amount">Documentation</a>')

    legal_owner = models.TextField(blank=True, null=True,
                                   help_text='Legal owner of the Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Legal_Owner">Documentation</a>')

    manufacturer_of_collateral = models.TextField(blank=True, null=True,
                                                  help_text='Name used to refer to the manufacturer of the Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Manufacturer_of_Collateral">Documentation</a>')

    name_or_model_of_collateral = models.TextField(blank=True, null=True,
                                                   help_text='Name / model of the Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Name_or_Model_of_Collateral">Documentation</a>')

    new_or_used = models.IntegerField(blank=True, null=True, choices=NEW_OR_USED_CHOICES,
                                      help_text='Condition of the Collateral at loan origination. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.New_Or_Used">Documentation</a>')

    registration_number = models.TextField(blank=True, null=True,
                                           help_text='Registration number of the Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Registration_Number">Documentation</a>')

    type_of_initial_valuation = models.IntegerField(blank=True, null=True, choices=TYPE_OF_INITIAL_VALUATION_CHOICES,
                                                    help_text='Type of the initial valuation. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Type_of_Initial_Valuation">Documentation</a>')

    type_of_latest_valuation = models.IntegerField(blank=True, null=True, choices=TYPE_OF_LATEST_VALUATION_CHOICES,
                                                   help_text='Type of the latest valuation for the Collateral, i.e. Full Appraisal, Drive-by, Automated Valuation Model, Indexed, Desktop, Managing / Estate Agent, Purchase Price, Hair Cut, Mark to market and Borrowers Valuation. <a class ="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Type_of_Latest_Valuation" > Documentation </a> ')

    type_of_legal_owner = models.IntegerField(blank=True, null=True, choices=TYPE_OF_LEGAL_OWNER_CHOICES,
                                              help_text='Type of the legal owner, i.e. Private Individual, Listed Corporate, Unlisted Corporate and Partnership. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Type_of_Legal_Owner">Documentation</a>')

    asset_purchase_obligation = models.BooleanField(blank=True, null=True,
                                                        help_text='Indicator as to whether there is an obligation for the Borrower to purchase the Collateral at the end of the lease. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty_Collateral.Asset_Purchase_Obligation">Documentation</a>')

    option_to_buy_price = models.FloatField(blank=True, null=True,
                                            help_text='Amount the Borrower will pay at the end of the lease in order to take ownership of the Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty_Collateral.Option_to_Buy_Price">Documentation</a>')

    year_of_manufacture = models.DateField(blank=True, null=True,
                                           help_text='Year that the Collateral was manufactured / first sold. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Year_of_Manufacture">Documentation</a>')

    year_of_registration = models.DateField(blank=True, null=True,
                                            help_text='Year that the Collateral was registered. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.NonProperty Collateral.Year_of_Registration">Documentation</a>')

    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.protection_identifier

    def get_absolute_url(self):
        return reverse('npl_portfolio:non_property_collateral_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Non-Property Collateral"
        verbose_name_plural = "Non-Property Collateral"
