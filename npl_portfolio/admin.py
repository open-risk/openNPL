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


from django.contrib import admin

'''
The 8 Relations (Tables) of the EBA Portfolio Templates that are currently implemented

The Portfolio table is used to group obligor data into portfolios. The Portfolio_Snapshot table is used to group data into time snapshots.

.. note:: Lease, Swap and History Tables not implemented :github:issue:`21`. Relation tables between entities implemented differently (not normalized)

'''

from npl_portfolio.models import PortfolioSnapshot, Portfolio
from npl_portfolio.models import Counterparty, CounterpartyGroup
from npl_portfolio.models import Loan
from npl_portfolio.models import ExternalCollection, Enforcement
from npl_portfolio.models import NonPropertyCollateral, PropertyCollateral
from npl_portfolio.models import Forbearance
from npl_portfolio.models import HistoricalRepayment
from npl_portfolio.models import Mortgage


class PortfolioAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['name']
    list_display = ('name', 'creation_date', 'last_change_date')


class Portfolio_SnapshotAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['name']
    list_display = ('name', 'creation_date', 'cutoff_date')


class CounterpartyAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['counterparty_identifier']
    list_display = ('counterparty_identifier', 'name_of_counterparty', 'legal_type_of_counterparty',
                    'snapshot_id', 'portfolio_id')
    list_filter = ('portfolio_id', 'snapshot_id', 'legal_type_of_counterparty', 'counterparty_role')
    fieldsets = (
        ('Portfolio Assignment', {
            'fields': ('portfolio_id', 'snapshot_id', 'counterparty_group_identifier'),
        }),
        ('Identification — EBA Mandatory', {
            'fields': (
                'counterparty_identifier', 'name_of_counterparty',
                'counterparty_role', 'legal_type_of_counterparty', 'industry_segment',
                'national_identifier', 'source_of_national_identifier', 'legal_entity_identifier',
            ),
        }),
        ('Address — EBA Mandatory', {
            'fields': (
                'address_of_registered_location', 'city_of_registered_location',
                'postcode_of_registered_location', 'country_of_registered_location',
            ),
        }),
        ('Private Individual Fields', {
            'fields': (
                'date_of_birth', 'residency_same_country_as_institution', 'counterparty_deceased',
                'availability_of_email_address', 'availability_of_telephone_number', 'date_of_last_contact',
            ),
        }),
        ('Financial Statements — EBA Recommended', {
            'classes': ('collapse',),
            'fields': (
                'date_of_latest_annual_financial_statements', 'currency_of_financial_statements',
                'fixed_assets', 'current_assets', 'cash_and_cash_equivalent_items',
                'total_assets', 'total_liabilities', 'total_debt',
                'annual_turnover', 'annual_ebit',
            ),
        }),
        ('Legal Status — EBA Mandatory', {
            'fields': (
                'name_of_insolvency_or_restructuring_proceedings',
                'status_of_legal_proceedings',
                'description_of_other_legal_measures',
            ),
        }),
        ('Legacy Data', {
            'classes': ('collapse',),
            'fields': (
                'borrower_type',
                'basis_of_financial_statements', 'business_description',
                'comments_on_other_litigation_related_process',
                'commencement_date_of_insolvency_or_restructuring_proceedings',
                'contingent_obligations', 'description_of_contingent_obligations',
                'correspondence_address_of_appointed_insolvency_practitioner',
                'insolvency_practitioner_reference', 'insolvency_practitioner_appointed',
                'proof_of_claim_filed_by_the_seller', 'distribution_made_to_the_seller',
                'notice_for_procedure_termination',
                'cross_collateralisation_for_counterparty', 'description_of_cross_collateralisation',
                'cross_default_for_counterparty', 'description_of_cross_default',
                'currency_of_deposit', 'deposit_balance_with_institution', 'eligibility_for_deposit_to_offset',
                'current_external_credit_rating', 'current_internal_credit_rating',
                'external_credit_rating_at_origination', 'internal_credit_rating_at_origination',
                'source_of_current_external_credit_rating', 'source_of_external_credit_rating_at_origination',
                'date_of_appointment', 'date_of_external_demand_issuance', 'date_of_incorporation',
                'date_of_internal_demand_issuance', 'date_of_obtaining_order_for_possession',
                'date_when_reservation_of_rights_letter_was_issued',
                'description_of_related_party', 'related_party',
                'enterprise_size', 'eviction_date',
                'financial_statements_type', 'financials_audited',
                'geographic_region_classification', 'geographic_region_of_registered_location',
                'indicator_of_counterparty_cooperation',
                'jurisdiction_of_court', 'legal_fees_accrued',
                'legal_procedure_type', 'description_of_legal_procedure_type',
                'market_capitalisation', 'net_assets', 'number_of_fte', 'number_of_joint_counterparties',
                'name_of_insolvency_practitioner',
                'additional_name_of_insolvency_or_restructuring_proceedings',
                'occupation_type', 'occupation_description',
                'other_products_with_institution', 'registration_number',
                'sheriff_or_bailiff_acquisition_date',
            ),
        }),
    )


class CounterpartyGroupAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    fieldsets = (
        ('EBA ITS 2023/2083 — Mandatory', {
            'fields': ('counterparty_group_identifier', 'name_of_counterparty_group'),
        }),
        ('Legacy Data', {
            'classes': ('collapse',),
            'fields': (
                'cross_collateralisation_in_counterparty_group',
                'cross_default_in_counterparty_group',
                'description_of_cross_collateralisation',
                'description_of_cross_default',
                'description_of_sponsor',
                'industry_segment_of_counterparty_group',
                'name_of_sponsor',
                'type_of_sponsor',
            ),
        }),
    )


class LoanAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['loan_identifier']
    list_display = ('loan_identifier', 'counterparty_identifier', 'asset_class',
                    'product_type', 'loan_currency', 'principal_balance',
                    'days_in_pastdue', 'date_of_default')
    list_filter = ('asset_class', 'product_type', 'loan_legal_status', 'forbearance_measure')
    fieldsets = (
        ('Relationships — Template 2', {
            'fields': ('counterparty_identifier',),
        }),
        ('Identification — EBA Mandatory', {
            'fields': (
                'loan_identifier',
                'date_of_origination', 'governing_law_of_loan_agreement',
                'joint_counterparties', 'asset_class', 'product_type', 'loan_currency',
            ),
        }),
        ('Balances — EBA Mandatory', {
            'fields': (
                'principal_balance', 'accrued_interest_balance_on_book',
                'other_balances', 'legal_balance', 'days_in_pastdue',
            ),
        }),
        ('Default & Legal Status — EBA Mandatory', {
            'fields': (
                'date_of_default', 'loan_legal_status',
                'date_of_initiation_of_legal_proceedings', 'stage_reached_in_legal_proceedings',
                'jurisdiction_of_court', 'statute_of_limitations_date',
            ),
        }),
        ('Forbearance & Lease — EBA Mandatory', {
            'fields': ('forbearance_measure', 'lease_agreement'),
        }),
        ('Interest Rate — EBA Recommended', {
            'classes': ('collapse',),
            'fields': (
                'current_maturity_date',
                'current_interest_rate', 'current_interest_rate_type',
                'description_of_current_interest_rate_type',
                'current_interest_margin', 'current_interest_base_rate',
                'current_interest_rate_reference', 'reference_rate',
                'interest_rate_reset_frequency', 'payment_frequency',
                'last_payment_date', 'last_payment_amount',
            ),
        }),
        ('Legal & Structure — EBA Recommended', {
            'classes': ('collapse',),
            'fields': (
                'date_of_obtaining_order_for_possession',
                'syndicated_loan', 'syndicated_portion', 'securitised',
            ),
        }),
        ('Lease Details — EBA Recommended', {
            'classes': ('collapse',),
            'fields': (
                'start_date_of_lease', 'end_date_of_lease',
                'lease_break_option', 'type_of_lease',
            ),
        }),
        ('Legacy Data', {
            'classes': ('collapse',),
            'fields': (
                'instrument_identifier',
                'accounting_stages_of_asset_quality', 'accrued_interest_balance_off_book',
                'amortisation_type', 'balance_at_default', 'capitalised_pastdue_amount',
                'channel_of_origination', 'chargeoff_date',
                'code_of_conduct', 'comments_on_code_of_conduct',
                'comments_on_covenant_waiver', 'country_of_origination', 'covenant_waiver',
                'current_covenant_levels', 'current_external_credit_rating',
                'current_internal_credit_rating', 'current_reversion_interest_rate',
                'default_penalty_interest_margin', 'description_of_bespoke_repayment',
                'description_of_original_interest_rate_type', 'description_of_relevant_schemes',
                'details_of_origination_channel', 'early_redemption_penalty',
                'end_date_of_current_fixed_interest_period', 'end_date_of_interest_grace_period',
                'end_date_of_interest_only_period', 'end_date_of_principal_grace_period',
                'end_date_of_subsidy', 'external_credit_rating_at_origination',
                'final_bullet_repayment',
                'interest_cap_rate', 'interest_floor_rate', 'interest_payment_frequency',
                'interest_reset_interval', 'internal_credit_rating_at_origination',
                'last_covenant_test_date', 'last_interest_reset_date',
                'legal_balance_at_chargeoff_date', 'loan_commitment',
                'loan_covenants', 'loan_purpose', 'loan_status',
                'marp_applicable', 'marp_entry', 'marp_status',
                'next_interest_reset_date', 'next_interest_scheduled_repayment_amount',
                'next_interest_scheduled_repayment_date',
                'next_principal_scheduled_repayment_amount', 'next_principal_scheduled_repayment_date',
                'nonperforming_reason', 'number_of_pastdue_events',
                'original_interest_base_rate', 'original_interest_margin',
                'original_interest_rate', 'original_interest_rate_reference',
                'original_interest_rate_type', 'original_maturity_date', 'origination_amount',
                'other_pastdue_amounts', 'other_syndicate_counterparties',
                'pastdue_interest_amount', 'pastdue_penalty_interest_margin', 'pastdue_principal_amount',
                'principal_payment_frequency', 'recourse_to_other_assets',
                'relevant_schemes', 'source_of_current_external_credit_rating',
                'source_of_external_credit_rating_at_origination', 'specialised_product',
                'start_date_of_current_fixed_interest_period', 'start_date_of_interest_grace_period',
                'start_date_of_interest_only_period', 'start_date_of_principal_grace_period',
                'start_date_of_subsidy', 'subsidy', 'subsidy_amount', 'subsidy_provider',
                'time_in_pastdue', 'total_balance', 'total_pastdue_amount',
                'trigger_levels_of_loan_covenants', 'type_of_reversion_interest_rate',
            ),
        }),
    )


class PropertyCollateralAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['protection_identifier']
    list_display = ('protection_identifier', 'loan_identifier', 'type_of_property',
                    'property_country', 'latest_valuation_amount', 'date_of_latest_valuation')
    list_filter = ('type_of_property', 'enforcement_status')
    fieldsets = (
        ('Relationships — Template 2', {
            'fields': ('loan_identifier',),
        }),
        ('Identification — EBA Mandatory', {
            'fields': ('protection_identifier', 'type_of_property'),
        }),
        ('Location — EBA Mandatory', {
            'fields': (
                'address_of_property', 'city_of_property',
                'property_postcode', 'property_country',
            ),
        }),
        ('Lien — EBA Mandatory', {
            'fields': ('lien_position', 'higher_ranking_loan'),
        }),
        ('Valuation (Internal) — EBA Mandatory', {
            'fields': (
                'currency_of_property', 'latest_valuation_amount',
                'date_of_latest_valuation', 'type_of_appraisal_amount_internal',
            ),
        }),
        ('Valuation (External) — EBA Mandatory', {
            'fields': (
                'latest_external_valuation_amount', 'date_of_latest_external_valuation',
                'type_of_appraisal_amount_external',
            ),
        }),
        ('Enforcement — EBA Mandatory', {
            'fields': ('enforcement_status',),
        }),
        ('Details — EBA Recommended', {
            'classes': ('collapse',),
            'fields': (
                'cadaster_id_number', 'cadaster_identification', 'register_of_deeds_number',
                'year_of_construction',
                'building_area_m2', 'land_area_m2', 'completion_of_property',
                'value_of_energy_performance_certificate', 'type_of_occupancy',
                'type_of_latest_valuation', 'type_of_latest_external_valuation',
                'enforcement_status_third_parties',
            ),
        }),
        ('Legacy Data', {
            'classes': ('collapse',),
            'fields': (
                'amount_of_vat_payable', 'area_type_of_property',
                'building_area_m2_lettable', 'building_area_m2_occupied',
                'condition_of_property', 'current_annual_passing_rent',
                'current_net_operating_income', 'current_opex_and_overheads',
                'date_of_initial_valuation', 'enforcement_description',
                'estimated_annual_void_cost', 'estimated_rental_void',
                'geographic_region_classification', 'geographic_region_of_property',
                'initial_estimated_rental_value', 'initial_valuation_amount',
                'internal_or_external_initial_valuation', 'internal_or_external_latest_valuation',
                'latest_estimated_rental_value', 'legal_owner_of_the_property',
                'number_of_bedrooms', 'number_of_car_parking_spaces',
                'number_of_lettable_units', 'number_of_rooms',
                'number_of_units_occupied', 'number_of_units_vacant',
                'party_liable_for_vat', 'percentage_complete', 'planned_capex_next_12m',
                'provider_of_energy_performance_certificate', 'provider_of_initial_valuation',
                'provider_of_latest_valuation', 'purpose_of_property',
                'remaining_term_of_leasehold', 'sector_of_property', 'tenure',
                'type_of_initial_valuation', 'vat_payable',
                'year_of_refurbishment',
            ),
        }),
    )


class ExternalCollectionAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('external_collection_identifier', 'loan_identifier', 'counterparty_identifier')
    fieldsets = (
        ('Relationships — Template 2', {
            'fields': ('loan_identifier', 'counterparty_identifier'),
        }),
        ('Identification', {
            'fields': ('external_collection_identifier',),
        }),
        ('Legacy Data', {
            'classes': ('collapse',),
            'fields': (
                'institutions_internal_identifier_for_the_loan_or_counterparty',
                'instrument_identifier', 'type_of_identifier',
                'balance_amount_sent_to_agent', 'cash_recoveries', 'costs_accrued',
                'date_returned_from_agent', 'date_sent_to_agent',
                'legal_entity_identifier', 'name_of_external_debt_collection_agent',
                'debt_forgiveness', 'quantity_returned_from_agent',
                'registration_number', 'repayment_plan', 'repayment_plan_description',
            ),
        }),
    )


class EnforcementAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('enforcement_identifier', 'counterparty_identifier',
                    'jurisdiction_of_court', 'court_appraisal_amount', 'sale_agreed_price')
    fieldsets = (
        ('Relationships — Template 2', {
            'fields': (
                'property_collateral_identifier', 'non_property_collateral_identifier',
                'counterparty_identifier',
            ),
        }),
        ('Identification — EBA Mandatory', {
            'fields': ('enforcement_identifier', 'protection_identifier'),
        }),
        ('Enforcement Data — EBA Mandatory', {
            'fields': (
                'jurisdiction_of_court', 'court_appraisal_amount', 'date_of_court_appraisal',
                'sale_agreed_price', 'next_auction_date',
                'court_auction_reserve_price_for_next_auction', 'last_auction_date',
            ),
        }),
        ('Enforcement Details — EBA Recommended', {
            'classes': ('collapse',),
            'fields': (
                'currency_of_enforcement', 'indicator_of_enforcement', 'cash_in_court',
                'court_auction_reserve_price_for_last_auction', 'number_of_failed_auctions',
            ),
        }),
        ('Legacy Data', {
            'classes': ('collapse',),
            'fields': (
                'amount_of_outstanding_liabilities', 'annual_insurance_payment',
                'contracted_date', 'collateral_repossessed_date',
                'costs_accrued_to_buyer', 'costs_at_end_of_sale',
                'court_auction_identifier', 'court_auction_reserve_price_for_first_auction',
                'current_market_status', 'date_next_insurance_payment_is_due',
                'date_of_receiver_appointment', 'enforcement_description',
                'fees_of_receivership', 'first_auction_date',
                'funds_remitted_full_date', 'funds_remitted_partial_date',
                'gross_sale_proceeds', 'indicator_of_receivership',
                'insurance', 'insurance_coverage_amount', 'insurance_provider',
                'name_of_legal_firm', 'name_of_receiver', 'net_sale_proceeds',
                'offer_price', 'on_market_offer_date', 'on_market_price',
                'other_ongoing_enforcement_proceedings',
                'prepare_property_for_sale_date', 'property_on_market_date',
                'sale_agreed_date', 'sold_date',
            ),
        }),
    )


class NonPropertyCollateralAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['protection_identifier']
    list_display = ('protection_identifier', 'loan_identifier', 'collateral_type',
                    'latest_valuation_amount', 'enforcement_status')
    list_filter = ('collateral_type', 'enforcement_status')
    fieldsets = (
        ('Relationships — Template 2', {
            'fields': ('loan_identifier',),
        }),
        ('Identification — EBA Mandatory', {
            'fields': ('protection_identifier', 'collateral_type'),
        }),
        ('Valuation — EBA Mandatory', {
            'fields': (
                'currency_of_collateral', 'latest_valuation_amount',
                'date_of_latest_valuation', 'guarantee_amount',
            ),
        }),
        ('Enforcement — EBA Mandatory', {
            'fields': ('enforcement_status',),
        }),
        ('Details — EBA Recommended', {
            'classes': ('collapse',),
            'fields': ('type_of_latest_valuation', 'isin', 'enforcement_status_third_parties'),
        }),
        ('Legacy Data', {
            'classes': ('collapse',),
            'fields': (
                'activation_of_guarantee', 'collateral_insurance',
                'collateral_insurance_coverage_amount', 'collateral_insurance_provider',
                'estimated_useful_life', 'configuration',
                'original_country_of_registration', 'current_country_of_registration',
                'current_opex_and_overheads', 'date_of_initial_valuation',
                'description', 'enforcement_description', 'engine_size',
                'initial_valuation_amount', 'initial_residual_value',
                'date_of_the_latest_residual_valuation', 'initial_residual_valuation_date',
                'latest_residual_value', 'legal_owner', 'manufacturer_of_collateral',
                'name_or_model_of_collateral', 'new_or_used', 'registration_number',
                'type_of_initial_valuation', 'type_of_legal_owner',
                'asset_purchase_obligation', 'option_to_buy_price',
                'year_of_manufacture', 'year_of_registration',
            ),
        }),
    )


class ForbearanceAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('forbearance_identifier', 'loan_identifier', 'counterparty_identifier',
                    'type_of_forbearance', 'end_date_of_forbearance')
    list_filter = ('type_of_forbearance',)
    fieldsets = (
        ('Relationships — Template 2', {
            'fields': ('loan_identifier', 'counterparty_identifier'),
        }),
        ('Identification', {
            'fields': ('forbearance_identifier',),
        }),
        ('Forbearance — EBA Mandatory', {
            'fields': ('type_of_forbearance', 'end_date_of_forbearance'),
        }),
        ('Details — EBA Recommended', {
            'classes': ('collapse',),
            'fields': (
                'description_of_forbearance', 'debt_forgiveness',
                'number_of_historical_forbearance',
            ),
        }),
        ('Legacy Data', {
            'classes': ('collapse',),
            'fields': (
                'type_of_identifier',
                'institutions_internal_identifier_for_the_loan_or_counterparty',
                'instrument_identifier', 'amount_of_repayment_step_up',
                'clause_to_stop_forbearance', 'date_of_first_forbearance',
                'date_of_principal_forgiveness', 'date_of_repayment_step_up',
                'description_of_the_forbearance_clause', 'interest_rate_under_forbearance',
                'repayment_amount_under_forbearance', 'repayment_frequency_under_forbearance',
                'start_date_of_forbearance',
            ),
        }),
    )


class HistoricalRepaymentAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    change_list_template = 'admin/npl_portfolio/historicalrepayment/change_list.html'
    list_display = ('loan_identifier', 'snapshot_id', 'reference_year', 'reference_month',
                    'type_of_collection', 'history_of_total_repayments',
                    'history_of_repayments_from_collateral_sales')
    list_filter = ('portfolio_id', 'snapshot_id', 'type_of_collection')
    fieldsets = (
        ('Portfolio Assignment', {
            'fields': ('portfolio_id', 'snapshot_id', 'loan_identifier'),
        }),
        ('EBA ITS 2023/2083 — Template 5', {
            'fields': (
                'reference_year', 'reference_month', 'type_of_collection',
                'name_of_external_collection_agent',
                'history_of_total_repayments',
                'history_of_repayments_from_collateral_sales',
            ),
        }),
    )

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom = [
            path('matrix/', self.admin_site.admin_view(self.matrix_view),
                 name='npl_portfolio_historicalrepayment_matrix'),
        ]
        return custom + urls

    def matrix_view(self, request):
        from django.http import HttpResponse
        from django.urls import reverse
        from npl_portfolio.models import HistoricalRepayment, PortfolioSnapshot

        snapshots = PortfolioSnapshot.objects.all().order_by('-cutoff_date')
        selected_snapshot_id = request.GET.get('snapshot_id')

        qs = HistoricalRepayment.objects.select_related('loan_identifier', 'snapshot_id')
        if selected_snapshot_id:
            qs = qs.filter(snapshot_id=selected_snapshot_id)

        records = list(qs)

        col_set = sorted(
            set(
                (r.reference_year, r.reference_month)
                for r in records
                if r.reference_year is not None and r.reference_month is not None
            ),
            reverse=True,
        )
        columns = [{'year': y, 'month': m, 'label': f'{y}-{m:02d}'} for y, m in col_set]

        loan_data = {}
        for r in records:
            loan_key = r.loan_identifier_id
            loan_label = str(r.loan_identifier) if r.loan_identifier else f'#{loan_key}'
            if loan_key not in loan_data:
                loan_data[loan_key] = {'label': loan_label, 'cells': {}}
            if r.reference_year is not None and r.reference_month is not None:
                loan_data[loan_key]['cells'][(r.reference_year, r.reference_month)] = {
                    'total': r.history_of_total_repayments,
                    'collateral': r.history_of_repayments_from_collateral_sales,
                    'collection_type': r.type_of_collection,
                    'agent_name': r.name_of_external_collection_agent,
                }

        rows = [
            {
                'loan': data['label'],
                'cells': [
                    data['cells'].get((col['year'], col['month']), {
                        'total': None, 'collateral': None,
                        'collection_type': None, 'agent_name': None,
                    })
                    for col in columns
                ],
            }
            for data in loan_data.values()
        ]

        changelist_url = reverse('admin:npl_portfolio_historicalrepayment_changelist')

        # --- Snapshot filter options ---
        snapshot_options = '<option value="">— All snapshots —</option>'
        for s in snapshots:
            label = s.name + (f' ({s.cutoff_date.date()})' if s.cutoff_date else '')
            sel = 'selected' if selected_snapshot_id == str(s.pk) else ''
            snapshot_options += f'<option value="{s.pk}" {sel}>{label}</option>'

        clear_link = f'<a href="?" style="font-size:12px;color:#888;">Clear</a>' if selected_snapshot_id else ''

        # --- Table header ---
        month_headers = ''.join(
            f'<th colspan="2" style="background:#1a3a4a;padding:6px 12px;border:1px solid #444;'
            f'text-align:center;font-weight:600;color:#7ecfef;">{col["label"]}</th>'
            for col in columns
        )
        sub_headers = ''.join(
            '<th style="background:#1a2a3a;padding:4px 8px;border:1px solid #444;'
            'text-align:right;color:#aaa;font-weight:400;min-width:90px;">Total</th>'
            '<th style="background:#1a2a3a;padding:4px 8px;border:1px solid #444;'
            'text-align:right;color:#aaa;font-weight:400;min-width:90px;">Collateral</th>'
            for _ in columns
        )

        # --- Table rows ---
        def fmt(val):
            return f'{val:,}' if val is not None else '—'

        def cell_html(cell, bg):
            total = cell['total']
            collateral = cell['collateral']
            ctype = cell['collection_type']
            agent = cell['agent_name'] or ''
            total_color = '#eee' if total is not None else '#555'
            col_color = '#7ecfef' if collateral else '#555'
            ext_badge = ''
            if ctype == 1:
                tip = f'Agent: {agent}' if agent else 'External collection'
                ext_txt = f'EXT · {agent}' if agent else 'EXT'
                ext_badge = (f'<br><span style="font-size:10px;background:#a05000;color:#fff;'
                             f'padding:1px 5px;border-radius:3px;font-weight:600;" title="{tip}">'
                             f'{ext_txt}</span>')
            td_total = (f'<td style="padding:6px 10px;border:1px solid #333;text-align:right;'
                        f'color:{total_color};vertical-align:top;background:{bg};">'
                        f'{fmt(total)}{ext_badge}</td>')
            td_col = (f'<td style="padding:6px 10px;border:1px solid #333;text-align:right;'
                      f'color:{col_color};background:{bg};">{fmt(collateral)}</td>')
            return td_total + td_col

        table_rows = ''
        for i, row in enumerate(rows):
            bg = '#1e1e1e' if i % 2 == 0 else '#242424'
            sticky_td = (f'<td style="position:sticky;left:0;z-index:1;background:{bg};'
                         f'padding:6px 16px;border:1px solid #333;font-weight:600;color:#ddd;">'
                         f'{row["loan"]}</td>')
            cells_html = ''.join(cell_html(c, bg) for c in row['cells'])
            table_rows += f'<tr>{sticky_td}{cells_html}</tr>'

        empty_msg = '' if columns else (
            '<div style="padding:40px;text-align:center;color:#888;background:#2b2b2b;border-radius:6px;">'
            'No repayment data found.</div>'
        )

        stats = (f'<p style="font-size:12px;color:#888;margin-bottom:12px;">'
                 f'{len(rows)} loan{"s" if len(rows) != 1 else ""} &nbsp;·&nbsp; '
                 f'{len(columns)} month{"s" if len(columns) != 1 else ""} &nbsp;·&nbsp; '
                 f'Columns sorted most-recent first &nbsp;·&nbsp; Amounts in loan currency</p>'
                 ) if columns else ''

        table_html = (
            f'<div style="overflow-x:auto;max-width:100%;">'
            f'<table style="border-collapse:collapse;font-size:12px;white-space:nowrap;min-width:100%;">'
            f'<thead>'
            f'<tr><th rowspan="2" style="position:sticky;left:0;z-index:2;background:#1a1a2e;'
            f'padding:8px 16px;border:1px solid #444;text-align:left;min-width:180px;">Loan Identifier</th>'
            f'{month_headers}</tr>'
            f'<tr>{sub_headers}</tr>'
            f'</thead>'
            f'<tbody>{table_rows}</tbody>'
            f'</table></div>'
        ) if columns else ''

        html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>EBA Template 5 Matrix</title>
<link rel="stylesheet" href="/static/admin/css/base.css">
<style>body{{background:#121212;color:#eee;font-family:sans-serif;padding:20px;}}</style>
</head><body>
<div style="padding:8px 0 16px;">
  <a href="{changelist_url}" style="color:#888;font-size:13px;">← Historical Repayments</a>
</div>
<h1 style="margin-bottom:20px;">Historical Repayments — EBA Template 5 Matrix</h1>
<form method="get" style="margin-bottom:20px;display:flex;align-items:center;gap:12px;">
  <label for="snapshot_id" style="font-weight:600;font-size:13px;">Snapshot:</label>
  <select name="snapshot_id" id="snapshot_id"
    style="padding:4px 10px;border-radius:4px;border:1px solid #444;background:#2b2b2b;color:#eee;font-size:13px;">
    {snapshot_options}
  </select>
  <button type="submit"
    style="padding:4px 14px;background:#1a7a4a;color:#fff;border:none;border-radius:4px;cursor:pointer;font-size:13px;">
    Apply
  </button>
  {clear_link}
</form>
{stats}{empty_msg}{table_html}
</body></html>"""

        return HttpResponse(html)


class MortgageAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['mortgage_identifier', 'protection_identifier']
    list_display = ('mortgage_identifier', 'protection_identifier', 'loan_identifier',
                    'mortgage_amount', 'lien_position', 'register_of_deeds_number')
    list_filter = ('lien_position',)
    fieldsets = (
        ('Relationships — Template 2', {
            'fields': ('loan_identifier',),
        }),
        ('Identification — EBA Mandatory', {
            'fields': ('mortgage_identifier', 'protection_identifier'),
        }),
        ('Mortgage Data — EBA Mandatory', {
            'fields': ('mortgage_amount', 'lien_position', 'higher_ranking_loan'),
        }),
        ('EBA Recommended', {
            'fields': ('register_of_deeds_number',),
        }),
    )


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioSnapshot, Portfolio_SnapshotAdmin)
admin.site.register(CounterpartyGroup, CounterpartyGroupAdmin)
admin.site.register(Counterparty, CounterpartyAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(ExternalCollection, ExternalCollectionAdmin)
admin.site.register(Enforcement, EnforcementAdmin)
admin.site.register(NonPropertyCollateral, NonPropertyCollateralAdmin)
admin.site.register(PropertyCollateral, PropertyCollateralAdmin)
admin.site.register(Forbearance, ForbearanceAdmin)
admin.site.register(HistoricalRepayment, HistoricalRepaymentAdmin)
admin.site.register(Mortgage, MortgageAdmin)
