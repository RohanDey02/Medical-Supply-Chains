"""This function houses the country dataclass and its helpers."""

from typing import *

# Global Vars
country_master_list = []


class Country:
    """Implementation of the country dataclass"""
    name: str
    gdp: float
    num_vaccines: Optional[int]
    num_pop: int
    vaccinated_pop_1dose: int
    vaccinated_pop_2dose: int

    def __init__(self, name: str, gdp: float, num_vaccines: Optional[int], num_pop: int,
                 vaccinated_pop_1dose: int, vaccinated_pop_2dose: int) -> None:
        """Fields to initialize country"""
        self.name = name
        self.gdp = gdp
        self.num_vaccines = num_vaccines  # Vaccines
        self.num_pop = num_pop  # Number of people
        self.vaccinated_pop_1dose = vaccinated_pop_1dose
        self.vaccinated_pop_2dose = vaccinated_pop_2dose
        country_master_list.append(self)

    def surplus(self) -> int:
        """This function return the surplus/deficit of vaccines"""
        return (self.num_vaccines - (self.num_pop - self.vaccinated_pop_1dose -
                                     self.vaccinated_pop_2dose*2))

    def donate(self, num_donation: int) -> None:
        """This function modifies the amount of vaccines a country has.
        One country can "donate" their vaccines to another country."""
        self.num_vaccines = self.num_vaccines - num_donation

    def receive_donation(self, num_donation: int) -> None:
        self.num_vaccines += num_donation

    def vaccination_rate(self) -> float:
        """ The vaccination rate is defined as:
            The amount of vaccines available/amount of vaccines needed
            Idealy this number should be 1 or greater, less than one means a shortage of vaccines"""
        return round(float(self.num_vaccines/((self.num_pop - self.vaccinated_pop_2dose -
                                               self.vaccinated_pop_1dose) * 2 + self.vaccinated_pop_1dose)), 2)

    def print_country(self):
        return "Name: " + str(self.name) + ",Vaccines: " + str(self.num_vaccines) + ",Population: " \
            + str(self.num_pop) + ",1 Dose: " + str(self.vaccinated_pop_1dose) + \
            ",2 Dose: " + str(self.vaccinated_pop_2dose)


def find_country(country_master_list: List[Country], name: str) -> Country:
    """This function finds and returns the country dataclass when given the country name"""
    for country in country_master_list:
        if country.name == name:
            return country


def test_total_vaccines():
    total = 0
    for country in country_master_list:
        total += country.num_vaccines
    return total
