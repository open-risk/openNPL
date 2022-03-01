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

#
# CHOICE DICTIONARIES COUNTERPARTY GROUP
#

TYPE_OF_SPONSOR_CHOICES = [
    (0, '(a) Listed Corporate is a Corporate entity whose shares are quoted and traded on a Stock Exchange'),
    (1,
     '(b) Unlisted Corporate is a Corporate entity whose shares are not quoted and traded on a stock exchange, however an unlisted corporate may have an unlimited number of shareholders to raise capital for any commercial venture'),
    (2, '(c) Listed Fund is a fund whose shares are quoted and traded on a Stock exchange'),
    (3, '(d) Unlisted Fund is a fund whose shares are not quoted and traded on a Stock exchange'),
    (4,
     '(e) Partnership is where the Sponsor constitutes a group of individuals who form a legal partnership, where profits and liabilities are shared; or,'),
    (5, '(f) Private Individual')]

CROSS_DEFAULT_IN_COUNTERPARTY_GROUP_CHOICES = [(0, '(a) Full'), (1, '(b) Partial'), (2, '(c) None')]

CROSS_COLLATERALISATION_IN_COUNTERPARTY_GROUP_CHOICES = [(0, '(a) Full'), (1, '(b) Partial'), (2, '(c) None')]
