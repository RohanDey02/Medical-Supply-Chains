from typing import *

import pandas as pd
import country as c
import balanceDistributions as bd
from pandas.core.frame import DataFrame
import plotly.express as px
import csv

# Constants
COUNTRY_NAME: int = 0
POPULATION: int = 15
GDPPERCAPITA: int = 18


def scrape_covid_data() -> DataFrame:
    """The purpose of this function is to scrape data from a CSV file provided by various reputable sources such as the WHO
    and governments. It provides the user with a plot of the average number of doses received by each person in a given country
    as of June 22nd, 2021.

    Sources Referenced: https://www.kaggle.com/gpreda/covid-world-vaccination-progress
                        https://datahub.io/JohnSnowLabs/country-and-continent-codes-list/r/country-and-continent-codes-list-csv.csv
    """
    covid_CSV = 'input_csvs/country_vaccinations.csv'
    covid_data = pd.read_csv(covid_CSV, usecols=[
                             'iso_code', 'country', 'total_vaccinations', 'people_fully_vaccinated', 'population', 'gdpPerCapita'])

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


def create_countries(master_list: List[c.Country], df: DataFrame) -> List[c.Country]:
    i = 0
    with open('input_csvs/country_vaccinations.csv', 'r') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for row in reader:
            new_country = c.Country(row[COUNTRY_NAME], float(row[GDPPERCAPITA]), 100, int(row[POPULATION]), df.at[i,
                                    'total_vaccinations'] - df.at[i, 'people_fully_vaccinated'], df.at[i, 'people_fully_vaccinated'])
            master_list.append(new_country)
            i += 1
    return master_list


def master_list_to_csv(master_list: List[c.Country], country_to_quantity: dict) -> None:
    """This function takes in the country dictionary and writes it out as a CSV"""
    with open('output_csvs/vaccines.csv', 'w', newline="") as f:
        filewriter = csv.writer(f, delimiter=',')
        filewriter.writerow(['country', '2dose',
                            '1dose', 'vaccine_per_population', 'gdpPerCapita'])
        for country in country_to_quantity:

            country_obj = c.find_country(master_list, country.name)
            vaccine_per_pop = ((country_to_quantity[country_obj] - country_obj.vaccinated_pop_2dose) +
                               country_obj.vaccinated_pop_2dose*2) / country_obj.num_pop

            filewriter.writerow([country.name, country.vaccinated_pop_2dose,
                                country.vaccinated_pop_1dose, vaccine_per_pop, country.gdp])


# def master_list_to_csv2(master_list: List[c.Country], country_to_quantity: dict) -> None:
#     """This function takes in the country dictionary and writes it out as a CSV"""
#     with open('output_csvs/vaccines_balanced.csv', 'w', newline="") as f:
#         filewriter = csv.writer(f, delimiter=',')
#         filewriter.writerow(['country', 'total_vaccinations',
#                             'people_fully_vaccinated', 'population', 'gdpPerCapita'])
#         for country in country_to_quantity:

#             country_obj = c.find_country(master_list, country.name)
#             vaccine_per_pop = ((country_to_quantity[country_obj] - country_obj.vaccinated_pop_2dose) +
#                                country_obj.vaccinated_pop_2dose*2) / country_obj.num_pop

#             filewriter.writerow([country.name, country.vaccinated_pop_2dose,
#                                 country.vaccinated_pop_1dose, vaccine_per_pop, country.gdp])


# def vaccines_to_gui() -> DataFrame:
#     """This function will read vaccines.csv and output a graph similar to scrape and display"""
#     covid_CSV = 'output_csvs/vaccines.csv'
#     covid_data = pd.read_csv(covid_CSV, usecols=[
#                              'country', 'total_vaccinations', 'people_fully_vaccinated',
#                              'vaccine_per_population', 'gdpPerCapita'])

#     df = covid_data
#     df['Average Doses'] = ((df.total_vaccinations - df.people_fully_vaccinated) +
#                            df.people_fully_vaccinated*2) / df.vaccine_per_population
#     df = df.rename({'country': 'smd'}, axis='columns')
#     px.line(df, x='smd', y='Average Doses').show()
#     return df


if __name__ == "__main__":
    # Test Run
    create_countries(master_list=c.country_master_list,
                     df=scrape_covid_data())

    country_to_quantity = {}  # Dictionary that sorts by country vs vaccine quantity
    for country in c.country_master_list:
        country_to_quantity[country] = (country.vaccinated_pop_2dose*2) + (country.num_vaccines) + \
            country.vaccinated_pop_1dose
        print(country.name, (country.vaccinated_pop_2dose*2) + (country.num_vaccines) +
              country.vaccinated_pop_1dose)

    master_list_to_csv(c.country_master_list, country_to_quantity)

    # bd.balance()
    # master_list_to_csv2(c.country_master_list, country_to_quantity)

    # vaccines_to_gui()
