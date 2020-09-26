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
Data object holds Counterparty Group data conforming to the EBA NPL Template specification
`EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Template>`_

"""


class CounterpartyGroup(models.Model):
    #
    # CHOICE DICTIONARIES
    #

    TYPE_OF_SPONSOR_CHOICES = [
        (0, '(a) Listed Corporate is a Corporate entity whose shares are quoted and traded on a Stock Exchange'),
        (1, '(b) Unlisted Corporate is a Corporate entity whose shares are not quoted and traded on a stock exchange, however an unlisted corporate may have an unlimited number of shareholders to raise capital for any commercial venture'),
        (2, '(c) Listed Fund is a fund whose shares are quoted and traded on a Stock exchange'),
        (3, '(d) Unlisted Fund is a fund whose shares are not quoted and traded on a Stock exchange'),
        (4, '(e) Partnership is where the Sponsor constitutes a group of individuals who form a legal partnership, where profits and liabilities are shared; or,'),
        (5, '(f) Private Individual')]

    CROSS_DEFAULT_IN_COUNTERPARTY_GROUP_CHOICES = [(0, '(a) Full'), (1, '(b) Partial'), (2, '(c) None')]

    CROSS_COLLATERALISATION_IN_COUNTERPARTY_GROUP_CHOICES = [(0, '(d) Full'), (1, '(e) Partial'), (2, '(f) None')]

    #
    # FIELDS
    #

    counterparty_group_identifier = models.TextField(unique=True)

    cross_collateralisation_in_counterparty_group = models.IntegerField(blank=True, null=True, choices=CROSS_COLLATERALISATION_IN_COUNTERPARTY_GROUP_CHOICES, help_text='Indicator as to whether all / some of the loans in the Counterparty Group are secured by all / some of the collaterals within the Counterparty Group ("Full", "Partial", "none"). <a target="_blank" class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Counterparty Group.Cross_Collateralisation_in_Counterparty_Group">Documentation</a>')

    cross_default_in_counterparty_group = models.IntegerField(blank=True, null=True, choices=CROSS_DEFAULT_IN_COUNTERPARTY_GROUP_CHOICES, help_text='The indicator as to whether Contractual breach of any loans in the Counterparty Group would trigger the contractual default event of the other loans. ("Full", "Partial", "none"). <a target="_blank" class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Counterparty Group.Cross_Default_in_Counterparty_Group">Documentation</a>')

    description_of_cross_collateralisation = models.TextField(blank=True, null=True, help_text='Description of cross collateralisation when "Partial" is selected in field "Cross Collateralisation in Borrower Group". <a target="_blank" class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Counterparty Group.Description_of_Cross_Collateralisation">Documentation</a>')

    description_of_cross_default = models.TextField(blank=True, null=True, help_text='Description of cross default when "Partial" is selected in field "Cross Default in Borrower Group". <a target="_blank" class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Counterparty Group.Description_of_Cross_Default">Documentation</a>')

    description_of_sponsor = models.TextField(blank=True, null=True,
                                              help_text='Description and related narrative on the Sponsor, e.g. the Sponsor is a high net worth individual and owns the Borrower via a fund. <a target="_blank" class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Counterparty Group.Description_of_Sponsor">Documentation</a>')

    industry_segment_of_counterparty_group = models.TextField(blank=True, null=True, help_text='Industry in which the Counterparty Group mainly operates. <a target="_blank" class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Counterparty Group.Industry_Segment_of_Counterparty_Group">Documentation</a>')

    name_of_counterparty_group = models.TextField(blank=True, null=True, help_text='Name used to refer to the Counterparty Group. <a target="_blank" class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Counterparty Group.Name_of_Counterparty_Group">Documentation</a>')

    name_of_sponsor = models.TextField(blank=True, null=True, help_text='Name used to refer to the main decision maker / key individual in relation to the Counterparty Group. <a target="_blank" class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Counterparty Group.Name_of_Sponsor">Documentation</a>')

    type_of_sponsor = models.IntegerField(blank=True, null=True, choices=TYPE_OF_SPONSOR_CHOICES, help_text='Type of entity the sponsor is i.e. Listed Corporate, Unlisted Corporate, Listed Fund, Unlisted Fund and High Net Worth Individual. <a target="_blank" class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Counterparty Group.Type_of_Sponsor">Documentation</a>')

    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.counterparty_group_identifier

    def get_absolute_url(self):
        return reverse('eba_portfolio:eba_counterparty_group_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Counterparty Group"
        verbose_name_plural = "Counterparty Groups"
