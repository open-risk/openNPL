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

from npl_portfolio.counterparty_group import CounterpartyGroup
from npl_portfolio.counterparty import Counterparty
from npl_portfolio.enforcement import Enforcement
from npl_portfolio.external_collection import ExternalCollection
from npl_portfolio.forbearance import Forbearance
from npl_portfolio.property_collateral import PropertyCollateral
from npl_portfolio.non_property_collateral import NonPropertyCollateral
from npl_portfolio.loan import Loan


class NPLPortfolioModelTests(TestCase):

    def test_counterparty_group_str(self):
        CounterpartyGroup.objects.create(counterparty_group_identifier='test')
        instance = CounterpartyGroup.objects.get()
        self.assertEqual("test", str(instance))

    def test_counterparty_str(self):
        Counterparty.objects.create(counterparty_identifier='test')
        instance = Counterparty.objects.get()
        self.assertEqual("test", str(instance))

    def test_enforcement_str(self):
        Enforcement.objects.create(enforcement_identifier='test')
        instance = Enforcement.objects.get()
        self.assertEqual("test", str(instance))

    def test_external_collection_str(self):
        ExternalCollection.objects.create(external_collection_identifier='test')
        instance = ExternalCollection.objects.get()
        self.assertEqual("test", str(instance))

    def test_forbearance_str(self):
        Forbearance.objects.create(forbearance_identifier='test')
        instance = Forbearance.objects.get()
        self.assertEqual("test", str(instance))

    def test_loan_str(self):
        Loan.objects.create(contract_identifier='test')
        instance = Loan.objects.get()
        self.assertEqual("test", str(instance))

    def test_property_collateral_str(self):
        PropertyCollateral.objects.create(protection_identifier='test')
        instance = PropertyCollateral.objects.get()
        self.assertEqual("test", str(instance))

    def test_non_property_collateral_str(self):
        NonPropertyCollateral.objects.create(protection_identifier='test')
        instance = NonPropertyCollateral.objects.get()
        self.assertEqual("test", str(instance))


