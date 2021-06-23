import country as c
from country import Country


def find_negative_country() -> Country:
    for country in c.country_master_list.reverse:
        if country.surplus < 0:
            return country


def balance():
    """
    country_to_quantity = {}
    for country in c.country_master_list:
        country_to_quantity[country.name] = country.surplus()

    sorted(country_to_quantity.values())

    for country in country_to_quantity:
        while country.surplus > 0:
            donatee = find_negative_country
            c.country.donate(donatee.name, 1)
    """

    # Redistribution algorithm: Porom Rendition
    deficit_countries = {}
    surplus_countries = {}

    # Find the countries that are in a deficit of vaccines and surpluses
    for country in c.country_master_list:
        if country.surplus() < 0:
            deficit_countries[country] = country.surplus()
        else:
            surplus_countries[country] = country.surplus()
    
    #order the countries from greatest to least deficits
    deficit_countries = {k: v for k, v in sorted(deficit_countries.items(), key=lambda item: item[1])}
    #order the countries from greatest to least surplus's
    surplus_countries = {k: v for k, v in sorted(surplus_countries.items(), key=lambda item: item[1], reverse=True)}

    # Donate to countries in deficit in priority order from greatest deficit to least
    # Donatees donate based on highest surplus to least
    print("Deficit countries before balancing: ")
    for country in deficit_countries:
        print(country.name + ": " + str(deficit_countries[country]))
    print("Surplus countries before balancing: ")
    for country in surplus_countries:
        print(country.name + ": " + str(surplus_countries[country]))
    
    
    for demand in deficit_countries:
        for supply in surplus_countries:
            if -1 * deficit_countries[demand] <= surplus_countries[supply] and deficit_countries[demand] != 0:
                print("entered for:"+ demand.name + "," + supply.name)
                #Execute donation
                supply.donate(demand, deficit_countries[demand])
                #update dictionaries
                surplus_countries[supply] += deficit_countries[demand]
                deficit_countries[demand] = 0
            elif deficit_countries[demand] > surplus_countries[supply]:
                #print("entered 2nd for:"+ demand.name + "," + supply.name)
                #donate entire supply
                supply.donate(demand, surplus_countries[supply])
                #update dictionaries
                deficit_countries[demand] += surplus_countries[supply]
                surplus_countries[supply] = 0
    print("Deficit countries after balancing: ")
    for country in deficit_countries:
        print(country.name + ": " + str(deficit_countries[country]))
    print("Surplus countries after balancing: ")
    for country in surplus_countries:
        print(country.name + ": " + str(surplus_countries[country]))
                
                

if __name__ == "__main__":
    balance()


# https://ourworldindata.org/covid-vaccinations
