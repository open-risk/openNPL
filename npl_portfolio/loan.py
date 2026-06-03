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
from npl_portfolio.loan_choices import *


class Loan(models.Model):
    """
    The Loan model holds Loan Portfolio data conforming to the EBA NPL Template specification
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Loan_Table>`_

    .. note:: The EBA Templates make a distinction between instrument and contract. At present this is not fully implemented

    """

    #
    # IDENTIFICATION FIELDS
    #

    loan_identifier = models.TextField(blank=True, null=True,
                                       help_text=mandatory_help('3.01', 'Institution internal identifier for the loan. Cannot be reused for any other loan under the same or different loan agreement.'))

    instrument_identifier = models.TextField(blank=True, null=True,
                                             help_text=legacy_help('Institution internal identifier for the Loan part (sub-instrument level).'))

    #
    # FOREIGN KEYS
    #

    counterparty_identifier = models.ForeignKey(Counterparty, on_delete=models.CASCADE, null=True, blank=True,
                                                help_text=mandatory_help('2.00', "Institution's internal identifier to uniquely identify each counterparty linked to this loan."))

    snapshot_id = models.ForeignKey('PortfolioSnapshot', on_delete=models.CASCADE, null=True, blank=True,
                                    help_text=mandatory_help('3.00', 'Reference date of the data included in the EBA NPL templates.'))

    #
    # LEGACY DATA PROPERTIES (pre-2023 EBA draft — not in EU 2023/2083)
    #

    accounting_stages_of_asset_quality = models.IntegerField(blank=True, null=True,
                                                             choices=ACCOUNTING_STAGES_OF_ASSET_QUALITY_CHOICES,
                                                             help_text=legacy_help('Accounting stages of asset quality: IFRS Stage 1, IFRS Stage 2, IFRS Stage 3 (impaired), Fair Value Through P&L, Other Accounting Standard.'))

    accrued_interest_balance_off_book = models.BigIntegerField(blank=True, null=True,
                                                               help_text=legacy_help('Amount of interest accrued but not capitalised to the Loan, not recognised on the balance sheet.'))

    amortisation_type = models.IntegerField(blank=True, null=True, choices=AMORTISATION_TYPE_CHOICES,
                                            help_text=legacy_help('Amortisation type of the loan per the latest Loan Agreement (e.g. Full amortisation, part amortisation, final bullet, bespoke repayment).'))

    balance_at_default = models.BigIntegerField(blank=True, null=True,
                                                help_text=legacy_help('Balance of the Loan when it defaulted (CRR Art.178).'))

    capitalised_pastdue_amount = models.BigIntegerField(blank=True, null=True,
                                                        help_text=legacy_help('Total capitalised past-due balance as recognised on balance sheet at Cut-Off Date (interest and legal fees).'))

    channel_of_origination = models.IntegerField(blank=True, null=True, choices=CHANNEL_OF_ORIGINATION_CHOICES,
                                                 help_text=legacy_help('Channel through which the Loan was originated (e.g. Branch, Internet, Broker).'))

    chargeoff_date = models.DateField(blank=True, null=True,
                                      help_text=legacy_help('Date when the Loan went into charge-off.'))

    code_of_conduct = models.TextField(blank=True, null=True,
                                       help_text=legacy_help('Indicator as to whether the Loan is subject to a Code of Conduct.'))

    comments_on_code_of_conduct = models.TextField(blank=True, null=True,
                                                   help_text=legacy_help('Further comments / details on Code of Conduct.'))

    comments_on_covenant_waiver = models.TextField(blank=True, null=True,
                                                   help_text=legacy_help('Further comments / details on the covenant waiver.'))

    country_of_origination = models.TextField(blank=True, null=True,
                                              help_text=legacy_help('Country where the Loan was originated.'))

    covenant_waiver = models.TextField(blank=True, null=True,
                                       help_text=legacy_help('Indicator as to whether there has been a covenant waiver for any breaches of the Loan Agreement.'))

    current_covenant_levels = models.BigIntegerField(blank=True, null=True,
                                                     help_text=legacy_help('Current levels of covenants as at NPL Portfolio Cut-Off date.'))

    current_external_credit_rating = models.TextField(blank=True, null=True,
                                                      help_text=legacy_help('External credit rating issued for the Loan at Cut-Off Date.'))

    current_internal_credit_rating = models.TextField(blank=True, null=True,
                                                      help_text=legacy_help('Internal credit rating issued to the Loan at Cut-Off Date.'))

    current_reversion_interest_rate = models.FloatField(blank=True, null=True,
                                                        help_text=legacy_help('Current level of reversion interest rate per the Loan Agreement at Cut-Off Date.'))

    default_penalty_interest_margin = models.FloatField(blank=True, null=True,
                                                        help_text=legacy_help('Additional margin charged on the balance of the Loan in default per the Loan Agreement at Cut-Off Date.'))

    description_of_bespoke_repayment = models.TextField(blank=True, null=True,
                                                        help_text=legacy_help('Description of the bespoke repayment profile when "Bespoke Repayment" is selected in "Amortisation Type".'))

    description_of_original_interest_rate_type = models.TextField(blank=True, null=True,
                                                                  help_text=legacy_help('Description of original interest rate type when "Mixed" is selected in "Original Interest Rate Type".'))

    description_of_relevant_schemes = models.TextField(blank=True, null=True,
                                                       help_text=legacy_help('Description of the relevant scheme if YES is selected in field "Relevant Schemes".'))

    details_of_origination_channel = models.TextField(blank=True, null=True,
                                                      help_text=legacy_help('Description of the origination channel when "Broker" or "Other" is selected in "Channel of Origination".'))

    early_redemption_penalty = models.FloatField(blank=True, null=True,
                                                 help_text=legacy_help('Additional charge on early redemption per the Loan Agreement at Cut-Off Date.'))

    end_date_of_current_fixed_interest_period = models.DateField(blank=True, null=True,
                                                                 help_text=legacy_help('Date that the current fixed interest period ends per the Loan Agreement at Cut-Off Date.'))

    end_date_of_interest_grace_period = models.DateField(blank=True, null=True,
                                                         help_text=legacy_help('Date that the interest payment postponement ends per the Loan Agreement at Cut-Off Date.'))

    end_date_of_interest_only_period = models.DateField(blank=True, null=True,
                                                        help_text=legacy_help('Date that the interest-only repayment period ends per the current Loan Agreement at Cut-Off Date.'))

    end_date_of_principal_grace_period = models.DateField(blank=True, null=True,
                                                          help_text=legacy_help('Date that the principal payment postponement ends per the Loan Agreement at Cut-Off Date.'))

    end_date_of_subsidy = models.DateField(blank=True, null=True,
                                           help_text=legacy_help('Date that the current subsidy ends.'))

    external_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                             help_text=legacy_help('External credit rating issued to the Loan at the point of origination.'))

    final_bullet_repayment = models.BigIntegerField(blank=True, null=True,
                                                    help_text=legacy_help('Total amount of principal repayment to be paid at the maturity date of the loan.'))

    interest_cap_rate = models.FloatField(blank=True, null=True,
                                          help_text=legacy_help('Maximum interest rate chargeable on the Loan as specified in the current Loan Agreement.'))

    interest_floor_rate = models.FloatField(blank=True, null=True,
                                            help_text=legacy_help('Minimum interest rate chargeable on the Loan as specified in the current Loan Agreement.'))

    interest_payment_frequency = models.IntegerField(blank=True, null=True, choices=INTEREST_PAYMENT_FREQUENCY_CHOICES,
                                                     help_text=legacy_help('Frequency of interest payments based on the current Loan Agreement at Cut-Off Date.'))

    interest_reset_interval = models.BigIntegerField(blank=True, null=True,
                                                     help_text=legacy_help('Number of months between two interest reset dates per the Loan Agreement at Cut-Off Date.'))

    internal_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                             help_text=legacy_help('Internal credit rating issued to the Loan at the point of origination.'))

    last_covenant_test_date = models.DateField(blank=True, null=True,
                                               help_text=legacy_help('Date that the covenant levels were last tested by the institution.'))

    last_interest_reset_date = models.DateField(blank=True, null=True,
                                                help_text=legacy_help('Date that the last interest reset event happened.'))

    legal_balance_at_chargeoff_date = models.BigIntegerField(blank=True, null=True,
                                                             help_text=legacy_help('Total claim amount when the Loan went into charge-off.'))

    loan_commitment = models.BigIntegerField(blank=True, null=True,
                                             help_text=legacy_help('Total available credit extended as at the NPL Portfolio Cut-Off Date.'))

    loan_covenants = models.IntegerField(blank=True, null=True, choices=LOAN_COVENANTS_CHOICES,
                                         help_text=legacy_help('Covenants as agreed in the current Loan Agreement at Cut-Off Date (LTV, ICR, DSCR etc.).'))

    loan_purpose = models.IntegerField(blank=True, null=True, choices=LOAN_PURPOSE_CHOICES,
                                       help_text=legacy_help('Ultimate financing purpose of the Loan (e.g. Residential real estate purchase, Commercial real estate, Working capital).'))

    loan_status = models.IntegerField(blank=True, null=True, choices=LOAN_STATUS_CHOICES,
                                      help_text=legacy_help('Loan status (e.g. performing, non-performing).'))

    marp_applicable = models.BooleanField(blank=True, null=True,
                                          help_text=legacy_help('Indicator as to whether the Institution operates a Mortgage Arrears Resolution Process (MARP).'))

    marp_entry = models.DateField(blank=True, null=True,
                                  help_text=legacy_help('Date loan entered current MARP status.'))

    marp_status = models.IntegerField(blank=True, null=True, choices=MARP_STATUS_CHOICES,
                                      help_text=legacy_help('Status of the current Mortgage Arrears Resolution Process.'))

    next_interest_reset_date = models.DateField(blank=True, null=True,
                                                help_text=legacy_help('Date that the next interest reset event is scheduled.'))

    next_interest_scheduled_repayment_amount = models.BigIntegerField(blank=True, null=True,
                                                                      help_text=legacy_help('Amount of next scheduled interest repayment at Cut-Off Date.'))

    next_interest_scheduled_repayment_date = models.DateField(blank=True, null=True,
                                                              help_text=legacy_help('Date that the next interest repayment is due at Cut-Off Date.'))

    next_principal_scheduled_repayment_amount = models.BigIntegerField(blank=True, null=True,
                                                                       help_text=legacy_help('Amount of next scheduled principal repayment at Cut-Off Date.'))

    next_principal_scheduled_repayment_date = models.DateField(blank=True, null=True,
                                                               help_text=legacy_help('Date that the next principal repayment is due at Cut-Off Date.'))

    nonperforming_reason = models.IntegerField(blank=True, null=True, choices=NONPERFORMING_REASON_CHOICES,
                                               help_text=legacy_help('Main reason for non-performing status (impaired, defaulted CRR Art.178, >90 DPD, unlikely to pay).'))

    number_of_pastdue_events = models.BigIntegerField(blank=True, null=True,
                                                      help_text=legacy_help('Number of times the Loan was previously categorised as past-due.'))

    original_interest_base_rate = models.FloatField(blank=True, null=True,
                                                    help_text=legacy_help('Original base rate of the Loan when "Variable" is selected in "Original Interest Rate Type".'))

    original_interest_margin = models.FloatField(blank=True, null=True,
                                                 help_text=legacy_help('Original margin above the base rate at loan origination.'))

    original_interest_rate = models.FloatField(blank=True, null=True,
                                               help_text=legacy_help('Original total interest rate of the Loan as stated in the Loan Agreement at origination.'))

    original_interest_rate_reference = models.IntegerField(blank=True, null=True,
                                                           choices=ORIGINAL_INTEREST_RATE_REFERENCE_CHOICES,
                                                           help_text=legacy_help('Original interest rate base/reference when "Variable" is selected in "Original Interest Rate Type".'))

    original_interest_rate_type = models.IntegerField(blank=True, null=True,
                                                      choices=ORIGINAL_INTEREST_RATE_TYPE_CHOICES,
                                                      help_text=legacy_help('Original interest rate type as per Loan Agreement at origination (Fixed / Variable / Mixed).'))

    original_maturity_date = models.DateField(blank=True, null=True,
                                              help_text=legacy_help('Original contractual maturity date of the Loan.'))

    origination_amount = models.BigIntegerField(blank=True, null=True,
                                                help_text=legacy_help('Loan amount advanced to the Borrower at origination.'))

    other_pastdue_amounts = models.BigIntegerField(blank=True, null=True,
                                                   help_text=legacy_help('Accumulated amount of other past-due amounts (e.g. fees) at Cut-Off Date.'))

    other_syndicate_counterparties = models.TextField(blank=True, null=True,
                                                      help_text=legacy_help('Other syndicate counterparties when "Yes" is selected in "Syndicated Loan".'))

    pastdue_interest_amount = models.BigIntegerField(blank=True, null=True,
                                                     help_text=legacy_help('Accumulated amount of past-due interest as recognised on balance sheet at Cut-Off Date.'))

    pastdue_penalty_interest_margin = models.FloatField(blank=True, null=True,
                                                        help_text=legacy_help('Additional margin charged on the past-due portion of the Loan per the Loan Agreement at Cut-Off Date.'))

    pastdue_principal_amount = models.BigIntegerField(blank=True, null=True,
                                                      help_text=legacy_help('Accumulated amount of past-due principal as recognised on balance sheet at Cut-Off Date.'))

    principal_payment_frequency = models.IntegerField(blank=True, null=True,
                                                      choices=PRINCIPAL_PAYMENT_FREQUENCY_CHOICES,
                                                      help_text=legacy_help('Frequency of principal payments based on the current Loan Agreement at Cut-Off Date.'))

    recourse_to_other_assets = models.BooleanField(blank=True, null=True,
                                                   help_text=legacy_help('Indicator as to whether the Institution has the legal right to access other assets of the Borrower.'))

    relevant_schemes = models.TextField(blank=True, null=True,
                                        help_text=legacy_help('Indicator as to whether the Loan is involved with any relevant schemes (e.g. Right to Buy Scheme in UK).'))

    source_of_current_external_credit_rating = models.TextField(blank=True, null=True,
                                                                help_text=legacy_help('Agency which provided the external credit rating at Cut-Off Date.'))

    source_of_external_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                                       help_text=legacy_help('Agency which provided the external credit rating at origination.'))

    specialised_product = models.TextField(blank=True, null=True,
                                           help_text=legacy_help('Indicator as to whether the Loan is a specialised product (e.g. Fractioned Loans in Italy).'))

    start_date_of_current_fixed_interest_period = models.DateField(blank=True, null=True,
                                                                   help_text=legacy_help('Date that the current fixed interest period started per the Loan Agreement at Cut-Off Date.'))

    start_date_of_interest_grace_period = models.DateField(blank=True, null=True,
                                                           help_text=legacy_help('Date that the interest payment postponement started per the Loan Agreement at Cut-Off Date.'))

    start_date_of_interest_only_period = models.DateField(blank=True, null=True,
                                                          help_text=legacy_help('Date that the interest-only repayment period started per the most recent Loan Agreement at Cut-Off Date.'))

    start_date_of_principal_grace_period = models.DateField(blank=True, null=True,
                                                            help_text=legacy_help('Date that the principal payment postponement started per the Loan Agreement at Cut-Off Date.'))

    start_date_of_subsidy = models.DateField(blank=True, null=True,
                                             help_text=legacy_help('Date that the current subsidy starts.'))

    subsidy = models.TextField(blank=True, null=True,
                               help_text=legacy_help('Indicator where contractual payments are subsidised by an external party.'))

    subsidy_amount = models.BigIntegerField(blank=True, null=True,
                                            help_text=legacy_help('Amount of the subsidy received.'))

    subsidy_provider = models.TextField(blank=True, null=True,
                                        help_text=legacy_help('Name of the external party who provided the subsidy.'))

    time_in_pastdue = models.BigIntegerField(blank=True, null=True,
                                             help_text=legacy_help('Total number of months the Loan has been in past-due in the past 12 months.'))

    total_balance = models.BigIntegerField(blank=True, null=True,
                                           help_text=legacy_help('Total unpaid balance: Principal Balance + Accrued Interest (On book) + Other Balances.'))

    total_pastdue_amount = models.BigIntegerField(blank=True, null=True,
                                                  help_text=legacy_help('Total past-due amount: Past-Due Principal + Past-Due Interest + Other Past-Due.'))

    trigger_levels_of_loan_covenants = models.BigIntegerField(blank=True, null=True,
                                                              help_text=legacy_help('Trigger levels of covenants as agreed in the Loan Agreement at Cut-Off Date.'))

    type_of_reversion_interest_rate = models.TextField(blank=True, null=True,
                                                       help_text=legacy_help('Type of reversion interest rate after the fixed interest period per the Loan Agreement at Cut-Off Date.'))

    #
    # EBA ITS 2023/2083 — MANDATORY FIELDS
    #

    date_of_origination = models.DateField(blank=True, null=True,
                                           help_text=mandatory_help('3.02', 'Date on which the contractual relationship originated (the date the contract became binding for all parties).'))

    governing_law_of_loan_agreement = models.TextField(blank=True, null=True,
                                                       help_text=mandatory_help('3.03', 'Jurisdiction governing the loan agreement, per ISO 3166 ALPHA-2. Does not necessarily correspond to the country where the loan was originated.'))

    asset_class = models.IntegerField(blank=True, null=True, choices=ASSET_CLASS_CHOICES,
                                      help_text=mandatory_help('3.05', 'Asset class of the loan per Article 2(1) of Commission Delegated Regulation (EU) 2020/1224 (e.g. Residential real estate, Commercial real estate, Corporate, Consumer).'))

    product_type = models.IntegerField(blank=True, null=True, choices=PRODUCT_TYPE_CHOICES,
                                       help_text=mandatory_help('3.06', 'Classification of the loan according to the type of contractual terms agreed between the parties (e.g. Overdraft, Credit card, Revolving credit, Financial lease, Other loans).'))

    loan_currency = models.TextField(blank=True, null=True,
                                     help_text=mandatory_help('3.08', 'Currency denomination of the Loan per ISO 4217.'))

    principal_balance = models.BigIntegerField(blank=True, null=True,
                                               help_text=mandatory_help('3.09', 'Outstanding principal amount as recognised on the balance sheet at Cut-Off Date. Excludes accrued interest and other balances.'))

    accrued_interest_balance_on_book = models.BigIntegerField(blank=True, null=True,
                                                              help_text=mandatory_help('3.10', 'Accrued interest on loans as recognised on the balance sheet at Cut-Off Date, per Reg. (EU) No 1071/2013.'))

    other_balances = models.BigIntegerField(blank=True, null=True,
                                            help_text=mandatory_help('3.11', 'Total other outstanding amounts on the balance sheet at Cut-Off Date (charges, commissions, fees not in principal or accrued interest).'))

    legal_balance = models.BigIntegerField(blank=True, null=True,
                                           help_text=mandatory_help('3.12', 'Total claim amount including on-balance sheet exposures, off-balance sheet exposures and penalty interests the lender is entitled to receive at Cut-Off Date.'))

    days_in_pastdue = models.BigIntegerField(blank=True, null=True,
                                             help_text=mandatory_help('3.13', 'Number of days the loan is currently past-due at Cut-Off Date. Zero for non-performing loans not past-due. Past-due per Annex V paragraph 96 of Reg. (EU) 2021/451.'))

    date_of_default = models.DateField(blank=True, null=True,
                                       help_text=mandatory_help('3.23', 'Date on which the default status occurred per Article 178 of Regulation (EU) No 575/2013. Not reported for non-performing loans not in default.'))

    #
    # EBA ITS 2023/2083 — RECOMMENDED FIELDS
    #

    current_maturity_date = models.DateField(blank=True, null=True,
                                             help_text=recommended_help('3.07', 'Contractual maturity date of the Loan at Cut-Off Date, including any amendments and forbearance measures. Required only when Days in Past-Due ≤ 365.'))

    current_interest_rate = models.FloatField(blank=True, null=True,
                                              help_text=recommended_help('3.14', 'Annualised agreed interest rate per Reg. (EU) No 1072/2013 (ECB/2013/34), applicable at Cut-Off Date including any forbearance. Required only when Days in Past-Due ≤ 365.'))

    current_interest_rate_type = models.IntegerField(blank=True, null=True, choices=CURRENT_INTEREST_RATE_TYPE_CHOICES,
                                                     help_text=recommended_help('3.15', 'Classification of loan by base rate for the interest rate (Fixed, Variable, Mixed). Applicable at Cut-Off Date including forbearance. Required only when Days in Past-Due ≤ 365.'))

    description_of_current_interest_rate_type = models.TextField(blank=True, null=True,
                                                                 help_text=recommended_help('3.16', 'Description of interest rate type when "Mixed" is selected in "Interest Rate Type". Required only when Days in Past-Due ≤ 365.'))

    current_interest_margin = models.FloatField(blank=True, null=True,
                                                help_text=recommended_help('3.17', 'Margin or spread (percentage) above the reference rate used for interest calculation in basis points. Applicable at Cut-Off Date. Required only when Days in Past-Due ≤ 365.'))

    current_interest_base_rate = models.FloatField(blank=True, null=True,
                                                   help_text=legacy_help('Reference rate used for the calculation of the actual interest rate. Applicable at Cut-Off Date when "Variable" is selected. Required only when Days in Past-Due ≤ 365.'))

    current_interest_rate_reference = models.IntegerField(blank=True, null=True,
                                                          choices=CURRENT_INTEREST_RATE_REFERENCE_CHOICES,
                                                          help_text=legacy_help('Current interest rate base/reference of the loan per Loan Agreement at Cut-Off Date when "Variable" is selected in "Interest Rate Type".'))

    last_payment_date = models.DateField(blank=True, null=True,
                                         help_text=recommended_help('3.21', 'Date that the last payment was made.'))

    last_payment_amount = models.BigIntegerField(blank=True, null=True,
                                                 help_text=recommended_help('3.22', 'Amount of last payment.'))

    syndicated_loan = models.BooleanField(blank=True, null=True,
                                          help_text=recommended_help('3.30', 'Indicator as to whether the loan is provided by a syndicate or consortium of two or more credit institutions (institution holds <100% of total loan).'))

    syndicated_portion = models.FloatField(blank=True, null=True,
                                           help_text=recommended_help('3.31', 'Percentage of the portion held by the institution. Applicable when "Yes" is selected in "Syndicated Loan".'))

    securitised = models.BooleanField(blank=True, null=True,
                                      help_text=recommended_help('3.32', 'Indicator as to whether the loan has been securitised or is within a covered bond pool.'))

    #
    # EBA TEMPLATE 3 ADDITIONAL FIELDS
    #

    joint_counterparties = models.IntegerField(
        blank=True, null=True, choices=JOINT_COUNTERPARTIES_CHOICES,
        help_text=mandatory_help(
            '3.04',
            'Number of counterparties who jointly owe under the loan and are jointly responsible for payments to the lender.'
        )
    )
    reference_rate = models.TextField(
        blank=True, null=True,
        help_text=recommended_help(
            '3.18',
            "Reference rate used for the calculation of the actual interest rate. Combination of the reference rate value and maturity value, applicable at the cut-off date when 'Variable' is selected in 'Interest Rate Type'. Required only when Days in Past-Due ≤ 365."
        )
    )
    interest_rate_reset_frequency = models.IntegerField(
        blank=True, null=True, choices=INTEREST_RATE_RESET_FREQUENCY_CHOICES,
        help_text=recommended_help(
            '3.19',
            "Frequency at which the interest rate is reset after the initial fixed-rate period. Applicable at Cut-Off Date including forbearance. Required only when Days in Past-Due ≤ 365."
        )
    )
    payment_frequency = models.IntegerField(
        blank=True, null=True, choices=PAYMENT_FREQUENCY_CHOICES,
        help_text=recommended_help(
            '3.20',
            "Frequency of payments due (principal or interest), i.e. number of months between payments. Based on the current loan agreement at Cut-Off Date. Required only when Days in Past-Due ≤ 365."
        )
    )
    loan_legal_status = models.IntegerField(
        blank=True, null=True, choices=LOAN_LEGAL_STATUS_CHOICES,
        help_text=mandatory_help(
            '3.24',
            'Indication of the loan legal status at Cut-Off Date (out of court settlement, legal proceedings, no action taken).'
        )
    )
    date_of_initiation_of_legal_proceedings = models.DateField(
        blank=True, null=True,
        help_text=mandatory_help(
            '3.25',
            "Date on which legal proceedings were initiated. Must be the most recent relevant date prior to Cut-Off Date. Required only when 'Loan legal status' = 'legal proceedings'."
        )
    )
    stage_reached_in_legal_proceedings = models.JSONField(
        blank=True, null=True, default=list,
        help_text=mandatory_help(
            '3.26',
            "Indication of how advanced the legal procedure has become. Multiple selections allowed: (a) Initial stage; (b) Proof of claim filed; (c) Notice of intention to sell secured assets; (d) Distribution made to seller; (e) Notice of end of procedure. Required only when 'Loan legal status' = 'legal proceedings'."
        )
    )
    jurisdiction_of_court = models.TextField(
        blank=True, null=True,
        help_text=mandatory_help(
            '3.27',
            'Location of the court where the court case is being heard, per ISO 3166 ALPHA-2. Required only when a court case has been initiated.'
        )
    )
    date_of_obtaining_order_for_possession = models.DateField(
        blank=True, null=True,
        help_text=recommended_help(
            '3.28',
            'Date that the order for possession is granted by the court. Required only when an order for possession has been granted.'
        )
    )
    statute_of_limitations_date = models.DateField(
        blank=True, null=True,
        help_text=mandatory_help(
            '3.29',
            'Date when the loan expires and legal proceedings cannot be undertaken. Required only when applicable under the governing law and legal status of the loan.'
        )
    )
    lease_agreement = models.BooleanField(
        blank=True, null=True,
        help_text=mandatory_help(
            '3.33',
            'Indicator as to whether the credit agreement contains a lease.'
        )
    )
    start_date_of_lease = models.DateField(
        blank=True, null=True,
        help_text=recommended_help(
            '3.34',
            "Date that the current lease starts. Required when 'yes' is selected in 'Lease agreement'."
        )
    )
    end_date_of_lease = models.DateField(
        blank=True, null=True,
        help_text=recommended_help(
            '3.35',
            "Date that the current lease ends. Required when 'yes' is selected in 'Lease agreement'."
        )
    )
    lease_break_option = models.TextField(
        blank=True, null=True,
        help_text=recommended_help(
            '3.36',
            "Details of any lease break clause(s). Required when 'yes' is selected in 'Lease agreement'."
        )
    )
    type_of_lease = models.IntegerField(
        blank=True, null=True, choices=TYPE_OF_LEASE_CHOICES,
        help_text=recommended_help(
            '3.37',
            "Type of the lease agreement with the counterparty. Required when 'yes' is selected in 'Lease agreement'."
        )
    )
    forbearance_measure = models.BooleanField(
        blank=True, null=True,
        help_text=mandatory_help(
            '3.38',
            'Indicator as to whether forbearance measures are currently applied to the loan at Cut-Off Date.'
        )
    )

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.loan_identifier

    def get_absolute_url(self):
        return reverse('npl_portfolio:loan_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
