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

AMORTIZATION_DICT = {'ARM': 0, 'FRM': 1}
AMORTIZATION_TYPE_CHOICES = [(0, '(ARM) Adjustable Rate Mortgage'), (1, '(FRM) Fixed Rate Mortgages')]

CHANNEL_DICT = {'R': 0, 'C': 1, 'B': 2}
CHANNEL_CHOICES = [(0, '(R) Retail'), (1, '(C) Correspondent'), (2, '(B) Broker')]

LOAN_PURPOSE_DICT = {'C': 0, 'R': 1, 'P': 2, 'U': 3}
LOAN_PURPOSE_CHOICES = [(0, '(C) Cash-Out Refinance'), (1, '(R) Refinance'), (2, '(P) Purchase'),
                        (3, '(U) Refinance-Not Specified')]

FIRST_TIME_DICT = {'Y': 0, 'N': 1, 'Null': 2}
FIRST_TIME_HOME_BUYER_INDICATOR_CHOICES = [(0, '(Y) Yes'), (1, '(N) No'), (2, '(Null) Unknown')]

PROPERTY_DICT = {'CO': 0, 'CP': 1, 'PU': 2, 'MH': 3, 'SF': 4}
PROPERTY_TYPE_CHOICES = [(0, '(CO) Condominium'), (1, '(CP) Co-operative'), (2, '(PU) Planned Urban Development'),
                         (3, '(MH) Manufactured Housing'), (4, '(SF) Single-Family Home')]

OCCUPANCY_DICT = {'P': 0, 'S': 1, 'I': 2, 'U': 3}
OCCUPANCY_STATUS_CHOICES = [(0, '(P) Principal'), (1, '(S) Second'), (2, '(I) Investor'), (3, '(U) Unknown')]

ZERO_BALANCE_DICT = {'01': 0, '02': 1, '03': 2, '06': 3, '09': 4, '15': 5, '16': 6, '96': 7, '97': 8, '98': 9, None:None}
ZERO_BALANCE_CODE_CHOICES = [(0, '(01) Prepaid or Matured'), (1, '(02) Third Party Sale'), (2, '(03) Short Sale'),
                             (3, '(06) Repurchased'), (4, '(09) Deed-in-Lieu; REO Disposition'),
                             (5, '(15) Notes Sales'), (6, '(16) Reperforming Loan Sale'),
                             (7, '(96) Removal (non-credit event)'), (8, '(97) Delinquency (credit event due to D180)'),
                             (9, '(98) Other Credit Event')]

MORTGAGE_INSURANCE_DICT = {'1': 0, '2': 1, '3': 2, None: None}
MORTGAGE_INSURANCE_TYPE_CHOICES = [(0, '(1) Borrower Paid'), (1, '(2) Lender Paid'), (2, '(3) Enterprise Paid'),
                                   (3, '(Null) No Mortgage Insurance')]

ELIGIBILITY_DICT = {'F': 0, 'H': 1, 'R': 2, 'O': 3, '7': 4, 'N': 5}
SPECIAL_ELIGIBILITY_PROGRAM_CHOICES = [(0, '(F) HFA Preferred'), (1, '(H) HomeReady'), (2, '(R) RefiNow'),
                                       (3, '(O) Other'), (4, '(7) Not Applicable'), (5, '(N) Not Available')]

LOAN_HOLDBACK_DICT = {'Y': 0, 'N': 1, None:2}
LOAN_HOLDBACK_INDICATOR_CHOICES = [(0, '(Y) Yes (current)'),
                                   (1, '(N) No (previously in loan hold but no longer in loan hold status)'),
                                   (2, '(Null) Has not been classified under loan hold status')]

PROPERTY_VALUATION_DICT = {'A': 0, 'P': 1, 'R': 2, 'W': 3, 'O': 4}
PROPERTY_VALUATION_METHOD_CHOICES = [(0, '(A) Appraisal'), (1, '(P) Onsite Property Data Collection'),
                                     (2, '(R) GSE Targeted Refinance'), (3, '(W) Appraisal Waiver'), (4, '(O) Other')]

BORROWER_PLAN_DICT = {'F': 0, 'R': 1, 'T': 2, 'O': 3, 'N': 4, '7': 5, '9': 6}
BORROWER_ASSISTANCE_PLAN_CHOICES = [(0, '(F) Forbearance Plan'), (1, '(R) Repayment Plan'),
                                    (2, '(T) Trial Period Plan'), (3, '(O) Other Workout Plan'),
                                    (4, '(N) No Workout Plan'), (5, '(7) Not Applicable'), (6, '(9) Not Available')]

DELINQUENCY_DICT = {'P': 0, 'C': 1, 'D': 2, 7: 3, 9: 4}
ALTERNATIVE_DELINQUENCY_RESOLUTION_CHOICES = [(0, '(P) payment deferral option'),
                                              (1, '(C) payment deferral option specific to COVID-19'), (2,
                                                                                                        '(D) payment deferral option specific to certain natural disaster related events'),
                                              (3, '(7) Not Applicable'), (4, '(9) Not Available')]
