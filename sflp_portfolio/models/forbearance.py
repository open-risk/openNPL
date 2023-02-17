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
    The Forbearance model holds Forbearance related data

    .. note:: The Agency Single Family Loan Performance Template does not explicitly segment data attributes into Counterparty, Loan etc. The assignment into tables (models) in openNPL is based on the interpretation and main function of different data fields

    .. note:: Fields are currently segmented into static and dynamic. In the future dynamic attributes may move to new models. The distinction is not always clear and may depend on the availability of updated date

    """

    #
    # IDENTIFICATION FIELDS
    #


    #
    # FOREIGN KEYS
    #

    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True)


    #
    # DYNAMIC DATA PROPERTIES
    #
    alternative_delinquency_resolution = models.IntegerField(blank=True, null=True,
                                                             choices=ALTERNATIVE_DELINQUENCY_RESOLUTION_CHOICES,
                                                             help_text='An indicator that denotes the loss mitigation solution designed to resolve delinquencies and help homeowners remain in their homes in accordance with the servicer’s contractual obligation, while allowing the loan to remain in the security.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    alternative_delinquency_resolution_count = models.FloatField(blank=True, null=True,
                                                                 help_text='The total number of Alternative Delinquency Resolutions as reported by the servicer for a specific loan.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    borrower_assistance_plan = models.IntegerField(blank=True, null=True, choices=BORROWER_ASSISTANCE_PLAN_CHOICES,
                                                   help_text='An indicator that denotes the type of assistance plan that the borrower is enrolled in that provides temporary mortgage payment relief or an opportunity for the borrower to cure a mortgage delinquency over a defined period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    cumulative_modification_loss_amount = models.FloatField(blank=True, null=True,
                                                            help_text='The cumulative loss amount calculated for a mortgage loan resulting from a modification event.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_period_modification_loss_amount = models.FloatField(blank=True, null=True,
                                                                help_text='The loss amount calculated for a mortgage loan resulting from a modification event for the corresponding reporting period.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    modification_flag = models.BooleanField(blank=True, null=True,
                                                help_text='An indicator that denotes if the mortgage loan has been modified.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    noninterest_bearing_upb = models.FloatField(blank=True, null=True,
                                                help_text='A portion of the UPB, as a result of an eligible loan modification, that will not accrue interest.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    principal_forgiveness_amount = models.FloatField(blank=True, null=True,
                                                     help_text='A reduction of the UPB owed on a mortgage by a borrower that is formally agreed to by the lender and the borrower, usually in conjunction with a loan modification.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    total_deferral_amount = models.FloatField(blank=True, null=True,
                                              help_text='The total non-interest-bearing deferral amount related to one or more Alternative Delinquency Resolutions.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('sflp_portfolio:forbearance_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Forbearance"
        verbose_name_plural = "Forbearance"