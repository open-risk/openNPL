# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
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

from npl_portfolio.eba_field_helpers import mandatory_help, recommended_help, legacy_help
from npl_portfolio.loan import Loan
from npl_portfolio.property_collateral_choices import *


class PropertyCollateral(models.Model):
    """
    The PropertyCollateral model object holds Property Collateral data conforming to the EBA NPL Template specification
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Property_Collateral_Table>`_

    """

    #
    # IDENTIFICATION FIELDS
    #

    protection_identifier = models.TextField(blank=True, null=True,
                                             help_text=mandatory_help('4.00', "Institution's internal identifier to uniquely identify each protection (collateral or guarantee) used to secure the loan."))

    #
    # FOREIGN KEYS (Template 2 — Relationship)
    #

    loan_identifier = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True,
                                        help_text=mandatory_help('2.01', "Institution's internal identifier of the loan secured by this property collateral."))

    #
    # EBA ITS 2023/2083 — MANDATORY FIELDS (Template 4)
    #

    type_of_property = models.IntegerField(blank=True, null=True, choices=TYPE_OF_PROPERTY_CHOICES,
                                           help_text=mandatory_help('4.01', "Type of the immovable property collateral (office, retail, industrial, residential, other). Applicable to all immovable (real estate) collateral."))

    address_of_property = models.TextField(blank=True, null=True,
                                           help_text=mandatory_help('4.03', "Street address where the immovable property is located, including flat/house number or name. Applicable to all immovable collateral."))

    city_of_property = models.TextField(blank=True, null=True,
                                        help_text=mandatory_help('4.04', "City where the immovable property is located, per UN/LOCODE. Applicable to all immovable collateral."))

    property_postcode = models.TextField(blank=True, null=True,
                                         help_text=mandatory_help('4.05', "Postcode where the immovable property is located. Applicable to all immovable collateral, unless there is no postal code for land or alike."))

    property_country = models.TextField(blank=True, null=True,
                                        help_text=mandatory_help('4.06', "Region or country where the immovable property collateral is located, per ISO 3166 ALPHA-2."))

    lien_position = models.IntegerField(blank=True, null=True,
                                        help_text=mandatory_help('4.09', "Highest lien position held by the institution on the immovable property collateral. Applicable if the lien is recorded in the official deed records."))

    higher_ranking_loan = models.FloatField(blank=True, null=True,
                                            help_text=mandatory_help('4.10', "Amount that higher-ranking lien holders are entitled to receive before the institution in a foreclosure. Applicable if the institution does not hold the first position lien."))

    currency_of_property = models.TextField(blank=True, null=True,
                                            help_text=mandatory_help('4.18', "Currency that the valuation and cash flows related to the collateral or guarantee are expressed in, per ISO 4217."))

    latest_valuation_amount = models.FloatField(blank=True, null=True,
                                                help_text=mandatory_help('4.19', "Value of the collateral as established following the chosen internal valuation approach when last assessed at or prior to Cut-Off Date, without regulatory haircuts."))

    date_of_latest_valuation = models.DateField(blank=True, null=True,
                                                help_text=mandatory_help('4.20', "Date that the latest internal valuation took place at or prior to Cut-Off Date."))

    type_of_appraisal_amount_internal = models.IntegerField(blank=True, null=True, choices=TYPE_OF_APPRAISAL_AMOUNT_CHOICES,
                                                            help_text=mandatory_help('4.21', "Type of appraisal amount for the latest internal valuation (market value, liquidation value, book value, other)."))

    latest_external_valuation_amount = models.FloatField(blank=True, null=True,
                                                         help_text=mandatory_help('4.23', "Value of the collateral as established following the chosen external valuation approach when last assessed at or prior to Cut-Off Date, without regulatory haircuts."))

    date_of_latest_external_valuation = models.DateField(blank=True, null=True,
                                                         help_text=mandatory_help('4.24', "Date that the latest external valuation took place at or prior to Cut-Off Date."))

    type_of_appraisal_amount_external = models.IntegerField(blank=True, null=True, choices=TYPE_OF_APPRAISAL_AMOUNT_CHOICES,
                                                            help_text=mandatory_help('4.25', "Type of appraisal amount for the latest external valuation (market value, liquidation value, book value, other)."))

    enforcement_status = models.BooleanField(blank=True, null=True,
                                             help_text=mandatory_help('4.29', "Indicator as to whether the collateral has entered into the enforcement process at Cut-Off Date."))

    #
    # EBA ITS 2023/2083 — RECOMMENDED FIELDS (Template 4)
    #

    cadaster_id_number = models.TextField(blank=True, null=True,
                                          help_text=recommended_help('4.07', "Identification number under which the immovable property collateral is recorded in the cadaster."))

    cadaster_identification = models.TextField(blank=True, null=True,
                                               help_text=recommended_help('4.08', "Name and/or identification code of the official cadaster showing details of ownership, boundaries and value of the immovable property."))

    register_of_deeds_number = models.TextField(blank=True, null=True,
                                                help_text=recommended_help('4.11', "Registration number under which the institution's lien is recorded in the official deed records. Applicable if the institution has a lien on the collateral."))

    building_area_m2 = models.FloatField(blank=True, null=True,
                                         help_text=recommended_help('4.13', "Building area (square metres) of the immovable property. Applicable to all immovable collateral."))

    land_area_m2 = models.FloatField(blank=True, null=True,
                                     help_text=recommended_help('4.14', "Land area surrounding the immovable property (square metres). Applicable to all immovable collateral."))

    completion_of_property = models.BooleanField(blank=True, null=True,
                                                 help_text=recommended_help('4.15', "Indicator as to whether the construction of the immovable property is complete."))

    value_of_energy_performance_certificate = models.IntegerField(blank=True, null=True,
                                                                  choices=VALUE_OF_ENERGY_PERFORMANCE_CERTIFICATE_CHOICES,
                                                                  help_text=recommended_help('4.16', "Value stated on the Energy Performance Certificate per EU Energy Efficiency Directive 2012 (A–G). Applicable to all immovable collateral."))

    type_of_occupancy = models.IntegerField(blank=True, null=True, choices=TYPE_OF_OCCUPANCY_CHOICES,
                                            help_text=recommended_help('4.17', "Type of occupancy for immovable property collateral (Owner-occupied, Rented, Other). For mixed use, classify by dominant use."))

    type_of_latest_valuation = models.IntegerField(blank=True, null=True, choices=TYPE_OF_LATEST_VALUATION_CHOICES,
                                                   help_text=recommended_help('4.22', "Type of the latest internal valuation (e.g. Full Appraisal, Drive-by, Automated Valuation Model, Indexed, Desktop, Managing/Estate Agent, Purchase Price)."))

    type_of_latest_external_valuation = models.IntegerField(blank=True, null=True, choices=TYPE_OF_LATEST_VALUATION_CHOICES,
                                                            help_text=recommended_help('4.26', "Type of the latest external valuation (e.g. Full Appraisal, Drive-by, Automated Valuation Model, Indexed, Desktop, Managing/Estate Agent, Purchase Price)."))

    enforcement_status_third_parties = models.BooleanField(blank=True, null=True,
                                                           help_text=recommended_help('4.30', "Indicator as to whether any other secured creditors have taken steps to enforce security over the collateral at Cut-Off Date."))

    year_of_construction = models.IntegerField(blank=True, null=True,
                                              help_text=recommended_help('4.12', 'Year that the immovable property was built/completed. Applicable to all immovable collateral.'))

    #
    # LEGACY DATA PROPERTIES (pre-2023 EBA draft — not in EU 2023/2083)
    #

    amount_of_vat_payable = models.FloatField(blank=True, null=True,
                                              help_text=legacy_help('Amount of VAT payable on the disposal of the unit.'))

    area_type_of_property = models.IntegerField(blank=True, null=True, choices=AREA_TYPE_OF_PROPERTY_CHOICES,
                                                help_text=legacy_help('Area type where the property is located (City centre, Suburban, Rural).'))

    building_area_m2_lettable = models.FloatField(blank=True, null=True,
                                                  help_text=legacy_help('Building area (square metres) of the unit that is lettable.'))

    building_area_m2_occupied = models.FloatField(blank=True, null=True,
                                                  help_text=legacy_help('Building area (square metres) of the unit that has been occupied by landlord/tenant.'))

    condition_of_property = models.IntegerField(blank=True, null=True, choices=CONDITION_OF_PROPERTY_CHOICES,
                                                help_text=legacy_help('Quality classification of the property (Excellent, Good, Fair, Poor).'))

    current_annual_passing_rent = models.FloatField(blank=True, null=True,
                                                    help_text=legacy_help('Current annual passing rent charged to tenants at latest valuation date.'))

    current_net_operating_income = models.FloatField(blank=True, null=True,
                                                     help_text=legacy_help('Current annual net operating income generated by the unit at latest valuation date.'))

    current_opex_and_overheads = models.FloatField(blank=True, null=True,
                                                   help_text=legacy_help('Current annual operational expenses and overheads of the unit at latest valuation date.'))

    date_of_initial_valuation = models.DateField(blank=True, null=True,
                                                 help_text=legacy_help('Date that the initial valuation was assessed.'))

    enforcement_description = models.TextField(blank=True, null=True,
                                               help_text=legacy_help('Comments/description of the stage of enforcement that the property collateral is in at cut-off date.'))

    estimated_annual_void_cost = models.FloatField(blank=True, null=True,
                                                   help_text=legacy_help('Additional costs when the units are vacant, on top of current Opex and overheads.'))

    estimated_rental_void = models.FloatField(blank=True, null=True,
                                              help_text=legacy_help('Estimated number of months the property is expected to be void.'))

    geographic_region_classification = models.IntegerField(blank=True, null=True,
                                                           choices=GEOGRAPHIC_REGION_CLASSIFICATION_CHOICES,
                                                           help_text=legacy_help('NUTS3 classification version used for the geographic region of the property.'))

    geographic_region_of_property = models.TextField(blank=True, null=True,
                                                     help_text=legacy_help('Province/Region where the property is located.'))

    initial_estimated_rental_value = models.FloatField(blank=True, null=True,
                                                       help_text=legacy_help('Estimated annual gross rental value of the unit assessed at loan origination.'))

    initial_valuation_amount = models.FloatField(blank=True, null=True,
                                                 help_text=legacy_help('Value of the unit assessed at loan origination.'))

    internal_or_external_initial_valuation = models.IntegerField(blank=True, null=True,
                                                                 choices=INTERNAL_or_EXTERNAL_INITIAL_VALUATION_CHOICES,
                                                                 help_text=legacy_help('Indicator as to whether the initial valuation was outsourced or done internally.'))

    internal_or_external_latest_valuation = models.IntegerField(blank=True, null=True,
                                                                choices=INTERNAL_or_EXTERNAL_LATEST_VALUATION_CHOICES,
                                                                help_text=legacy_help('Indicator as to whether the latest valuation was performed internally or by an external appraiser.'))

    latest_estimated_rental_value = models.FloatField(blank=True, null=True,
                                                      help_text=legacy_help('Estimated annual gross rental value of the unit when last assessed.'))

    legal_owner_of_the_property = models.TextField(blank=True, null=True,
                                                   help_text=legacy_help('Legal owner of the property collateral.'))

    number_of_bedrooms = models.FloatField(blank=True, null=True,
                                           help_text=legacy_help('Number of bedrooms that the unit has.'))

    number_of_car_parking_spaces = models.FloatField(blank=True, null=True,
                                                     help_text=legacy_help('Number of car parking spaces relating to the unit.'))

    number_of_lettable_units = models.FloatField(blank=True, null=True,
                                                 help_text=legacy_help('Number of lettable units that the property has.'))

    number_of_rooms = models.FloatField(blank=True, null=True,
                                        help_text=legacy_help('Number of rooms that the unit has, excluding kitchen and bathroom(s).'))

    number_of_units_occupied = models.FloatField(blank=True, null=True,
                                                 help_text=legacy_help('Number of occupied lettable units that the property has.'))

    number_of_units_vacant = models.FloatField(blank=True, null=True,
                                               help_text=legacy_help('Number of vacant lettable units that the property has.'))

    party_liable_for_vat = models.IntegerField(blank=True, null=True, choices=PARTY_LIABLE_FOR_VAT_CHOICES,
                                               help_text=legacy_help('Party liable to pay the VAT on the disposal of the unit (the institution or the buyer).'))

    percentage_complete = models.FloatField(blank=True, null=True,
                                            help_text=legacy_help('Percentage of development completed since construction started (applicable to units in development).'))

    planned_capex_next_12m = models.FloatField(blank=True, null=True,
                                               help_text=legacy_help('Current planned CAPEX for the next 12 months.'))

    provider_of_energy_performance_certificate = models.TextField(blank=True, null=True,
                                                                  help_text=legacy_help('Name of the provider of the energy performance certificate.'))

    provider_of_initial_valuation = models.TextField(blank=True, null=True,
                                                     help_text=legacy_help('Name of the external appraiser or managing/estate agent for the initial valuation.'))

    provider_of_latest_valuation = models.TextField(blank=True, null=True,
                                                    help_text=legacy_help('Name of the external appraiser or managing/estate agent for the latest valuation.'))

    purpose_of_property = models.IntegerField(blank=True, null=True, choices=PURPOSE_OF_PROPERTY_CHOICES,
                                              help_text=legacy_help('Purpose of the property (Investment property, Owner occupied, Business use, etc.).'))

    remaining_term_of_leasehold = models.FloatField(blank=True, null=True,
                                                    help_text=legacy_help('Remaining term of the leasehold when "Leasehold" is selected in "Tenure".'))

    sector_of_property = models.IntegerField(blank=True, null=True, choices=SECTOR_OF_PROPERTY_CHOICES,
                                             help_text=legacy_help('Sector for which the property is used (commercial real estate, residential real estate, etc.).'))

    tenure = models.IntegerField(blank=True, null=True, choices=TENURE_CHOICES,
                                 help_text=legacy_help('Conditions that the property is held or occupied (freehold, leasehold).'))

    type_of_initial_valuation = models.IntegerField(blank=True, null=True, choices=TYPE_OF_INITIAL_VALUATION_CHOICES,
                                                    help_text=legacy_help('Type of the initial valuation (Full Appraisal, Drive-by, Automated Valuation Model, Indexed, Desktop, etc.).'))

    vat_payable = models.BooleanField(blank=True, null=True,
                                      help_text=legacy_help('Indicator as to whether VAT is payable on the disposal of the unit.'))

    year_of_refurbishment = models.DateField(blank=True, null=True,
                                             help_text=legacy_help('Year in which the last significant refurbishment was completed.'))

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
