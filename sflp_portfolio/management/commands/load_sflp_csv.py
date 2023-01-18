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

import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand

from sflp_portfolio.models.models import Portfolio
from sflp_portfolio.models.models import PortfolioSnapshot
from sflp_portfolio.models.loan import Loan
from sflp_portfolio.models.counterparty import Counterparty
from sflp_portfolio.models.property_collateral import PropertyCollateral
from sflp_portfolio.models.repayment_schedule import RepaymentSchedule
from sflp_portfolio.models.forbearance import Forbearance
from sflp_portfolio.models.enforcement import Enforcement

from sflp_portfolio.models.model_choices import *


class Command(BaseCommand):
    help = 'Imports SFLP data'

    Portfolio.objects.all().delete()
    PortfolioSnapshot.objects.all().delete()
    Loan.objects.all().delete()
    Counterparty.objects.all().delete()
    Enforcement.objects.all().delete()
    Forbearance.objects.all().delete()
    PropertyCollateral.objects.all().delete()
    RepaymentSchedule.objects.all().delete()

    data = pd.read_csv("sflp_portfolio/fixtures/test.csv", sep='|', index_col=None, low_memory=False, na_values=None,
                       true_values=['Y'], false_values=['N'])

    data.fillna(np.nan, inplace=True)
    data = data.replace({np.nan: None})

    counterparty_data = []
    enforcement_data = []
    loan_data = []
    forbearance_data = []
    portfolio_data = []
    portfoliosnapshot_data = []
    propertycollateral_data = []
    repaymentschedule_data = []

    i = 0
    for index, entry in data.iterrows():
        i += 1
        if (i > 4):
            break
        print(i)
        if entry[43] == 1.0:
            entry[43] = '01'

        if entry[101] == 7.0:
            entry[101] = '7'

        if entry[78] is None:
            entry[78] = 'N'


        portfolio, _ = Portfolio.objects.update_or_create(
            name='test.csv',
            description='Test Portfolio',
            reference_pool_id=entry[0],
            deal_name=entry[103],
        )
        portfolio.save()

        portfoliosnapshot, _ = PortfolioSnapshot.objects.update_or_create(
            monthly_reporting_period=entry[2],
        )
        portfoliosnapshot.save()

        loan = Loan(
            portfolio=portfolio,
            snapshot=portfoliosnapshot,
            loan_identifier=str(entry[1]),
            channel=CHANNEL_DICT[entry[3]],
            seller_name=entry[4],
            servicer_name=entry[5],
            master_servicer=entry[6],
            original_interest_rate=entry[7],
            current_interest_rate=entry[8],
            original_upb=entry[9],
            upb_at_issuance=entry[10],
            current_actual_upb=entry[11],
            original_loan_term=entry[12],
            origination_date=pd.to_datetime(entry[13], format="%m%Y"),
            first_payment_date=pd.to_datetime(entry[14], format="%m%Y"),
            loan_age=entry[15],
            maturity_date=pd.to_datetime(entry[18], format="%m%Y"),
            original_loan_to_value_ratio=entry[19],
            original_combined_loan_to_value_ratio=entry[20],
            loan_purpose=LOAN_PURPOSE_DICT[entry[26]],
            mortgage_insurance_percentage=entry[33],
            amortization_type=AMORTIZATION_DICT[entry[34]],
            prepayment_penalty_indicator=entry[35],
            interest_only_loan_indicator=entry[36],
            interest_only_first_principal_and_interest_payment_date=
            pd.to_datetime(entry[37], format="%m%Y"),
            current_loan_delinquency_status=entry[39],
            mortgage_insurance_cancellation_indicator=entry[42],
            mortgage_insurance_type=MORTGAGE_INSURANCE_DICT[entry[72]],
            servicing_activity_indicator=entry[73],
            current_period_credit_event_net_gain_or_loss=entry[76],
            cumulative_credit_event_net_gain_or_loss=entry[77],
            special_eligibility_program=ELIGIBILITY_DICT[entry[78]],
            relocation_mortgage_indicator=entry[80],
            loan_holdback_indicator=LOAN_HOLDBACK_DICT[entry[82]],
            loan_holdback_effective_date=entry[83],
            delinquent_accrued_interest=entry[84],
            high_balance_loan_indicator=entry[86],
            arm_initial_fixed_rate_period_less_than_5_yr=entry[87],
            arm_product_type=entry[88],
            initial_fixed_rate_period=entry[89],
            interest_rate_adjustment_frequency=entry[90],
            next_interest_rate_adjustment_date=entry[91],
            next_payment_change_date=entry[92],
            index=entry[93],
            arm_cap_structure=entry[94],
            initial_interest_rate_cap=entry[95],
            periodic_interest_rate_cap=entry[96],
            lifetime_interest_rate_cap=entry[97],
            mortgage_margin=entry[98],
            arm_balloon_indicator=entry[99],
            arm_plan_number=entry[100],
            high_loan_to_value_refinance_option_indicator=entry[102],
            repurchase_make_whole_proceeds_flag=entry[104],
        )
        loan.save()

        counterparty = Counterparty(
            loan_id=loan,
            number_of_borrowers=entry[21],
            debt_to_income=entry[22],
            borrower_credit_score_at_origination=entry[23],
            coborrower_credit_score_at_origination=entry[24],
            first_time_home_buyer_indicator=FIRST_TIME_DICT[entry[25]],
            borrower_credit_score_at_issuance=entry[68],
            coborrower_credit_score_at_issuance=entry[69],
            borrower_credit_score_current=entry[70],
            coborrower_credit_score_current=entry[71],
        )
        # counterparty.save()

        enforcement = Enforcement(
            loan_id=loan,
            foreclosure_date=entry[51],
            disposition_date=entry[52],
            foreclosure_costs=entry[53],
            asset_recovery_costs=entry[55],
            net_sales_proceeds=entry[58],
            credit_enhancement_proceeds=entry[59],
            repurchase_make_whole_proceeds=entry[60],
            other_foreclosure_proceeds=entry[61],
            original_list_start_date=entry[64],
            original_list_price=entry[65],
            current_list_start_date=entry[66],
            current_list_price=entry[67],
            foreclosure_principal_writeoff_amount=entry[79],
        )
        # enforcement.save()

        forbearance = Forbearance(
            loan_id=loan,
            modification_flag=entry[41],
            noninterest_bearing_upb=entry[62],
            principal_forgiveness_amount=entry[63],
            current_period_modification_loss_amount=entry[74],
            cumulative_modification_loss_amount=entry[75],
            borrower_assistance_plan=BORROWER_PLAN_DICT[entry[101]],
            alternative_delinquency_resolution=DELINQUENCY_DICT[entry[105]],
            alternative_delinquency_resolution_count=entry[106],
            total_deferral_amount=entry[107],
        )
        # forbearance.save()

        propertycollateral = PropertyCollateral(
            loan_id=loan,
            property_type=PROPERTY_DICT[entry[27]],
            number_of_units=entry[28],
            occupancy_status=OCCUPANCY_DICT[entry[29]],
            property_state=entry[30],
            metropolitan_statistical_area=entry[31],
            zip_code_short=entry[32],
            property_preservation_and_repair_costs=entry[54],
            miscellaneous_holding_expenses_and_credits=entry[56],
            associated_taxes_for_holding_property=entry[57],
            property_valuation_method=PROPERTY_VALUATION_DICT[entry[85]],
        )
        # propertycollateral.save()

        repaymentschedule = RepaymentSchedule(
            loan_id=loan,
            remaining_months_to_legal_maturity=entry[16],
            remaining_months_to_maturity=entry[17],
            months_to_amortization=entry[38],
            loan_payment_history=entry[40],
            zero_balance_code=ZERO_BALANCE_DICT[entry[43]],
            zero_balance_effective_date=entry[44],
            upb_at_the_time_of_removal=entry[45],
            repurchase_date=entry[46],
            scheduled_principal_current=entry[47],
            total_principal_current=entry[48],
            unscheduled_principal_current=entry[49],
            last_paid_installment_date=entry[50],
            zero_balance_code_change_date=entry[81],
        )
        # repaymentschedule.save()

        # portfolio_data.append(portfolio)
        # portfoliosnapshot_data.append(portfoliosnapshot)
        # loan_data.append(loan)

        counterparty_data.append(counterparty)
        enforcement_data.append(enforcement)
        forbearance_data.append(forbearance)
        propertycollateral_data.append(propertycollateral)
        repaymentschedule_data.append(repaymentschedule)

    # Portfolio.objects.bulk_create(portfolio_data)
    # PortfolioSnapshot.objects.bulk_create(portfoliosnapshot_data)
    # Loan.objects.bulk_create(loan_data)

    Counterparty.objects.bulk_create(counterparty_data)
    Enforcement.objects.bulk_create(enforcement_data)
    Forbearance.objects.bulk_create(forbearance_data)
    PropertyCollateral.objects.bulk_create(propertycollateral_data)
    RepaymentSchedule.objects.bulk_create(repaymentschedule_data)

    # # Delete existing objects
    # Portfolio.objects.all().delete()
    #
    # # Import data from file
    # data = pd.read_csv("co.csv", header='infer', delimiter=',')
    #
    # indata = []
    # for index, entry in data.iterrows():
    #     pr = Project.objects.get(pk=entry['PROJECT'])
    #     co = Contractor(
    #         contractor_identifier=entry['PK'],
    #         project=pr,
    #         is_sme=entry['SME'],
    #         contractor_legal_entity_identifier=entry['NATIONALID'],
    #         name_of_contractor=entry['OFFICIALNAME'],
    #         address=entry['ADDRESS'],
    #         town=entry['TOWN'],
    #         postal_code=entry['POSTAL_CODE'],
    #         country=entry['COUNTRY'],
    #         phone=entry['PHONE'],
    #         email=entry['E_MAIL'],
    #         fax=entry['FAX'],
    #         region=entry['NUTS'],
    #         website=entry['URL'])
    #
    #     indata.append(co)
    #
    # Contractor.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted SFLP data into db'))
