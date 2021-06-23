from typing import *

import pandas as pd
import plotly.express as px

def scrape_and_display_covid_data() -> None:
    """The purpose of this function is to scrape data from a CSV file provided by various reputable sources such as the WHO
    and governments. It provides the user with a plot of the average number of doses received by each person in a given country
    as of June 22nd, 2021.

    Sources Referenced: https://www.kaggle.com/gpreda/covid-world-vaccination-progress
                        https://datahub.io/JohnSnowLabs/country-and-continent-codes-list/r/country-and-continent-codes-list-csv.csv
    """
    covid_CSV = 'country_vaccinations.csv'
    covid_data = pd.read_csv(covid_CSV, usecols=['iso_code', 'country', 'people_fully_vaccinated', 'people_vaccinated', 'population'])

    countries_URL = 'https://datahub.io/JohnSnowLabs/country-and-continent-codes-list/r/country-and-continent-codes-list-csv.csv'
    countries_data = pd.read_csv(countries_URL, usecols=['Three_Letter_Country_Code', 'Country_Name'])

    df = pd.merge(covid_data, countries_data, left_on='iso_code', right_on='Three_Letter_Country_Code')
    df = df.groupby(['Country_Name']).sum().reset_index()
    df['Total Vaccines Per Population'] = ((df.people_vaccinated - df.people_fully_vaccinated)*2 + df.people_vaccinated) / df.population
    df = df.rename({'total_vaccinations': 'Total Vaccinated', 'Country_Name': 'Country'}, axis='columns')
    px.line(df, x='Country', y='Total Vaccines Per Population').show()
    
scrape_and_display_covid_data()