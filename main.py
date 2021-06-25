"""
This function is the main function from which the program runs.

Copying for purposes other than personal use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Wasee Alam, Rohan Dey, Porom Kamal

"""

from typing import *
import country as c
import balance_distributions as bd
import print_plot as pp
import main_frame as display

if __name__ == "__main__":
    # Execute the function
    pp.create_countries(master_list=c.country_master_list,
                     df=pp.scrape_covid_data())

    country_to_quantity = {}  # Dictionary that sorts by country vs vaccine quantity
    for country in c.country_master_list:
        country_to_quantity[country] = country.num_vaccines

    c.country_master_list = list(dict.fromkeys(c.country_master_list))

    pp.master_list_to_csv(c.country_master_list, country_to_quantity)

    bd.new_bal()

    for country in c.country_master_list:
        country_to_quantity[country] = country.num_vaccines
        
    pp.master_list_balanced_to_csv(c.country_master_list, country_to_quantity)

    display.main()
