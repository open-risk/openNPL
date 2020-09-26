# Copyright (c) 2020 Open Risk (https://www.openriskmanagement.com)
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

'''

from eba_portfolio.models import PortfolioSnapshot, Portfolio
from eba_portfolio.models import Counterparty, CounterpartyGroup
from eba_portfolio.models import Loan
from eba_portfolio.models import ExternalCollection, Enforcement
from eba_portfolio.models import NonPropertyCollateral, PropertyCollateral
from eba_portfolio.models import Forbearance


class PortfolioAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['name']
    list_display = ('name', 'user', 'creation_date', 'last_change_date')
    list_filter = ('user',)


class Portfolio_SnapshotAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['name']
    list_display = ('name', 'user', 'creation_date', 'cutoff_date', 'notes')
    list_filter = ('user',)


class CounterpartyAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['name']
    list_display = ('counterparty_identifier', 'legal_type_of_counterparty', 'portfolio_id',
                    'date_of_entering_into_current_legal_process', 'current_internal_credit_rating',
                    'legal_fees_accrued')
    list_filter = ('portfolio_id', 'legal_procedure_type',)


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


class EnforcementAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False


class NonPropertyCollateralAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False


class ForbearanceAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False


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
