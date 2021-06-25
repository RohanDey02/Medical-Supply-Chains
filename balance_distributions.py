"""This file houses the balance function and helper functions that
comes with it. """

import country as c
import random
from country import Country
from operator import attrgetter


def find_negative_country(curr_country: Country) -> Country:
    temp_list = c.country_master_list
    temp_list.reverse
    for country in temp_list:
        if country.surplus() < 0:
            return country


def find_poor_country(curr_country: Country) -> Country:
    temp_master_list = c.country_master_list
    temp_master_list.sort(key=attrgetter("gdp"))
    for country in temp_master_list:
        if country.surplus() < 2:
            return country


def test_total_vaccines():
    total = 0
    for country in c.country_master_list:
        total += country.num_vaccines
    return total


def new_bal() -> None:
    for country in c.country_master_list:
        value = country.surplus()
        if value > 0:
            if find_negative_country(country) is None:
                break
            else:
                for country2 in c.country_master_list:
                    if country2.surplus() < 0:
                        country.donate(country.surplus())
                        country2.receive_donation(country.surplus())


def scaled_vaccine_nums(country: str) -> int:
    """This function will return an approprite integer which represents the 
    number of vaccines a country has"""

    country2 = c.find_country(c.country_master_list, country)
    return random.randint(int(country2.num_pop-country2.num_pop*0.25), int(country2.num_pop+country2.num_pop*0.10))

