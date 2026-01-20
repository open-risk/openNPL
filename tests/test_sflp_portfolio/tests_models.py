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


from django.test import TestCase

from sflp_portfolio.models.counterparty import Counterparty
from sflp_portfolio.models.enforcement import Enforcement
from sflp_portfolio.models.forbearance import Forbearance
from sflp_portfolio.models.property_collateral import PropertyCollateral
from sflp_portfolio.models.loan import Loan


class PortfolioModelTests(TestCase):

    def test_counterparty_str(self):
        Counterparty.objects.create(counterparty_identifier='test')
        instance = Counterparty.objects.get()
        self.assertEqual("test", instance.counterparty_identifier)

    def test_enforcement_str(self):
        Enforcement.objects.create(asset_recovery_costs=10.0)
        instance = Enforcement.objects.get()
        self.assertEqual(10.0, instance.asset_recovery_costs)

    def test_forbearance_str(self):
        Forbearance.objects.create(noninterest_bearing_upb=10000)
        instance = Forbearance.objects.get()
        self.assertEqual(10000, instance.noninterest_bearing_upb)

    def test_loan_str(self):
        Loan.objects.create(loan_identifier='test')
        instance = Loan.objects.get()
        self.assertEqual("test", instance.loan_identifier)

    def test_property_collateral_str(self):
        PropertyCollateral.objects.create(metropolitan_statistical_area='NYC')
        instance = PropertyCollateral.objects.get()
        self.assertEqual("NYC", instance.metropolitan_statistical_area)


