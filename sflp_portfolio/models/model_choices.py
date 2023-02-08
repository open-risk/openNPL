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


AMORTIZATION_TYPE_CHOICES = [(0, '(ARM) Adjustable Rate Mortgage'), (1, '(FRM) Fixed Rate Mortgages')]
CHANNEL_CHOICES = [(0, '(R) Retail'), (1, '(C) Correspondent'), (2, '(B) Broker')]
LOAN_PURPOSE_CHOICES = [(0, '(C) Cash-Out Refinance'), (1, '(R) Refinance'), (2, '(P) Purchase'),
                        (3, '(U) Refinance-Not Specified')]
FIRST_TIME_HOME_BUYER_INDICATOR_CHOICES = [(0, '(Y) Yes'), (1, '(N) No'), (2, '(Null) Unknown')]
PROPERTY_TYPE_CHOICES = [(0, '(CO) Condominium'), (1, '(CP) Co-operative'), (2, '(PU) Planned Urban Development'),
                         (3, '(MH) Manufactured Housing'), (4, '(SF) Single-Family Home')]
OCCUPANCY_STATUS_CHOICES = [(0, '(P) Principal'), (1, '(S) Second'), (2, '(I) Investor'), (3, '(U) Unknown')]
ZERO_BALANCE_CODE_CHOICES = [(0, '(01) Prepaid or Matured'), (1, '(02) Third Party Sale'), (2, '(03) Short Sale'),
                             (3, '(06) Repurchased'), (4, '(09) Deed-in-Lieu; REO Disposition'),
                             (5, '(15) Notes Sales'), (6, '(16) Reperforming Loan Sale'),
                             (7, '(96) Removal (non-credit event)'), (8, '(97) Delinquency (credit event due to D180)'),
                             (9, '(98) Other Credit Event')]
MORTGAGE_INSURANCE_TYPE_CHOICES = [(0, '(1) Borrower Paid'), (1, '(2) Lender Paid'), (2, '(3) Enterprise Paid'),
                                   (3, '(Null) No Mortgage Insurance')]
SPECIAL_ELIGIBILITY_PROGRAM_CHOICES = [(0, '(F) HFA Preferred'), (1, '(H) HomeReady'), (2, '(R) RefiNow'),
                                       (3, '(O) Other'), (4, '(7) Not Applicable'), (5, '(N) Not Available')]
LOAN_HOLDBACK_INDICATOR_CHOICES = [(0, '(Y) Yes (current)'),
                                   (1, '(N) No (previously in loan hold but no longer in loan hold status)'),
                                   (2, '(Null) Has not been classified under loan hold status')]
PROPERTY_VALUATION_METHOD_CHOICES = [(0, '(A) Appraisal'), (1, '(P) Onsite Property Data Collection'),
                                     (2, '(R) GSE Targeted Refinance'), (3, '(W) Appraisal Waiver'), (4, '(O) Other')]
BORROWER_ASSISTANCE_PLAN_CHOICES = [(0, '(F) Forbearance Plan'), (1, '(R) Repayment Plan'),
                                    (2, '(T) Trial Period Plan'), (3, '(O) Other Workout Plan'),
                                    (4, '(N) No Workout Plan'), (5, '(7) Not Applicable'), (6, '(9) Not Available')]
ALTERNATIVE_DELINQUENCY_RESOLUTION_CHOICES = [(0, '(P) payment deferral option'),
                                              (1, '(C) payment deferral option specific to COVID-19'), (2,
                                                                                                        '(D) payment deferral option specific to certain natural disaster related events'),
                                              (3, '(7) Not Applicable'), (4, '(9) Not Available')]
