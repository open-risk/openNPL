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


from django.contrib import admin

'''
The 8 Relations (Tables) of the EBA Portfolio Template currently implemented

Portfolio is used to group obligor data into portfolios
Portfolio_Snapshot is used to group data into time snapshots

.. note:: Lease, Swap and History Tables not implemented (TODO). Relation tables between entities implemented differently (not normalized)

'''

from npl_portfolio.models import PortfolioSnapshot, Portfolio
from npl_portfolio.models import Counterparty, CounterpartyGroup
from npl_portfolio.models import Loan
from npl_portfolio.models import ExternalCollection, Enforcement
from npl_portfolio.models import NonPropertyCollateral, PropertyCollateral
from npl_portfolio.models import Forbearance


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
    list_display = ('counterparty_identifier', 'snapshot_id', 'portfolio_id',
                    'current_internal_credit_rating',
                    'occupation_description',
                    'business_description',
                    'legal_fees_accrued')
    list_filter = ('portfolio_id', 'snapshot_id', 'borrower_type')


class CounterpartyGroupAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False


class LoanAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['contract_identifier']
    list_display = ('contract_identifier', 'asset_class', 'channel_of_origination',
                    'loan_covenants',
                    'current_maturity_date',
                    'date_of_default', 'final_bullet_repayment',
                    'subsidy_amount')

    list_filter = ('asset_class', 'loan_purpose')


class PropertyCollateralAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['protection_identifier']
    list_display = ('protection_identifier', 'loan_identifier',
                    'purpose_of_property', 'tenure',
                    'area_type_of_property', 'building_area_m2_lettable',
                    'current_annual_passing_rent',
                    'date_of_latest_valuation')

    list_filter = ('purpose_of_property', 'area_type_of_property')


class ExternalCollectionAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('counterparty_identifier', 'name_of_external_debt_collection_agent')

class EnforcementAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('counterparty_identifier', 'name_of_receiver')


class NonPropertyCollateralAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['protection_identifier']
    list_display = ('protection_identifier', 'loan_identifier', 'collateral_type')

    list_filter = ('collateral_type',)


class ForbearanceAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('counterparty_identifier', 'type_of_forbearance')
    list_filter = ('type_of_forbearance',)


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
