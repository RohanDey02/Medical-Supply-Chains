"""This file houses the GUI functions and its helpers."""

from tkinter import *

import pandas as pd
import plotly_express as px
import print_plot as pp


def button1_switch() -> None:
    print("Printing Data Before Balance")
    pp.display_covid_data(pp.scrape_covid_data())


def button2_switch() -> None:
    """This function will read vaccines.csv and output a graph similar to scrape and display"""
    print("Printing Data After Balance")

    covid_CSV = 'output_csvs/vaccines_balanced.csv'
    covid_data = pd.read_csv(covid_CSV, usecols=[
                             'country', 'vaccine_per_population'])

    df = covid_data
    df['Average Doses'] = df.vaccine_per_population
    df = df.rename({'country': 'Country'}, axis='columns')
    px.line(df, x='Country', y='Average Doses').show()
    return df


# The main function
def main() -> None:
    window = Tk()
    window.title("Medical Supply Chains")
    window.geometry("500x300")
    window.configure(bg="powder blue")

    labelTitle = Label(text="Manage Medical Supply Chains")
    labelTitle.grid(row=0, column=0)
    labelTitle.configure(bg="powder blue", font="helvetica 15")

    # Submit Button That Inserts Into Excel Document
    button1 = Button(window, text="Plot Data",
                     command=button1_switch, height=9, width=75)
    button1.grid(row=1, column=0)
    button1.configure(bg="light green")

    button2 = Button(window, text="Balance and Plot Data",
                     command=button2_switch, height=9, width=75)
    button2.grid(row=2, column=0)
    button2.configure(bg="light green")

    # Create an event loop
    window.mainloop()
