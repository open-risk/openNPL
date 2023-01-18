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

from django.db import models
from django.urls import reverse

from sflp_portfolio.models.Loan import Loan
from sflp_portfolio.models.model_choices import *


class Counterparty(models.Model):
    #
    # IDENTIFICATION FIELDS
    #

    #
    # FOREIGN KEYS
    #

    # Loan ID Foreign Key
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True,
                                help_text="The portfolio ID to which the Counterparty belongs (can be more than one)")

    #
    # DATA PROPERTIES
    #

    borrower_credit_score_at_issuance = models.FloatField(blank=True, null=True,
                                                          help_text='A numerical value used by the financial services industry to evaluate the quality of borrower credit. Credit scores are typically based on a proprietary statistical model that is developed for use by credit data repositories. These credit repositories apply the model to borrower credit information to arrive at a credit score. When this term is used by Fannie Mae, it is referring to FICO Score 5(1) developed by Fair Isaac Corporation and provided by Equifax Inc. and is distinct from the FICO Score referenced in Fannie Maes Selling Guide, which may be provided by any of the three major credit repositories..<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    borrower_credit_score_at_origination = models.FloatField(blank=True, null=True,
                                                             help_text='A numerical value used by the financial services industry to evaluate the quality of borrower’s credit. Credit scores are typically based on a proprietary statistical model that is developed for use by credit data repositories. These credit repositories apply the model to borrower credit information to arrive at a credit score. When this term is used by Fannie Mae, it is referring to the "Classic" FICO score developed by Fair Isaac Corporation.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    borrower_credit_score_current = models.FloatField(blank=True, null=True,
                                                      help_text='A numerical value used by the financial services industry to evaluate the quality of borrower credit. Credit scores are typically based on a proprietary statistical model that is developed for use by credit data repositories. These credit repositories apply the model to borrower credit information to arrive at a credit score. When this term is used by Fannie Mae, it is referring to FICO Score 5(1) developed by Fair Isaac Corporation and provided by Equifax Inc and is distinct from the FICO Score referenced in Fannie Maes Selling Guide, which may be provided by any of the three major credit repositories.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    coborrower_credit_score_at_issuance = models.TextField(blank=True, null=True,
                                                           help_text='A numerical value used by the financial services industry to evaluate the quality of borrower credit. Credit scores are typically based on a proprietary statistical model that is developed for use by credit data repositories. These credit repositories apply the model to borrower credit information to arrive at a credit score. When this term is used by Fannie Mae, it is referring to FICO Score 5(1) developed by Fair Isaac Corporation and provided by Equifax Inc and is distinct from the FICO Score referenced in Fannie Maes Selling Guide.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    coborrower_credit_score_at_origination = models.FloatField(blank=True, null=True,
                                                               help_text='A numerical value used by the financial services industry to evaluate the quality of borrower’s credit. Credit scores are typically based on a proprietary statistical model that is developed for use by credit data repositories. These credit repositories apply the model to borrower credit information to arrive at a credit score. When this term is used by Fannie Mae, it is referring to the "Classic" FICO score developed by Fair Isaac Corporation.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    coborrower_credit_score_current = models.FloatField(blank=True, null=True,
                                                        help_text='A numerical value used by the financial services industry to evaluate the quality of borrower credit. Credit scores are typically based on a proprietary statistical model that is developed for use by credit data repositories. These credit repositories apply the model to borrower credit information to arrive at a credit score. When this term is used by Fannie Mae, it is referring to FICO Score 5(1) developed by Fair Isaac Corporation and provided by Equifax Inc and is distinct from the FICO Score referenced in Fannie Maes Selling Guide.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    debt_to_income = models.FloatField(blank=True, null=True,
                                       help_text='DTI. The ratio obtained by dividing the total monthly debt expense by the total monthly income of the borrower at the time the loan was originated.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    first_time_home_buyer_indicator = models.IntegerField(blank=True, null=True,
                                                          choices=FIRST_TIME_HOME_BUYER_INDICATOR_CHOICES,
                                                          help_text='An indicator that denotes if the borrower or co-borrower qualifies as a first-time homebuyer.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    number_of_borrowers = models.FloatField(blank=True, null=True,
                                            help_text='The number of individuals obligated to repay the mortgage loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('sflp_portfolio:Counterparty_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Counterparty"
        verbose_name_plural = "Counterparties"
