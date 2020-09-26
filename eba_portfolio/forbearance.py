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

from django.db import models
from django.urls import reverse

"""
Data object holds Forbearance data conforming to the EBA NPL Template specification
`EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Template>`_

"""


class Forbearance(models.Model):

    #
    # CHOICE DICTIONARIES
    #

    TYPE_OF_IDENTIFIER_CHOICES = [(0, '(a) Counterparty'), (1, '(b) Loan')]

    TYPE_OF_FORBEARANCE_CHOICES = [(0, '(a) Loan maturity date extension'), (1, '(b) Amortisation change'),
                                   (2, '(c) Principal write-off'), (3, '(d) Temporary rate reduction'),
                                   (4, '(e) Capitalisation of interest'),
                                   (5, '(f) Capitalisation of costs advanced: which is insurance and ground rent'),
                                   (6, '(g) Combination '), (7, '(h) Other')]

    REPAYMENT_FREQUENCY_UNDER_FORBEARANCE_CHOICES = [(0, '(a) Monthly'), (1, '(b) Quarterly'), (2, '(c) Semi-Annually'),
                                                     (3, '(d) Annually'), (4, '(e) Daily'), (5, '(f) Other')]

    #
    # FIELDS
    #

    forbearance_identifier = models.TextField(unique=True)

    amount_of_repayment_step_up = models.FloatField(blank=True, null=True, help_text='Additional amount that the current agreed forbearance amount is increased by. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Amount_of_Repayment_Step_Up">Documentation</a>')

    clause_to_stop_forbearance = models.NullBooleanField(blank=True, null=True, help_text='Indicator as to whether a clause exists to allow the Institution to stop the current forbearance. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Clause_to_Stop_Forbearance">Documentation</a>')

    date_of_first_forbearance = models.DateField(blank=True, null=True, help_text='Date that the first forbearance happened. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Date_of_First_Forbearance">Documentation</a>')

    date_of_principal_forgiveness = models.DateField(blank=True, null=True, help_text='Date that the principal forgiveness happened. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Date_of_Principal_Forgiveness">Documentation</a>')

    date_of_repayment_step_up = models.DateField(blank=True, null=True, help_text='Date at which the current agreed forbearance amount is increased. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Date_of_Repayment_Step_Up">Documentation</a>')

    description_of_forbearance = models.TextField(blank=True, null=True, help_text='Further comments / details on the current forbearance. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Description_of_Forbearance">Documentation</a>')

    description_of_the_forbearance_clause = models.TextField(blank=True, null=True, help_text='Further comments / details on the clause if "Yes" is selected in field "Clause to Stop Forbearance". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Description_of_the_Forbearance_Clause">Documentation</a>')

    end_date_of_forbearance = models.DateField(blank=True, null=True, help_text='Date that the current forbearance arrangement ends. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.End_Date_of_Forbearance">Documentation</a>')

    institutions_internal_identifier_for_the_loan_or_counterparty = models.TextField(blank=True, null=True, help_text='Institutions internal identifier for the Counterparty or the Loan.<a class ="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Institutions_internal_identifier_for_the_Loan_or_Counterparty" > Documentation </a>')

    instrument_identifier = models.TextField(blank=True, null=True, help_text='Institutions internal identifier for the Loan part. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Instrument_Identifier">Documentation</a>')

    interest_rate_under_forbearance = models.FloatField(blank=True, null=True, help_text='Interest rate that the Institution and Counterparty agreed under the current forbearance terms. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Interest_Rate_Under_Forbearance">Documentation</a>')

    number_of_historical_forbearance = models.FloatField(blank=True, null=True, help_text='Number of forbearance(s) that happened in the past. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Number_of_Historical_Forbearance">Documentation</a>')

    principal_forgiveness = models.FloatField(blank=True, null=True, help_text='Amount of the principal that was forgiven as part of current forbearance, including principal forgiveness agreed by external collection agencies. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Principal_Forgiveness">Documentation</a>')

    repayment_amount_under_forbearance = models.FloatField(blank=True, null=True, help_text='Periodic repayment amount that the Institution and Counterparty agreed under the current forbearance terms. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Repayment_Amount_Under_Forbearance">Documentation</a>')

    repayment_frequency_under_forbearance = models.IntegerField(blank=True, null=True, choices=REPAYMENT_FREQUENCY_UNDER_FORBEARANCE_CHOICES, help_text='Frequency that the repayment under current forbearance terms is made. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Repayment_Frequency_Under_Forbearance">Documentation</a>')

    start_date_of_forbearance = models.DateField(blank=True, null=True, help_text='Date that the current forbearance arrangement starts. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Start_Date_of_Forbearance">Documentation</a>')

    type_of_forbearance = models.IntegerField(blank=True, null=True, choices=TYPE_OF_FORBEARANCE_CHOICES, help_text='Type of current forbearance. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Type_of_Forbearance">Documentation</a>')

    type_of_identifier = models.IntegerField(blank=True, null=True, choices=TYPE_OF_IDENTIFIER_CHOICES, help_text='Indicator as to whether forbearance has been prepared on a Counterparty level or a Loan level. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Forbearance.Type_of_Identifier">Documentation</a>')


    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.forbearance_identifier

    def get_absolute_url(self):
        return reverse('eba_portfolio:eba_forbearance_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Forbearance"
        verbose_name_plural = "Forbearances"

