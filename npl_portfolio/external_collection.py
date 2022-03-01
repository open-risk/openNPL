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

from django.db import models
from django.urls import reverse

from npl_portfolio.external_collection_choices import *
from npl_portfolio.loan import Loan
from npl_portfolio.counterparty import Counterparty


class ExternalCollection(models.Model):
    """
    The ExternalCollection model holds External Collection data conforming to the EBA NPL Template specification
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_External_Collection_Table>`_

    .. note:: The EBA Templates make a distinction between collections at loan and counterparty level. At present this is not implemented

    """

    #
    # IDENTIFICATION FIELDS
    #

    external_collection_identifier = models.TextField(blank=True, null=True)

    institutions_internal_identifier_for_the_loan_or_counterparty = models.TextField(blank=True, null=True,
                                                                                     help_text='Institutions internal identifier for the Counterparty or the Loan.<a class ="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Institutions_internal_identifier_for_the_Loan_or_Counterparty" >Documentation</a>')

    instrument_identifier = models.TextField(blank=True, null=True,
                                             help_text='Institutions internal identifier for the Loan part. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Instrument_Identifier">Documentation</a>')

    type_of_identifier = models.IntegerField(blank=True, null=True, choices=TYPE_OF_IDENTIFIER_CHOICES,
                                             help_text='Indicator as to whether the external collections have been prepares on a Counterparty level or on a Loan Level. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Type_of_Identifier">Documentation</a>')

    #
    # FOREIGN KEYS
    #

    loan_identifier = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True)

    counterparty_identifier = models.ForeignKey(Counterparty, on_delete=models.CASCADE, null=True, blank=True)

    #
    # DATA PROPERTIES
    #

    balance_amount_sent_to_agent = models.FloatField(blank=True, null=True,
                                                     help_text='The Balance that was sent to the External Debt Collection Agent. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Balance_Amount_Sent_to_Agent">Documentation</a>')

    cash_recoveries = models.FloatField(blank=True, null=True,
                                        help_text='Total cash recoveries collected by the external collection agent. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Cash_Recoveries">Documentation</a>')

    costs_accrued = models.FloatField(blank=True, null=True,
                                      help_text='Total amount of costs accrued for external collection as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Costs_Accrued">Documentation</a>')

    date_returned_from_agent = models.DateField(blank=True, null=True,
                                                help_text='Date that the Loan was received back from the external collection agent, i.e. when the agent stopped recovery efforts and passed the Loan back to the Institution. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Date_Returned_From_Agent">Documentation</a>')

    date_sent_to_agent = models.DateField(blank=True, null=True,
                                          help_text='Date that the Loan was sent to the external collection agent. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Date_Sent_to_Agent">Documentation</a>')

    legal_entity_identifier = models.TextField(blank=True, null=True,
                                               help_text='Global standard 20-character corporate identifier of the external collection agent. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Legal_entity_identifier">Documentation</a>')

    name_of_external_debt_collection_agent = models.TextField(blank=True, null=True,
                                                              help_text='Name of the external collection agent. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Name_of_External_Debt_Collection_Agent">Documentation</a>')

    principal_forgiveness = models.FloatField(blank=True, null=True,
                                              help_text='Amount of the principal that was forgiven by the external collection agent as part of recovery negotiations. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Principal_Forgiveness">Documentation</a>')

    quantity_returned_from_agent = models.FloatField(blank=True, null=True,
                                                     help_text='Amount of times the at the Loan was received back from the external debt collection agent. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Quantity_Returned_From_Agent">Documentation</a>')

    registration_number = models.TextField(blank=True, null=True,
                                           help_text='Company registration number of the external collection agent according to the registration with the country specific registration office. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Registration_number">Documentation</a>')

    repayment_plan = models.BooleanField(blank=True, null=True,
                                             help_text='Indicator as to whether a repayment plan has been agreed with the external collection agency. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Repayment_Plan">Documentation</a>')

    repayment_plan_description = models.TextField(blank=True, null=True,
                                                  help_text='Description of the repayment plan which has been agreed with the external collection agency. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.External Collection.Repayment_Plan_Description">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.external_collection_identifier

    def get_absolute_url(self):
        return reverse('npl_portfolio:external_collection_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "External Collection"
        verbose_name_plural = "External Collections"
