from typing import *

import balanceDistributions
import country
from country import Country

Usa = Country(name="USA",
              gdp=123456.00,
              num_vaccines=3000000,
              num_pop=2000000,
              curr_stock=0,
              vaccinated_pop_1dose=1000000,
              vaccinated_pop_2dose=500000)

Canada = Country(name="Canada",
                 gdp=123456.00,
                 num_vaccines=600000,
                 num_pop=100000,
                 curr_stock=30000,
                 vaccinated_pop_1dose=10000,
                 vaccinated_pop_2dose=40000)

China = Country(name="China",
                gdp=123456.00,
                num_vaccines=500000,
                num_pop=1000000,
                curr_stock=20000,
                vaccinated_pop_1dose=100000,
                vaccinated_pop_2dose=200000)

Japan = Country(name="Japan",
                gdp=123456.00,
                num_vaccines=400000,
                num_pop=700000,
                curr_stock=20000,
                vaccinated_pop_1dose=200000,
                vaccinated_pop_2dose=300000)

Bangladesh = Country(name="Bangladesh",
                     gdp=123456.00,
                     num_vaccines=100000,
                     num_pop=1500000,
                     curr_stock=2,
                     vaccinated_pop_1dose=185000,
                     vaccinated_pop_2dose=235000)

India = Country(name="India",
                gdp=123456.00,
                num_vaccines=3000000,
                num_pop=1230000,
                curr_stock=0,
                vaccinated_pop_1dose=200000,
                vaccinated_pop_2dose=300000)

England = Country(name="England",
                  gdp=123456.00,
                  num_vaccines=500000,
                  num_pop=200000,
                  curr_stock=2000,
                  vaccinated_pop_1dose=10000,
                  vaccinated_pop_2dose=25000)

# Print out all the surplus/deficits:
balanceDistributions.balance()
