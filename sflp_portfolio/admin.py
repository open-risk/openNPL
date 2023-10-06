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


from django.contrib import admin

'''
Portfolio is used to group borrower / loan data into portfolios
Portfolio_Snapshot is used to group data into time snapshots


'''

from sflp_portfolio.models.models import PortfolioSnapshot
from sflp_portfolio.models.models import Portfolio
from sflp_portfolio.models.counterparty import Counterparty
from sflp_portfolio.models.counterparty_state import CounterpartyState
from sflp_portfolio.models.loan import Loan
from sflp_portfolio.models.loan_state import LoanState
from sflp_portfolio.models.property_collateral import PropertyCollateral
from sflp_portfolio.models.property_collateral_state import PropertyCollateralState
from sflp_portfolio.models.enforcement import Enforcement
from sflp_portfolio.models.forbearance import Forbearance


class PortfolioAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    # search_fields = ['name']
    list_display = ('name', 'creation_date', 'last_change_date')


class Portfolio_SnapshotAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    # search_fields = ['monthly_reporting_period']
    list_display = ('monthly_reporting_period',)


class CounterpartyAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('counterparty_identifier', 'loan_identifier', 'debt_to_income', 'number_of_borrowers',
                    'borrower_credit_score_at_origination')


class CounterpartyStateAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    # TODO date_hierarchy = ('portfolio_snapshot_id')
    list_display = ('counterparty_identifier', 'portfolio_snapshot_id')


class LoanAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = (
        'loan_identifier', 'channel', 'original_loan_term', 'original_upb', 'original_loan_to_value_ratio',
        'loan_purpose')


class LoanStateAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('loan_identifier', 'portfolio_snapshot_id', 'servicer_name', 'total_principal_current',
                    'remaining_months_to_legal_maturity')


class PropertyCollateralAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = (
        'property_type', 'number_of_units', 'metropolitan_statistical_area', 'property_state', 'zip_code_short')


class PropertyCollateralStateAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('property_collateral_id', 'portfolio_snapshot_id', 'property_valuation_method')


class EnforcementAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('property_collateral_identifier', 'portfolio_snapshot_id',
                    'net_sales_proceeds', 'asset_recovery_costs', 'foreclosure_costs')


class ForbearanceAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('loan_identifier', 'portfolio_snapshot_id', 'modification_flag',
                    'noninterest_bearing_upb', 'principal_forgiveness_amount')


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioSnapshot, Portfolio_SnapshotAdmin)
admin.site.register(Counterparty, CounterpartyAdmin)
admin.site.register(CounterpartyState, CounterpartyStateAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(LoanState, LoanStateAdmin)
admin.site.register(PropertyCollateral, PropertyCollateralAdmin)
admin.site.register(PropertyCollateralState, PropertyCollateralStateAdmin)
admin.site.register(Enforcement, EnforcementAdmin)
admin.site.register(Forbearance, ForbearanceAdmin)
