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
import sys

import numpy as np
import pandas as pd
from django.core.management.base import BaseCommand

from sflp_portfolio.models.models import Portfolio
from sflp_portfolio.models.models import PortfolioSnapshot

from sflp_portfolio.models.counterparty import Counterparty
from sflp_portfolio.models.loan import Loan
from sflp_portfolio.models.property_collateral import PropertyCollateral

from sflp_portfolio.models.counterparty_state import CounterpartyState
from sflp_portfolio.models.loan_state import LoanState
from sflp_portfolio.models.property_collateral_state import PropertyCollateralState

"""
Note: this is not a performant insertion of data, use for debugging data schemas / pipelines 

"""


class Command(BaseCommand):
    help = 'Imports Segmented Single Family Loan Performance data (Core Models)'

    # Clean up the database
    Portfolio.objects.all().delete()
    PortfolioSnapshot.objects.all().delete()
    Counterparty.objects.all().delete()
    Loan.objects.all().delete()
    PropertyCollateral.objects.all().delete()

    #
    # Portfolio data
    #
    portfolio_data = pd.read_csv("./sflp_portfolio/fixtures/portfolio.csv", sep='|', index_col=None, low_memory=False,
                                 na_values=None,
                                 true_values=['Y'], false_values=['N'])

    portfolio_dict = {}
    for index, entry in portfolio_data.iterrows():
        portfolio, _ = Portfolio.objects.update_or_create(
            name=entry[0],
            description='Test SFLP Portfolio',
        )
        portfolio.save()
        portfolio_dict[entry[0]] = portfolio

    #
    # Portfolio snapshot data
    #
    portfolio_snapshot_data = pd.read_csv("./sflp_portfolio/fixtures/portfolio_snapshot.csv", sep='|', index_col=None,
                                          low_memory=False, na_values=None,
                                          true_values=['Y'], false_values=['N'])

    portfolio_snapshot_dict = {}
    for index, entry in portfolio_snapshot_data.iterrows():
        portfolio_snapshot, _ = PortfolioSnapshot.objects.update_or_create(
            monthly_reporting_period=entry[0],
        )
        portfolio_snapshot.save()
        portfolio_snapshot_dict[entry[0]] = portfolio_snapshot

    #
    # Static Loan Data
    #
    loan_data = pd.read_csv("./sflp_portfolio/fixtures/loan.csv", sep='|', index_col=None, low_memory=False,
                            na_values=None,
                            true_values=['Y'], false_values=['N'])

    loan_data_list = []
    i = 0
    loan_dict = {}
    for index, entry in loan_data.iterrows():
        print('Loan: ', i)
        loan = Loan(
            id=i,
            loan_identifier=entry[0],
            portfolio=portfolio_dict[entry[1]],
            # snapshot=portfolio_snapshot_dict[entry[2]],
            channel=entry[3],
            original_interest_rate=entry[4],
            original_upb=entry[5],
            original_loan_term=entry[6],
            origination_date=entry[7],
            first_payment_date=entry[8],
            original_loan_to_value_ratio=entry[9],
            loan_purpose=entry[10],
            amortization_type=entry[11],
            relocation_mortgage_indicator=entry[12],
            high_balance_loan_indicator=entry[13],
            mortgage_insurance_percentage=entry[14],
            mortgage_insurance_type=entry[15],
            original_combined_loan_to_value_ratio=entry[16],
            # prepayment_penalty_indicator=entry[17],
            # interest_only_loan_indicator=entry[18],
        )
        # loan.save()
        loan_data_list.append(loan)
        loan_dict[entry[0]] = loan
        i += 1

    Loan.objects.bulk_create(loan_data_list)
    #
    # Dynamic Loan Data
    #

    column_datatypes = {
        'zero_balance_code': pd.Int64Dtype(),
        'loan_holdback_indicator': pd.Int64Dtype()
    }
    loan_state_data = pd.read_csv("./sflp_portfolio/fixtures/loan_state.csv", sep='|', index_col=None, true_values=['Y'], false_values=['N'], dtype=column_datatypes)

    loan_state_data = loan_state_data.replace({np.nan: None})

    loan_state_data_list = []
    i = 0
    for index, entry in loan_state_data.iterrows():
        print('LoanState: ', i)
        loan_state = LoanState(
            id=i,
            loan_id=loan_dict[entry[0]],
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
            servicing_activity_indicator=entry[24]
        )
        loan_state_data_list.append(loan_state)
        # loan_state.save()
        i += 1

    LoanState.objects.bulk_create(loan_state_data_list)

    # #
    # # Static Counterparty data
    # #
    # counterparty_data = pd.read_csv("./sflp_portfolio/fixtures/counterparty.csv", sep='|', index_col=None,
    #                                 low_memory=False, na_values=None,
    #                                 true_values=['Y'], false_values=['N'])
    # i = 0
    # for index, entry in counterparty_data.iterrows():
    #     counterparty = Counterparty.objects.create(
    #         id=i,
    #         loan_id=loan_dict[entry[0]],  # loan FK reference
    #         counterparty_id=entry[0],  # counterparty ID identical to loan ID
    #         number_of_borrowers=entry[1],
    #         debt_to_income=entry[2],
    #         borrower_credit_score_at_origination=entry[3],
    #         coborrower_credit_score_at_origination=entry[4],
    #         first_time_home_buyer_indicator=entry[5],
    #     )
    #     counterparty.save()
    #     i += 1
    #
    # #
    # # Static Property collateral data
    # #
    # property_collateral_data = pd.read_csv("./sflp_portfolio/fixtures/property_collateral.csv", sep='|', index_col=None,
    #                                        low_memory=False, na_values=None,
    #                                        true_values=['Y'], false_values=['N'])
    #
    # i = 0
    # for index, entry in property_collateral_data.iterrows():
    #     property_collateral = PropertyCollateral.objects.create(
    #         id=i,
    #         loan_id=loan_dict[entry[0]],  # loan FK reference
    #         property_type=entry[1],
    #         number_of_units=entry[2],
    #         occupancy_status=entry[3],
    #         property_state=entry[4],
    #         metropolitan_statistical_area=entry[5],
    #         zip_code_short=entry[6]
    #     )
    #     property_collateral.save()
    #     i += 1

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted Core SFLP data into db'))
