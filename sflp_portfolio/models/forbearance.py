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

from sflp_portfolio.models.loan import Loan
from sflp_portfolio.models.model_choices import *


class Forbearance(models.Model):
    """
    The Forbearance model holds Forbearance related data. Forbearance is contingent action linked to a Loan.


    """

    #
    # IDENTIFICATION FIELDS
    #


    #
    # FOREIGN KEYS
    #

    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True,
                                help_text='The loan ID to which the Forbearance activity links.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/FM_SFLP.Loan_Identifier">Documentation</a>')
    """The loan ID to which the Forbearance activity links."""

    #
    # DYNAMIC DATA PROPERTIES
    #

    loan_holdback_effective_date = models.DateField(blank=True, null=True,
                                                    help_text='The date of the latest Loan Holdback indicator change.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    loan_holdback_indicator = models.IntegerField(blank=True, null=True, choices=LOAN_HOLDBACK_INDICATOR_CHOICES,
                                                  help_text='An indicator that denotes if a loan has been moved temporarily into a ‘hold’ status to allow Fannie Mae to further evaluate unique situations that may otherwise result in a credit event or loan removal. Such situations may include loans with reported data anomalies, loans currently in forbearance due to a natural disaster or loans refinanced under the High LTV program that will continue to be included in the reference pool.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    current_period_credit_event_net_gain_or_loss = models.FloatField(blank=True, null=True,
                                                                     help_text='The net realized gain or loss amount calculated for a mortgage loan resulting from a credit event for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    delinquent_accrued_interest = models.FloatField(blank=True, null=True,
                                                    help_text='The lost accrued interest amount calculated for a mortgage loan that becomes subject to a credit event for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    alternative_delinquency_resolution = models.IntegerField(blank=True, null=True,
                                                             choices=ALTERNATIVE_DELINQUENCY_RESOLUTION_CHOICES,
                                                             help_text='An indicator that denotes the loss mitigation solution designed to resolve delinquencies and help homeowners remain in their homes in accordance with the servicer’s contractual obligation, while allowing the loan to remain in the security.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    alternative_delinquency_resolution_count = models.FloatField(blank=True, null=True,
                                                                 help_text='The total number of Alternative Delinquency Resolutions as reported by the servicer for a specific loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    borrower_assistance_plan = models.IntegerField(blank=True, null=True, choices=BORROWER_ASSISTANCE_PLAN_CHOICES,
                                                   help_text='An indicator that denotes the type of assistance plan that the borrower is enrolled in that provides temporary mortgage payment relief or an opportunity for the borrower to cure a mortgage delinquency over a defined period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    cumulative_modification_loss_amount = models.FloatField(blank=True, null=True,
                                                            help_text='The cumulative loss amount calculated for a mortgage loan resulting from a modification event.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    current_period_modification_loss_amount = models.FloatField(blank=True, null=True,
                                                                help_text='The loss amount calculated for a mortgage loan resulting from a modification event for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    modification_flag = models.BooleanField(blank=True, null=True,
                                                help_text='An indicator that denotes if the mortgage loan has been modified.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    noninterest_bearing_upb = models.FloatField(blank=True, null=True,
                                                help_text='A portion of the UPB, as a result of an eligible loan modification, that will not accrue interest.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    principal_forgiveness_amount = models.FloatField(blank=True, null=True,
                                                     help_text='A reduction of the UPB owed on a mortgage by a borrower that is formally agreed to by the lender and the borrower, usually in conjunction with a loan modification.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    total_deferral_amount = models.FloatField(blank=True, null=True,
                                              help_text='The total non-interest-bearing deferral amount related to one or more Alternative Delinquency Resolutions.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')
    """"""

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    """The first insertion date of the data point"""

    last_change_date = models.DateTimeField(auto_now=True)
    """The last change date of the data point"""

    def __str__(self):
        """String representing the data object"""
        return "Forbearance of " + str(self.loan_id)

    def get_absolute_url(self):
        """Absolute URL where the data point can be edited"""
        return reverse('sflp_portfolio:forbearance_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Forbearance"
        verbose_name_plural = "Forbearance"