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

from npl_portfolio.counterparty_choices import *
from npl_portfolio.counterparty_group import CounterpartyGroup
from npl_portfolio.eba_field_helpers import mandatory_help, recommended_help, legacy_help, deprecated_help
from npl_portfolio.models import PortfolioSnapshot, Portfolio


class Counterparty(models.Model):
    """
    The Counterparty model holds Counterparty data conforming to the EBA NPL Template specification
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Counterparty_Table>`_

    .. note:: The EBA Templates make a distinction between corporate borrowers and individual borrowers. The Counterparty model holds data for either type

    """

    #
    # IDENTIFICATION FIELDS
    #

    counterparty_identifier = models.TextField(blank=True, null=True,
                                               help_text=mandatory_help('1.02', 'Unique internal identifier for each counterparty. Cannot be reused for any other counterparty.'))

    # EBA NPL ITS 1.10 / 1.11 — National Identifier
    national_identifier = models.TextField(blank=True, null=True,
                                           help_text=mandatory_help('1.10', 'Unique identifier of the counterparty in the country of residence (e.g. tax code, national ID number). Mandatory for Corporate (1.10), recommended for Private Individual (1.11).'))

    # EBA NPL ITS 1.12 — Source of National Identifier
    source_of_national_identifier = models.IntegerField(blank=True, null=True,
                                                        choices=TYPE_OF_PERSONAL_IDENTITY_NUMBER_CHOICES,
                                                        help_text=mandatory_help('1.12', 'Type/source of the national identifier provided in field 1.10.'))

    # EBA NPL ITS 1.18 — Availability of e-mail address
    availability_of_email_address = models.BooleanField(blank=True, null=True,
                                                        help_text=recommended_help('1.18', 'Indicator whether the institution has an e-mail address for the counterparty.'))

    # EBA NPL ITS 1.19 — Availability of telephone number
    availability_of_telephone_number = models.BooleanField(blank=True, null=True,
                                                           help_text=recommended_help('1.19', 'Indicator whether the institution has a telephone number (mobile or landline) for the counterparty.'))

    #
    # EBA ITS 2023/2083 — PRIVATE INDIVIDUAL FIELDS
    #

    # EBA NPL ITS 1.07 — Date of Birth (Private Individual only)
    date_of_birth = models.DateField(blank=True, null=True,
                                     help_text=recommended_help('1.07', 'Date of birth of the private individual counterparty. Applicable to private individuals only.'))

    # EBA NPL ITS 1.08 — Residency of Counterparty (Private Individual, MANDATORY)
    residency_same_country_as_institution = models.BooleanField(blank=True, null=True,
                                                                help_text=mandatory_help('1.08', 'Indication whether the residency of the private individual counterparty is in the same country as the institution. Applicable to private individuals only.'))

    # EBA NPL ITS 1.09 — Counterparty Deceased (Private Individual only)
    counterparty_deceased = models.BooleanField(blank=True, null=True,
                                                help_text=recommended_help('1.09', 'Indication as to whether the private individual counterparty has passed away. Applicable to private individuals only.'))

    #
    # FOREIGN KEYS
    #

    # ATTN Promoted to Foreign Key
    counterparty_group_identifier = models.ForeignKey(CounterpartyGroup, on_delete=models.CASCADE, null=True,
                                                      blank=True)

    # Portfolio ID Foreign Key
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE, blank=True, null=True,
                                     help_text="The portfolio ID to which the Counterparty belongs (can be more than one)")

    # Snapshot ID  Foreign Key
    snapshot_id = models.ForeignKey(PortfolioSnapshot, on_delete=models.CASCADE, blank=True, null=True,
                                    help_text="The snapshot ID to which the Counterparty belongs")

    #
    # ADDITIONAL DATA PROPERTIES
    #

    borrower_type = models.IntegerField(blank=True, null=True,
                                        choices=BORROWER_TYPE_CHOICES,
                                        help_text=deprecated_help(
                                            'Classification of the borrower as Private Individual or Corporate.',
                                            reason='No EBA ITS 2023/2083 field. Borrower type is derived from Legal Type of Counterparty (field 1.06).'))

    #
    # EBA DATA PROPERTIES
    #

    address_of_registered_location = models.TextField(blank=True, null=True,
                                                      help_text=mandatory_help('1.14', "Counterparty's street address, including the street number."))

    annual_ebit = models.BigIntegerField(blank=True, null=True,
                                         help_text=recommended_help('1.30', 'Annual Earnings Before Interest and Tax (EBIT) of the corporate counterparty per latest financial statements.'))

    annual_revenue = models.BigIntegerField(blank=True, null=True,
                                            help_text=recommended_help('1.29', 'Annual sales volume net of all discounts and sales taxes (Annual Turnover) per Recommendation 2003/361/EC.'))

    basis_of_financial_statements = models.IntegerField(blank=True, null=True,
                                                        choices=BASIS_OF_FINANCIAL_STATEMENTS_CHOICES,
                                                        help_text=legacy_help('Financial reporting practice adopted by the Corporate Counterparty (IFRS, National GAAP, Not Available).'))

    business_description = models.TextField(blank=True, null=True,
                                            help_text=legacy_help('Description of the business operations of the Corporate Counterparty, providing more detail for field Industry Segment.'))

    cash_and_cash_equivalent_items = models.BigIntegerField(blank=True, null=True,
                                                            help_text=recommended_help('1.25', 'Carrying amount of cash and cash equivalent items per latest financial statements (IAS 7).'))

    city_of_registered_location = models.TextField(blank=True, null=True,
                                                   help_text=mandatory_help('1.15', "Counterparty's city, town or village."))

    comments_on_other_litigation_related_process = models.TextField(blank=True, null=True,
                                                                    help_text=legacy_help('Further comments / details if there is other litigation processes in place.'))

    commencement_date_of_insolvency_or_restructuring_proceedings = models.DateField(blank=True, null=True,
                                                                                    help_text=legacy_help('Date that the Counterparty commenced Insolvency / Restructuring Proceedings.'))

    contingent_obligations = models.TextField(blank=True, null=True,
                                              help_text=legacy_help('Indicator as to whether the Corporate Counterparty has contingent obligations which will be part of the sale.'))

    counterparty_role = models.IntegerField(blank=True, null=True, choices=COUNTERPARTY_ROLE_CHOICES,
                                            help_text=mandatory_help('1.05', 'Role of the counterparty: Protection Provider or Borrower.'))

    country_of_registered_location = models.TextField(blank=True, null=True,
                                                      help_text=mandatory_help('1.17', "Counterparty's country, per ISO 3166-1 alpha-2."))

    correspondence_address_of_appointed_insolvency_practitioner = models.TextField(blank=True, null=True,
                                                                                   help_text=legacy_help('Correspondence address of the appointed insolvency practitioner.'))

    insolvency_practitioner_reference = models.TextField(blank=True, null=True,
                                                         help_text=legacy_help('Reference number of the insolvency practitioner.'))

    proof_of_claim_filed_by_the_seller = models.BooleanField(blank=True, null=True,
                                                             help_text=legacy_help('Indicator whether proof of claim has been filed by the seller.'))

    distribution_made_to_the_seller = models.BooleanField(blank=True, null=True,
                                                          help_text=legacy_help('Indicator whether a distribution has been made to the seller.'))

    notice_for_procedure_termination = models.BooleanField(blank=True, null=True,
                                                           help_text=legacy_help('Indicator whether the notice of the end of the procedure has been given to the seller.'))

    cross_collateralisation_for_counterparty = models.IntegerField(blank=True, null=True,
                                                                   choices=CROSS_COLLATERALISATION_FOR_COUNTERPARTY_CHOICES,
                                                                   help_text=legacy_help('Indicator whether all/some of the loans held by the Counterparty are secured by all/some of the collaterals.'))

    cross_default_for_counterparty = models.IntegerField(blank=True, null=True,
                                                         choices=CROSS_DEFAULT_FOR_COUNTERPARTY_CHOICES,
                                                         help_text=legacy_help('Indicator whether contractual breach of any loan held by the Counterparty would trigger default of any other loan.'))

    currency_of_deposit = models.TextField(blank=True, null=True,
                                           help_text=legacy_help('Currency of the deposit held with the Institution.'))

    currency_of_financial_statements = models.TextField(blank=True, null=True,
                                                        help_text=recommended_help('1.22', 'Currency of the latest available financial statements, per ISO 4217.'))

    current_assets = models.BigIntegerField(blank=True, null=True,
                                            help_text=recommended_help('1.24', 'Carrying amount of current assets (excluding cash) per latest financial statements (IAS 1.60).'))

    current_external_credit_rating = models.TextField(blank=True, null=True,
                                                      help_text=legacy_help('External credit rating issued to the Corporate Counterparty at NPL Portfolio Cut-Off Date.'))

    current_internal_credit_rating = models.TextField(blank=True, null=True,
                                                      help_text=legacy_help('Internal credit rating issued to the Counterparty at the NPL Portfolio Cut-Off Date.'))

    date_of_appointment = models.DateField(blank=True, null=True,
                                           help_text=legacy_help('Date that the insolvency practitioner was appointed.'))

    date_of_external_demand_issuance = models.DateField(blank=True, null=True,
                                                        help_text=legacy_help('Date that a demand notice was sent by solicitors acting on behalf of the Institution.'))

    date_of_incorporation = models.DateField(blank=True, null=True,
                                             help_text=legacy_help('Date that the Corporate Counterparty was incorporated as a separate legal entity.'))

    date_of_internal_demand_issuance = models.DateField(blank=True, null=True,
                                                        help_text=legacy_help('Date that a demand notice was sent by the Institution itself.'))

    date_of_last_contact = models.DateField(blank=True, null=True,
                                            help_text=recommended_help('1.20', 'Most recent date of contact with the counterparty where a reply was received.'))

    date_of_latest_annual_financial_statements = models.DateField(blank=True, null=True,
                                                                  help_text=recommended_help('1.21', 'Date of the latest available financial statements.'))

    date_of_obtaining_order_for_possession = models.DateField(blank=True, null=True,
                                                              help_text=legacy_help('Date that the Order for Possession was granted by the court.'))

    date_when_reservation_of_rights_letter_was_issued = models.DateField(blank=True, null=True,
                                                                         help_text=legacy_help('Date that the Reservation of Rights Letter was issued by the Institution.'))

    deposit_balance_with_institution = models.BigIntegerField(blank=True, null=True,
                                                              help_text=legacy_help('Deposit amount the Counterparty holds with the Institution.'))

    description_of_contingent_obligations = models.TextField(blank=True, null=True,
                                                             help_text=legacy_help('Description of contingent obligations when Yes is selected in field Contingent Obligations.'))

    description_of_cross_collateralisation = models.TextField(blank=True, null=True,
                                                              help_text=legacy_help('Description of cross collateralisation when Partial is selected in field Cross Collateralisation for Counterparty.'))

    description_of_cross_default = models.TextField(blank=True, null=True,
                                                    help_text=legacy_help('Description of cross default when Partial is selected in field Cross Default for Counterparty.'))

    description_of_related_party = models.TextField(blank=True, null=True,
                                                    help_text=legacy_help('Further comments on the nature of the relation between the institution and the related party.'))

    eligibility_for_deposit_to_offset = models.TextField(blank=True, null=True,
                                                         help_text=legacy_help('Indicator whether the deposit held with the Institution can be used to pay down the loan.'))

    enterprise_size = models.IntegerField(blank=True, null=True, choices=ENTERPRISE_SIZE_CHOICES,
                                          help_text=legacy_help('Classification of the Corporate Counterparty by size: Micro, Small, Medium, Large.'))

    eviction_date = models.DateField(blank=True, null=True,
                                     help_text=legacy_help('Date that the Counterparty was evicted.'))

    external_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                             help_text=legacy_help('External credit rating issued to the Corporate Counterparty at the point of origination.'))

    financial_statements_type = models.IntegerField(blank=True, null=True, choices=FINANCIAL_STATEMENTS_TYPE_CHOICES,
                                                    help_text=legacy_help('Indicator whether financial statements are prepared at Consolidated or Counterparty level.'))

    financials_audited = models.TextField(blank=True, null=True,
                                          help_text=legacy_help('Indicator whether the financial statements have been audited.'))

    fixed_assets = models.BigIntegerField(blank=True, null=True,
                                          help_text=recommended_help('1.23', 'Carrying amount of fixed assets per latest financial statements (IAS 16).'))

    geographic_region_classification = models.IntegerField(blank=True, null=True,
                                                           choices=GEOGRAPHIC_REGION_CLASSIFICATION_CHOICES,
                                                           help_text=legacy_help('NUTS3 classification version used for Geographic Region of Registered Location.'))

    geographic_region_of_registered_location = models.TextField(blank=True, null=True,
                                                                help_text=legacy_help('Province or Region where the Corporate Counterparty is registered.'))

    indicator_of_counterparty_cooperation = models.TextField(blank=True, null=True,
                                                             help_text=legacy_help('Indicator whether the Corporate or Private Individual Counterparty is cooperative.'))

    industry_segment = models.TextField(blank=True, null=True,
                                        help_text=mandatory_help('1.04', 'Economic activity of the corporate counterparty per NACE rev.2 classification (Reg. EC 1893/2006).'))

    insolvency_practitioner_appointed = models.TextField(blank=True, null=True,
                                                         help_text=legacy_help('Indicator whether an insolvency practitioner has been appointed.'))

    internal_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                             help_text=legacy_help('Internal credit rating issued to the Counterparty at the point of origination.'))

    jurisdiction_of_court = models.TextField(blank=True, null=True,
                                             help_text=legacy_help('Location of the court where the case is being heard.'))

    legal_entity_identifier = models.TextField(blank=True, null=True,
                                               help_text=recommended_help('1.13', 'Legal entity identifier of the counterparty assigned per ISO 17442.'))

    legal_fees_accrued = models.BigIntegerField(blank=True, null=True,
                                                help_text=legacy_help('Total amount of legal fees accrued at the NPL Portfolio Cut-Off Date.'))

    legal_procedure_type = models.IntegerField(blank=True, null=True, choices=LEGAL_PROCEDURE_TYPE_CHOICES,
                                               help_text=legacy_help('Type of the insolvency process the Counterparty is currently in.'))

    description_of_legal_procedure_type = models.TextField(blank=True, null=True, choices=LEGAL_PROCEDURE_TYPE_CHOICES,
                                                           help_text=legacy_help('Description of the insolvency process type when Other is selected.'))

    legal_type_of_counterparty = models.IntegerField(blank=True, null=True, choices=LEGAL_TYPE_OF_COUNTERPARTY_CHOICES,
                                                     help_text=mandatory_help('1.06', 'Counterparty sector type: Non-financial corporations SMEs, Non-financial corporations other, or Households (per Annex V Reg. 2021/451).'))

    market_capitalisation = models.BigIntegerField(blank=True, null=True,
                                                   help_text=legacy_help('Market capitalisation of a listed Corporate Counterparty.'))

    name_of_counterparty = models.TextField(blank=True, null=True,
                                            help_text=mandatory_help('1.03', 'Full legal name of the counterparty.'))

    name_of_insolvency_practitioner = models.TextField(blank=True, null=True,
                                                       help_text=legacy_help('Name of the insolvency practitioner.'))

    name_of_insolvency_or_restructuring_proceedings = models.TextField(blank=True, null=True,
                                                                       help_text=mandatory_help('1.31', 'Name of any insolvency or restructuring proceedings to which the counterparty is subject.'))

    additional_name_of_insolvency_or_restructuring_proceedings = models.TextField(blank=True, null=True,
                                                                                  help_text=legacy_help('Additional name of insolvency or restructuring proceedings.'))

    net_assets = models.BigIntegerField(blank=True, null=True,
                                        help_text=legacy_help('Amount of net assets held by the Corporate Counterparty per latest financial statements.'))

    number_of_fte = models.BigIntegerField(blank=True, null=True,
                                           help_text=legacy_help('Number of full-time employees (or equivalent) at the last financial reporting date.'))

    number_of_joint_counterparties = models.BigIntegerField(blank=True, null=True,
                                                            help_text=legacy_help('Number of joint Counterparties who jointly own parts of the Loan.'))

    occupation_type = models.TextField(blank=True, null=True,
                                       help_text=legacy_help('Main occupation of the Private Individual Counterparty.'))

    occupation_description = models.TextField(blank=True, null=True,
                                              help_text=legacy_help('Description of the occupation of the Private Individual Counterparty.'))

    other_products_with_institution = models.TextField(blank=True, null=True,
                                                       help_text=legacy_help('Other products the Counterparty holds with the Institution not included in the NPL Portfolio.'))

    postcode_of_registered_location = models.TextField(blank=True, null=True,
                                                       help_text=mandatory_help('1.16', "Counterparty's postal code."))

    registration_number = models.TextField(blank=True, null=True,
                                           help_text=legacy_help('Company registration number per the country-specific registration office.'))

    related_party = models.TextField(blank=True, null=True,
                                     help_text=legacy_help('Indicator whether the Counterparty is a related party to the Institution.'))

    sheriff_or_bailiff_acquisition_date = models.DateField(blank=True, null=True,
                                                           help_text=legacy_help('Date that sheriff / bailiff was acquired by the court.'))

    source_of_current_external_credit_rating = models.TextField(blank=True, null=True,
                                                                help_text=legacy_help('Agency which provided the external credit rating at cut-off date.'))

    source_of_external_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                                       help_text=legacy_help('Agency which provided the external credit rating at origination.'))

    stage_reached_in_insolvency_or_restructuring_procedure = models.IntegerField(blank=True, null=True,
                                                                                 choices=STAGE_REACHED_IN_INSOLVENCY_OR_RESTRUCTURING_PROCEDURE_CHOICES,
                                                                                 help_text=mandatory_help('1.32', 'Categories describing the counterparty legal status in relation to solvency per national legal framework.'))

    additional_stage_reached_in_insolvency_procedure = models.TextField(blank=True, null=True,
                                                                        help_text=recommended_help('1.33', 'Description of the status of legal proceedings when Other legal measures is selected in field 1.32.'))

    total_assets = models.BigIntegerField(blank=True, null=True,
                                          help_text=recommended_help('1.26', 'Carrying amount of total assets per latest financial statements (IAS 1.9(a)).'))

    total_debt = models.BigIntegerField(blank=True, null=True,
                                        help_text=recommended_help('1.28', 'Carrying amount of total debt per latest financial statements (IAS 32.11).'))

    total_liabilities = models.BigIntegerField(blank=True, null=True,
                                               help_text=recommended_help('1.27', 'Carrying amount of total liabilities per latest financial statements (IAS 1.9(b)).'))

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.counterparty_identifier

    class Meta:
        verbose_name = "Counterparty"
        verbose_name_plural = "Counterparties"
        unique_together = [['portfolio_id', 'counterparty_identifier']]
