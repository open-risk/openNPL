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

from npl_portfolio.property_collateral_choices import *
from npl_portfolio.loan import Loan

class PropertyCollateral(models.Model):
    """
    The PropertyCollateral model object holds Property Collateral data conforming to the EBA NPL Template specification
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Property_Collateral_Table>`_

    """

    #
    # IDENTIFICATION FIELDS
    #

    protection_identifier = models.TextField(blank=True, null=True,
                                             help_text='Institutions internal identifier for the Property Collateral.<a class ="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Protection_identifier" >Documentation</a>')

    #
    # FOREIGN KEYS
    #

    loan_identifier = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True)

    #
    # DATA PROPERTIES
    #

    address_of_property = models.TextField(blank=True, null=True,
                                           help_text='Street address where the Property is located at, including flat / house number or name. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Address_of_Property">Documentation</a>')

    amount_of_vat_payable = models.FloatField(blank=True, null=True,
                                              help_text='Amount of VAT payable on the disposal of the Unit. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.11.05.Amount_of_VAT_Payable">Documentation</a>')

    area_type_of_property = models.IntegerField(blank=True, null=True, choices=AREA_TYPE_OF_PROPERTY_CHOICES,
                                                help_text='Area type where the Property is located at , i.e. City centre, Suburban and Rural. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Area_Type_of_Property">Documentation</a>')

    building_area_m2 = models.FloatField(blank=True, null=True,
                                         help_text='Building area (square metres) of the Unit. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Building_Area_M2">Documentation</a>')

    building_area_m2_lettable = models.FloatField(blank=True, null=True,
                                                  help_text='Building area (square metres) of the Unit that is lettable. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Building_Area_M2_Lettable">Documentation</a>')

    building_area_m2_occupied = models.FloatField(blank=True, null=True,
                                                  help_text='Building area (square metres) of the Unit that has been occupied by landlord / tenant. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Building_Area_M2_Occupied">Documentation</a>')

    city_of_property = models.TextField(blank=True, null=True,
                                        help_text='City where the Property is located at. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.City_of_Property">Documentation</a>')

    completion_of_property = models.BooleanField(blank=True, null=True,
                                                     help_text='Indicator as to whether the construction of the Unit is complete. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Completion_of_Property">Documentation</a>')

    condition_of_property = models.IntegerField(blank=True, null=True, choices=CONDITION_OF_PROPERTY_CHOICES,
                                                help_text='Quality classification of the property, e.g. Excellent, Good, Fair, Poor. and include explanation of the category, and please provide the internal methodology used to decide the categories as a part of the transaction documents. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Condition_of_Property">Documentation</a>')

    currency_of_property = models.TextField(blank=True, null=True,
                                            help_text='Currency that the valuation and cash flows related to the Unit are expressed in. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Currency_of_Property">Documentation</a>')

    current_annual_passing_rent = models.FloatField(blank=True, null=True,
                                                    help_text='Current annual passing rent charged to the Tenants of the Unit as at latest valuation date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Current_Annual_Passing_Rent">Documentation</a>')

    current_net_operating_income = models.FloatField(blank=True, null=True,
                                                     help_text='Current annual net operating income generated by the Unit as at the latest valuation date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Current_Net_Operating_Income">Documentation</a>')

    current_opex_and_overheads = models.FloatField(blank=True, null=True,
                                                   help_text='Current annual operational expenses and overheads of the Unit as at latest valuation date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Current_Opex_And_Overheads">Documentation</a>')

    date_of_initial_valuation = models.DateField(blank=True, null=True,
                                                 help_text='Date that the initial valuation was assessed. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Date_of_Initial_Valuation">Documentation</a>')

    date_of_latest_valuation = models.DateField(blank=True, null=True,
                                                help_text='Date that the latest valuation took place. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Date_of_Latest_Valuation">Documentation</a>')

    enforcement_description = models.TextField(blank=True, null=True,
                                               help_text='Comments/Description of the stage of Enforcement that the Property Collateral is in as at cut-off date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Enforcement_Description">Documentation</a>')

    enforcement_status = models.BooleanField(blank=True, null=True,
                                                 help_text='Indicator as to whether the property collateral has entered into the enforcement process as at cut-off date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Enforcement_Status">Documentation</a>')

    enforcement_status_third_parties = models.BooleanField(blank=True, null=True,
                                                               help_text='Indicator as to whether any other secured creditors have taken steps to enforce security over the asset? (Y/N). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Enforcement_Status_Third_Parties">Documentation</a>')

    estimated_annual_void_cost = models.FloatField(blank=True, null=True,
                                                   help_text='Additional costs to "Current Opex And Overheads" when the Units are vacant. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Estimated_Annual_Void_Cost">Documentation</a>')

    estimated_rental_void = models.FloatField(blank=True, null=True,
                                              help_text='Estimated number of months the property is expected to be void. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Estimated_Rental_Void">Documentation</a>')

    geographic_region_classification = models.IntegerField(blank=True, null=True,
                                                           choices=GEOGRAPHIC_REGION_CLASSIFICATION_CHOICES,
                                                           help_text='NUTS3 classification used for the field "Geographic Region of Property", i.e. NUTS3 2013 (1), NUTS3 2010 (2), NUTS3 2006 (3), NUTS3 2003 (4), Other (5). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Geographic_Region_Classification">Documentation</a>')

    geographic_region_of_property = models.TextField(blank=True, null=True,
                                                     help_text='Province / Region where the Property is located at. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.11.01.Property Collateral.Geographic_Region_of_Property">Documentation</a>')

    initial_estimated_rental_value = models.FloatField(blank=True, null=True,
                                                       help_text='Estimated annual gross rental value of the Unit assessed at loan origination. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Initial_Estimated_Rental_Value">Documentation</a>')

    initial_valuation_amount = models.FloatField(blank=True, null=True,
                                                 help_text='Value of the Unit assessed at loan origination. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.11.03.Initial_Valuation_Amount">Documentation</a>')

    internal_or_external_initial_valuation = models.IntegerField(blank=True, null=True,
                                                                 choices=INTERNAL_or_EXTERNAL_INITIAL_VALUATION_CHOICES,
                                                                 help_text='Indicator as to whether the initial valuation was outsource, or done internally. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Internal_or_External_Initial_Valuation">Documentation</a>')

    internal_or_external_latest_valuation = models.IntegerField(blank=True, null=True,
                                                                choices=INTERNAL_or_EXTERNAL_LATEST_VALUATION_CHOICES,
                                                                help_text='Indicator as to whether the latest valuation was performed internally or by an external appraiser. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Internal_or_External_Latest_Valuation">Documentation</a>')

    land_area_m2 = models.FloatField(blank=True, null=True,
                                     help_text='Land area (square metres) of the Property. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Land_Area_M2">Documentation</a>')

    latest_estimated_rental_value = models.FloatField(blank=True, null=True,
                                                      help_text='Estimated annual gross rental value of the Unit when last assessed. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Latest_Estimated_Rental_Value">Documentation</a>')

    latest_valuation_amount = models.FloatField(blank=True, null=True,
                                                help_text='Value of the Unit when last assessed. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Latest_Valuation_Amount">Documentation</a>')

    legal_owner_of_the_property = models.TextField(blank=True, null=True,
                                                   help_text='Legal owner of the Property Collateral. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Legal_Owner_of_the_Property">Documentation</a>')

    number_of_bedrooms = models.FloatField(blank=True, null=True,
                                           help_text='Number of bedrooms that the Unit has. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Number_of_Bedrooms">Documentation</a>')

    number_of_car_parking_spaces = models.FloatField(blank=True, null=True,
                                                     help_text='Number of car parking spaces relating to the Unit. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Number_of_Car_Parking_Spaces">Documentation</a>')

    number_of_lettable_units = models.FloatField(blank=True, null=True,
                                                 help_text='Number of lettable units that the Property has. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Number_of_Lettable_Units">Documentation</a>')

    number_of_rooms = models.FloatField(blank=True, null=True,
                                        help_text='Number of rooms that the Unit has excluding kitchen and bathroom(s). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.11.02.Number_of_Rooms">Documentation</a>')

    number_of_units_occupied = models.FloatField(blank=True, null=True,
                                                 help_text='Number of occupied lettable units that the Property has. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Number_of_Units_Occupied">Documentation</a>')

    number_of_units_vacant = models.FloatField(blank=True, null=True,
                                               help_text='Number of vacant lettable units that the Property has. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Number_of_Units_Vacant">Documentation</a>')

    party_liable_for_vat = models.IntegerField(blank=True, null=True, choices=PARTY_LIABLE_FOR_VAT_CHOICES,
                                               help_text='Party who is liable to pay the VAT on the disposal of the Unit i.e. the Institution or the buyer(s). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Party_Liable_for_VAT">Documentation</a>')

    percentage_complete = models.FloatField(blank=True, null=True,
                                            help_text='The percentage of development completed since construction started (applicable to Units in development). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Percentage_complete">Documentation</a>')

    planned_capex_next_12m = models.FloatField(blank=True, null=True,
                                               help_text='Current planned CAPEX for the next 12 months. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Planned_Capex_next_12m">Documentation</a>')

    property_country = models.TextField(blank=True, null=True,
                                        help_text='Country of residence where the Property is located at. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Property_Country">Documentation</a>')

    property_postcode = models.TextField(blank=True, null=True,
                                         help_text='Postcode where the Property is located at. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Property_Postcode">Documentation</a>')

    provider_of_energy_performance_certificate = models.TextField(blank=True, null=True,
                                                                  help_text='Name of the provider of the energy performance certificate. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Provider_of_Energy_Performance_Certificate">Documentation</a>')

    provider_of_initial_valuation = models.TextField(blank=True, null=True,
                                                     help_text='Name of the external appraiser or managing / estate agent is when "Full Appraisal" or "Managing / Estate Agent" is selected in field "Type of Initial Valuation". If the valuation was done internally, please select "Internal". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Provider_of_Initial_Valuation">Documentation</a>')

    provider_of_latest_valuation = models.TextField(blank=True, null=True,
                                                    help_text='Name of the external appraiser or managing / estate agent when "Full Appraisal" or "Managing / Estate Agent" is selected in field "Type of Latest Valuation". If the valuation was done internally, please select "Internal". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.11.04.Provider_of_Latest_Valuation">Documentation</a>')

    purpose_of_property = models.IntegerField(blank=True, null=True, choices=PURPOSE_OF_PROPERTY_CHOICES,
                                              help_text='Purpose of the Property, e.g. Investment property, owner occupied, Business Use, etc.. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Purpose_of_Property">Documentation</a>')

    register_of_deeds_number = models.TextField(blank=True, null=True,
                                                help_text='Registration number of the Property. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Register_of_Deeds_Number">Documentation</a>')

    remaining_term_of_leasehold = models.FloatField(blank=True, null=True,
                                                    help_text='Remaining term of the leasehold when "Leasehold" is selected in field "Tenure". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Remaining_Term_of_Leasehold">Documentation</a>')

    sector_of_property = models.IntegerField(blank=True, null=True, choices=SECTOR_OF_PROPERTY_CHOICES,
                                             help_text='Sector which the property is used for, e.g. commercial real estate, residential real estate, etc.. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Sector_of_Property">Documentation</a>')

    tenure = models.IntegerField(blank=True, null=True, choices=TENURE_CHOICES,
                                 help_text='Conditions that the Property is held or occupied, e.g. freehold and leasehold. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Tenure">Documentation</a>')

    type_of_initial_valuation = models.IntegerField(blank=True, null=True, choices=TYPE_OF_INITIAL_VALUATION_CHOICES,
                                                    help_text='Type of the initial valuation for the Unit i.e. Full Appraisal, Drive-by, Automated Valuation Model, Indexed, Desktop, Managing / Estate Agent, Purchase Price, Hair Cut, Mark to market and Borrowers Valuation. <a class ="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Type_of_Initial_Valuation" >Documentation</a>')

    type_of_latest_valuation = models.IntegerField(blank=True, null=True, choices=TYPE_OF_LATEST_VALUATION_CHOICES,
                                                   help_text='Type of the latest valuation for the Unit i.e. Full Appraisal, Drive-by, Automated Valuation Model, Indexed, Desktop, Managing / Estate Agent, Purchase Price, Hair Cut, Mark to market and Internal Institution Valuation. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Type_of_Latest_Valuation">Documentation</a>')

    type_of_occupancy = models.IntegerField(blank=True, null=True, choices=TYPE_OF_OCCUPANCY_CHOICES,
                                            help_text='Type of occupancy, i.e. owner occupied, tenanted, not tenanted. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Type_of_Occupancy">Documentation</a>')

    type_of_property = models.IntegerField(blank=True, null=True, choices=TYPE_OF_PROPERTY_CHOICES,
                                           help_text='Type of the Property, e.g. Apartment, Semi Detached House, Terraced House, Land, etc.. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Type_of_Property">Documentation</a>')

    value_of_energy_performance_certificate = models.IntegerField(blank=True, null=True,
                                                                  choices=VALUE_OF_ENERGY_PERFORMANCE_CERTIFICATE_CHOICES,
                                                                  help_text='Value stated on Energy Performance Certificate, i.e. A,B,C,D,E,F and G. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Value_of_Energy_Performance_Certificate">Documentation</a>')

    vat_payable = models.BooleanField(blank=True, null=True,
                                          help_text='Indicator as to whether the VAT is payable on the disposal of the Unit. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.VAT_Payable">Documentation</a>')

    year_of_construction = models.DateField(blank=True, null=True,
                                            help_text='Year that the Property was completed and refurbished. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Year_of_Construction">Documentation</a>')

    year_of_refurbishment = models.DateField(blank=True, null=True,
                                             help_text='Year in which the last significantly refurbished was completed. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Property Collateral.Year_of_Refurbishment">Documentation</a>')

    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.protection_identifier

    def get_absolute_url(self):
        return reverse('npl_portfolio:property_collateral_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Property Collateral"
        verbose_name_plural = "Property Collateral"
