import country as c
import math
from country import Country
from operator import attrgetter

# Global Vars


# def find_negative_country(curr_country: Country) -> Country:
#     temp_list = c.country_master_list
#     temp_list.reverse
#     for country in temp_list:
#         if country.surplus() < 0:
#             return country


# def find_poor_country(curr_country: Country) -> Country:
#     temp_master_list = c.country_master_list
#     temp_master_list.sort(key=attrgetter("gdp"))
#     for country in temp_master_list:
#         if country.surplus() < 2:
#             return country
def test_total_vaccines():
    total = 0
    for country in c.country_master_list:
        total += country.num_vaccines
    return total


def balance() -> int:
    """ 
    The balance function redistributes vaccines fairly and is done in two stages:
    Returns the amount of vaccines needed to balance
    Stage 1:
    - Calculate the total amount of vaccine surplus
    - Divide the surplus by the amount of countries in a deficit
    - Distribute the vaccines to the deficit countries equally
        * If one country has less deficit than the amount distributed to them
        only give the amount they need.
    If after distribution there are extra surplus left, the surplus will
    be redistributed to the surplus countries.
    *** IMPORTANT ***
    The distribution plot will be outputted after this stage.


    Stage 2:
    If there are still deficits:
    Calculate the amount of vaccines needed to balance,
    Include this amount in final graph.
    """

    #STAGE 1
    deficit_countries = {}
    surplus_countries = {}

    # # Find the countries that are in a deficit of vaccines and surpluses
    for country in c.country_master_list:
         if country.surplus() < 0:
             deficit_countries[country] = country.surplus()
         else:
             surplus_countries[country] = country.surplus()
    
    #order the countries from greatest to least deficits
    deficit_countries = {k: v for k, v in sorted(deficit_countries.items(), key=lambda item: item[1])}
    #order the countries from greatest to least surplus's
    surplus_countries = {k: v for k, v in sorted(surplus_countries.items(), key=lambda item: item[1], reverse=True)}
    print("Total vaccines in the system: %d", test_total_vaccines())
    total_surplus = 0
    #Find total amount of surplus
    for country in surplus_countries:
        total_surplus += surplus_countries[country]
        #Take away the surplus vaccines from the countries to stock pile
        country.num_vaccines -= country.surplus()


    """
    #TEST PRINT OUT DATA
    print("Surplus countries before distribution")
    for country in surplus_countries:
        print(country.name + " " + str(surplus_countries[country]))
    print("Deficit countries before distribution")
    for country in deficit_countries:
        print(country.name + ": " + str(deficit_countries[country]))
    """
    
    print("Vaccine rates before distribution: ")
    for country in c.country_master_list:
        print(country.name + ": " + str(country.vaccination_rate())) 


    #Find the average distribution amount to each deficit country
    while(len(deficit_countries) > 0 and total_surplus > 0):
        average_distribution = math.floor(float(total_surplus/len(deficit_countries)))
        print("Average distribution: %d, Amount of donatees: %d, Total surplus: %d" % (average_distribution, len(deficit_countries), total_surplus))
        donated_counter = 0
        for country in deficit_countries:
            donated_counter += 1
            if average_distribution >= -1 * country.surplus():
                country.num_vaccines += -1 * deficit_countries[country]
                deficit_countries[country] = 0
                total_surplus -= -1 * deficit_countries[country]
            else:
                deficit_countries[country] += average_distribution
                country.num_vaccines += average_distribution
                total_surplus -= average_distribution
        #Remove non deficit countries from deficit countries
        for i in deficit_countries.copy():
            if deficit_countries[i] == 0:
                deficit_countries.pop(i)
    """
    #Assume that every surplus country donated their surplus, set the values accordingly
    for country in surplus_countries:
        country.num_vaccines -= country.surplus()
    """
    
    #Equally give back the number of vaccines that may be left over in the surplus
    #To the countries that donated
    if total_surplus > 0:
        average_distribution = math.floor(float(total_surplus/len(surplus_countries)))
        for country in surplus_countries:
            country.num_vaccines += average_distribution
    
    print("Vaccine rates after distribution: ")
    for country in c.country_master_list:
        print(country.name + ": " + str(country.vaccination_rate())) 

    print("Total vaccines in the system: %d", test_total_vaccines())
    """
    print("Surplus countries after distribution")
    for country in surplus_countries:
        print(country.name + " " + str(country.num_vaccines))
    print("Deficit countries after distribution")
    for country in deficit_countries:
        print(country.name + ": " + str(deficit_countries[country]))
    """
    #STAGE 2: find the amount of vaccines needed to purchase
    # To properly balance the graph
    if len(deficit_countries) > 0:
        #Find total deficit:
        return -1 * sum(deficit_countries.values())
    else:
        return 0


if __name__ == "__main__":
    #pp.master_list_to_csv(country_to_quantity=country_to_quantity)
    balance()

# https://ourworldindata.org/covid-vaccinations
