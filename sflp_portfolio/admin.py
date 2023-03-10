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
    # list_display = ('name', 'creation_date', 'last_change_date')


class Portfolio_SnapshotAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    # search_fields = ['name']
    # list_display = ('name', 'creation_date', 'cutoff_date')


class CounterpartyAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False


class CounterpartyStateAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False


class LoanAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    search_fields = ['loan_identifier']


class LoanStateAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('loan_id', 'portfolio_snapshot_id')


class PropertyCollateralAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False


class PropertyCollateralStateAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False


class ExternalCollectionAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False


class EnforcementAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False


class ForbearanceAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False



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
