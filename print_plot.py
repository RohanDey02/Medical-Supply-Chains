"""This function scrapes COVID data, and writes COVID data it also creates the masterlist
of countries used throughout the program."""
import random
from typing import *

import pandas as pd
import country as c
from pandas.core.frame import DataFrame
import plotly.express as px
import csv
import balance_distributions as bd

# Constants
COUNTRY_NAME: int = 0
TOTAL_VACCINATIONS: int = 3
PEOPLE_FULLY_VACCINATED: int = 5
POPULATION: int = 15
GDPPERCAPITA: int = 18


def scrape_covid_data() -> DataFrame:
    """The purpose of this function is to scrape data from a CSV file provided by various 
    reputable sources such as the WHO and governments. It provides the user with a plot of 
    the average number of doses received by each person in a given country
    as of June 22nd, 2021.

    Sources Referenced: https://www.kaggle.com/gpreda/covid-world-vaccination-progress
                        https://datahub.io/JohnSnowLabs/country-and-continent-codes-list/r/country-and-continent-codes-list-csv.csv
    """
    covid_CSV = 'input_csvs/country_vaccinations.csv'
    covid_data = pd.read_csv(covid_CSV, usecols=[
                             'iso_code', 'country', 'total_vaccinations',
                             'people_fully_vaccinated', 'population', 'gdpPerCapita'])

    countries_URL = 'https://datahub.io/JohnSnowLabs/country-and-continent-codes-list/r/country-and-continent-codes-list-csv.csv'
    countries_data = pd.read_csv(countries_URL, usecols=[
                                 'Three_Letter_Country_Code', 'Country_Name'])

    df = pd.merge(covid_data, countries_data, left_on='iso_code',
                  right_on='Three_Letter_Country_Code')

    df['Average Doses'] = ((df.total_vaccinations - df.people_fully_vaccinated) +
                           df.people_fully_vaccinated*2) / df.population

    df = df.rename({'Country_Name': 'Country'}, axis='columns')
    return df


def display_covid_data(df: DataFrame) -> None:
    px.line(df, x='Country', y='Average Doses').show()


def provide_average_doses(df: DataFrame) -> int:
    return (df['Average Doses'].mean() * 1.153110048)


def master_list_to_csv(master_list: List[c.Country], country_to_quantity: dict) -> None:
    """This function takes in the country dictionary and writes it out as a CSV"""
    with open('output_csvs/vaccines.csv', 'w', newline='') as f:
        filewriter = csv.writer(f, delimiter=',')
        filewriter.writerow(['country', 'num_vaccines', '2dose',
                            '1dose', 'vaccine_per_population', 'gdpPerCapita'])
        for country in country_to_quantity:
            country_obj = c.find_country(master_list, country.name)
            #
            vaccine_per_pop = ((country_to_quantity[country_obj] +
                                country_obj.vaccinated_pop_2dose*2 + country_obj.vaccinated_pop_1dose)) \
                / country_obj.num_pop
            # write each row
            filewriter.writerow([country.name, country.num_vaccines, country.vaccinated_pop_2dose,
                                country.vaccinated_pop_1dose, vaccine_per_pop, country.gdp])


def master_list_balanced_to_csv(master_list: List[c.Country], country_to_quantity: dict) -> None:
    """This function takes in the country dictionary and writes it out as a CSV"""
    with open('output_csvs/vaccines_balanced.csv', 'w', newline='') as f:
        filewriter = csv.writer(f, delimiter=',')
        filewriter.writerow(['country', 'num_vaccines', '2dose',
                             '1dose', 'vaccine_per_population', 'gdpPerCapita'])
        for country in country_to_quantity:
            # create the country object so country functions can be accessed
            country_obj = c.find_country(master_list, country.name)
            # calculate the numebr of vaccines per person
            vaccine_per_pop = ((country_to_quantity[country_obj] +
                                country_obj.vaccinated_pop_2dose*2 + country_obj.vaccinated_pop_1dose)) / country_obj.num_pop

            filewriter.writerow([country.name, country.num_vaccines, country.vaccinated_pop_2dose,
                                 country.vaccinated_pop_1dose, vaccine_per_pop, country.gdp])


def create_countries(master_list: List[c.Country], df: DataFrame) -> List[c.Country]:
    i = 0
    with open('input_csvs/country_vaccinations.csv', 'r') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for row in reader:
            new_country = c.Country(name=str(row[COUNTRY_NAME]), gdp=float(row[GDPPERCAPITA]), num_vaccines=0,
                                    num_pop=int(row[POPULATION]), vaccinated_pop_1dose=int(row[TOTAL_VACCINATIONS]) -
                                    int(row[PEOPLE_FULLY_VACCINATED]), vaccinated_pop_2dose=int(row[PEOPLE_FULLY_VACCINATED]))
            new_country.num_vaccines = bd.scaled_vaccine_nums(row[COUNTRY_NAME])

            master_list.append(new_country)
            i += 1

    return master_list
