# Copyright (c) 2020 - 2024 Open Risk (https://www.openriskmanagement.com)
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

import numpy as np
import pandas as pd
from django.core.management.base import BaseCommand

from sflp_portfolio.models.counterparty import Counterparty
from sflp_portfolio.models.counterparty_state import CounterpartyState
from sflp_portfolio.models.enforcement import Enforcement
from sflp_portfolio.models.forbearance import Forbearance
from sflp_portfolio.models.loan import Loan
from sflp_portfolio.models.loan_state import LoanState
from sflp_portfolio.models.models import Portfolio
from sflp_portfolio.models.models import PortfolioSnapshot
from sflp_portfolio.models.property_collateral import PropertyCollateral
from sflp_portfolio.models.property_collateral_state import PropertyCollateralState

column_datatypes = {
    'zero_balance_code': pd.Int64Dtype(),
    'loan_holdback_indicator': pd.Int64Dtype(),
    'counterparty_identifier': str
}


class Command(BaseCommand):
    help = 'Imports Segmented SFLP data (All Models)'

    # Clean up the database
    Portfolio.objects.all().delete()
    PortfolioSnapshot.objects.all().delete()
    Loan.objects.all().delete()
    Counterparty.objects.all().delete()
    Enforcement.objects.all().delete()
    Forbearance.objects.all().delete()
    PropertyCollateral.objects.all().delete()

    #
    # Portfolio data
    #
    portfolio_data = pd.read_csv("./sflp_portfolio/fixtures/portfolio.csv", sep='|', index_col=None, low_memory=False,
                                 na_values=None,
                                 true_values=['Y'], false_values=['N'])
    print('Loaded Portfolio Data')

    portfolio_dict = {}
    for index, entry in portfolio_data.iterrows():
        portfolio, _ = Portfolio.objects.update_or_create(
            name=entry[0],
            description='Test SFLP Portfolio',
        )
        portfolio.save()
        portfolio_dict[entry[0]] = portfolio

    print('Created Portfolio Entities')
    #
    # Portfolio snapshot data
    #
    portfolio_snapshot_data = pd.read_csv("./sflp_portfolio/fixtures/portfolio_snapshot.csv", sep='|', index_col=None,
                                          low_memory=False, na_values=None,
                                          true_values=['Y'], false_values=['N'])

    print('Loaded Portfolio Snapshots')
    portfolio_snapshot_dict = {}
    for index, entry in portfolio_snapshot_data.iterrows():
        portfolio_snapshot, _ = PortfolioSnapshot.objects.update_or_create(
            monthly_reporting_period=entry[0],
        )
        portfolio_snapshot.save()
        portfolio_snapshot_dict[entry[0]] = portfolio_snapshot

    print('Created Portfolio Snapshots')
    #
    # Static Loan Data
    #
    loan_data = pd.read_csv("./sflp_portfolio/fixtures/loan.csv", sep='|', index_col=None, low_memory=False,
                            na_values=None,
                            true_values=['Y'], false_values=['N'])

    print('Loaded Static Loan Data')
    loan_data_list = []
    i = 0
    loan_dict = {}
    for index, entry in loan_data.iterrows():
        # print('Loan: ', i)
        loan = Loan(
            id=i,
            loan_identifier=entry[0],
            portfolio=portfolio_dict[entry[1]],
            channel=entry[2],
            original_interest_rate=entry[3],
            original_upb=entry[4],
            original_loan_term=entry[5],
            origination_date=entry[6],
            first_payment_date=entry[7],
            original_loan_to_value_ratio=entry[8],
            loan_purpose=entry[9],
            amortization_type=entry[10],
            relocation_mortgage_indicator=entry[11],
            high_balance_loan_indicator=entry[12],
            mortgage_insurance_percentage=entry[13],
            mortgage_insurance_type=entry[14],
            original_combined_loan_to_value_ratio=entry[15]

        )
        # loan.save()
        loan_data_list.append(loan)
        loan_dict[entry[0]] = loan
        i += 1

    Loan.objects.bulk_create(loan_data_list)
    print('Created Static Loan Entries')
    #
    # Dynamic Loan Data
    #

    loan_state_data = pd.read_csv("./sflp_portfolio/fixtures/loan_state.csv", sep='|', index_col=None, na_values=None,
                                  true_values=['Y'], false_values=['N'], dtype=column_datatypes)

    loan_state_data = loan_state_data.replace({np.nan: None})

    print("Loaded Dynamic Loan Data")

    loan_state_data_list = []
    i = 0
    for index, entry in loan_state_data.iterrows():
        # print('LoanState: ', i)
        loan_state = LoanState(
            id=i,
            loan_identifier=loan_dict[entry[0]],
            portfolio_snapshot_id=portfolio_snapshot_dict[entry[1]],
            high_loan_to_value_refinance_option_indicator=entry[2],
            zero_balance_code=entry[3],
            zero_balance_effective_date=entry[4],
            upb_at_the_time_of_removal=entry[5],
            total_principal_current=entry[6],
            last_paid_installment_date=entry[7],
            months_to_amortization=entry[8],
            mortgage_insurance_cancellation_indicator=entry[9],
            scheduled_principal_current=entry[10],
            unscheduled_principal_current=entry[11],
            zero_balance_code_change_date=entry[12],
            loan_holdback_indicator=entry[13],
            loan_holdback_effective_date=entry[14],
            next_interest_rate_adjustment_date=entry[15],
            next_payment_change_date=entry[16],
            servicer_name=entry[17],
            current_interest_rate=entry[18],
            current_actual_upb=entry[19],
            loan_age=entry[20],
            remaining_months_to_legal_maturity=entry[21],
            remaining_months_to_maturity=entry[22],
            maturity_date=entry[23],
            servicing_activity_indicator=entry[24],
            repayment_history=entry[25]
        )
        loan_state_data_list.append(loan_state)
        i += 1

    LoanState.objects.bulk_create(loan_state_data_list)
    print("Created Dynamic Loan Data")

    #
    # Static Counterparty data
    #
    counterparty_data = pd.read_csv("./sflp_portfolio/fixtures/counterparty.csv", sep='|', index_col=None,
                                    low_memory=False, na_values=None,
                                    true_values=['Y'], false_values=['N'], dtype=column_datatypes)

    print("Loaded Static Counterparty Data")

    counterparty_data_list = []
    i = 0
    counterparty_dict = {}
    for index, entry in counterparty_data.iterrows():
        counterparty = Counterparty(
            id=i,
            loan_identifier=loan_dict[entry[0]],  # loan FK reference
            counterparty_identifier=entry[0],  # counterparty ID is identical to loan ID
            number_of_borrowers=entry[1],
            debt_to_income=entry[2],
            borrower_credit_score_at_origination=entry[3],
            coborrower_credit_score_at_origination=entry[4],
            first_time_home_buyer_indicator=entry[5],
        )
        counterparty_data_list.append(counterparty)
        counterparty_dict[entry[0]] = counterparty
        i += 1

    Counterparty.objects.bulk_create(counterparty_data_list)
    print("Created Static Counterparty Data")

    #
    # Counterparty State data
    #
    counterparty_state_data = pd.read_csv("./sflp_portfolio/fixtures/counterparty_state.csv", sep='|', index_col=None,
                                          low_memory=False, na_values=None,
                                          true_values=['Y'], false_values=['N'], dtype=column_datatypes)
    counterparty_state_data = counterparty_state_data.replace({np.nan: None})

    print("Loaded Counterparty State Data")

    counterparty_state_data_list = []
    i = 0
    for index, entry in counterparty_state_data.iterrows():
        counterparty_state = CounterpartyState(
            id=i,
            counterparty_identifier=counterparty_dict[entry[0]],
            portfolio_snapshot_id=portfolio_snapshot_dict[entry[1]],
            borrower_credit_score_current=entry[2],
            coborrower_credit_score_current=entry[3],
        )
        counterparty_state_data_list.append(counterparty_state)
        i += 1

    CounterpartyState.objects.bulk_create(counterparty_state_data_list)
    print("Created Counterparty State Data")

    #
    # Static Property collateral data
    #
    property_collateral_data = pd.read_csv("./sflp_portfolio/fixtures/property_collateral.csv", sep='|', index_col=None,
                                           low_memory=False, na_values=None,
                                           true_values=['Y'], false_values=['N'], dtype=column_datatypes)

    print("Loaded Static Collateral Data")

    property_collateral_data_list = []
    i = 0
    property_collateral_dict = {}
    for index, entry in property_collateral_data.iterrows():
        property_collateral = PropertyCollateral(
            id=i,
            loan_identifier=loan_dict[entry[0]],  # loan FK reference
            property_type=entry[1],
            number_of_units=entry[2],
            occupancy_status=entry[3],
            property_state=entry[4],
            metropolitan_statistical_area=entry[5],
            zip_code_short=entry[6]
        )
        property_collateral_data_list.append(property_collateral)
        i += 1
        property_collateral_dict[entry[0]] = property_collateral
    PropertyCollateral.objects.bulk_create(property_collateral_data_list)
    print("Created Property Collateral Static Data")

    #
    # Property Collateral State data
    #
    property_collateral_state_data = pd.read_csv("./sflp_portfolio/fixtures/property_collateral_state.csv", sep='|',
                                                 index_col=None,
                                                 low_memory=False, na_values=None,
                                                 true_values=['Y'], false_values=['N'], dtype=column_datatypes)
    property_collateral_state_data = property_collateral_state_data.replace({np.nan: None})
    print("Loaded Property Collateral State Data")

    property_collateral_state_data_list = []
    i = 0
    for index, entry in property_collateral_state_data.iterrows():
        property_collateral_state = PropertyCollateralState(
            id=i,
            property_collateral_id=property_collateral_dict[entry[0]],
            portfolio_snapshot_id=portfolio_snapshot_dict[entry[1]],
            property_preservation_and_repair_costs=entry[2],
            miscellaneous_holding_expenses_and_credits=entry[3],
            associated_taxes_for_holding_property=entry[4],
            property_valuation_method=entry[5],
        )
        property_collateral_state_data_list.append(property_collateral_state)
        i += 1

    PropertyCollateralState.objects.bulk_create(property_collateral_state_data_list)
    print("Created Property Collateral State Data")

    #
    # Forbearance data
    #
    forbearance_data = pd.read_csv("./sflp_portfolio/fixtures/forbearance.csv", sep='|',
                                   index_col=None,
                                   low_memory=False, na_values=None,
                                   true_values=['Y'], false_values=['N'], dtype=column_datatypes)
    forbearance_data = forbearance_data.replace({np.nan: None})
    print("Loaded Forbearance Data")

    forbearance_data_list = []
    i = 0
    for index, entry in forbearance_data.iterrows():
        forbearance = Forbearance(
            id=i,
            loan_identifier=loan_dict[entry[0]],
            portfolio_snapshot_id=portfolio_snapshot_dict[entry[1]],
            current_loan_delinquency_status=entry[2],
            modification_flag=entry[3],
            noninterest_bearing_upb=entry[4],
            principal_forgiveness_amount=entry[5],
            current_period_modification_loss_amount=entry[6],
            cumulative_modification_loss_amount=entry[7],
            current_period_credit_event_net_gain_or_loss=entry[8],
            delinquent_accrued_interest=entry[11],
            borrower_assistance_plan=entry[12],
            alternative_delinquency_resolution=entry[13],
            alternative_delinquency_resolution_count=entry[14],
            total_deferral_amount=entry[15],
        )
        forbearance_data_list.append(forbearance)
        i += 1

    Forbearance.objects.bulk_create(forbearance_data_list)
    print("Created Forbearance Data")

    #
    # Enforcement data
    #
    enforcement_data = pd.read_csv("./sflp_portfolio/fixtures/enforcement.csv", sep='|',
                                   index_col=None,
                                   low_memory=False, na_values=None,
                                   true_values=['Y'], false_values=['N'], dtype=column_datatypes)
    enforcement_data = enforcement_data.replace({np.nan: None})
    print("Loaded Enforcement Data")

    enforcement_data_list = []
    i = 0
    for index, entry in enforcement_data.iterrows():
        enforcement = Enforcement(
            id=i,
            loan_identifier=loan_dict[entry[0]],
            property_collateral_identifier=property_collateral_dict[entry[0]],
            portfolio_snapshot_id=portfolio_snapshot_dict[entry[1]],
            repurchase_date=entry[2],
            foreclosure_date=entry[3],
            disposition_date=entry[4],
            foreclosure_costs=entry[5],
            asset_recovery_costs=entry[6],
            net_sales_proceeds=entry[7],
            credit_enhancement_proceeds=entry[8],
            repurchase_make_whole_proceeds=entry[9],
            other_foreclosure_proceeds=entry[10],
            original_list_start_date=entry[11],
            original_list_price=entry[12],
            current_list_start_date=entry[13],
            current_list_price=entry[14],
            cumulative_credit_event_net_gain_or_loss=entry[15],
            foreclosure_principal_writeoff_amount=entry[16],
            repurchase_make_whole_proceeds_flag=entry[17],
        )
        enforcement_data_list.append(enforcement)
        i += 1

    Enforcement.objects.bulk_create(enforcement_data_list)
    print("Created Enforcement Data")

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted Full SFLP data into db'))
