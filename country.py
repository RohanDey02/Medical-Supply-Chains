from typing import *

# Global Vars
country_master_list = []


class Country:
    """Implementation of the country dataclass"""
    name: str
    gdp: float
    num_vaccines: int
    num_pop: int
    curr_stock: int
    vaccinated_pop_1dose: int
    vaccinated_pop_2dose: int

    def __init__(self, name: str, gdp: float, num_vaccines: int, num_pop: int,
                 vaccinated_pop_1dose: int, vaccinated_pop_2dose: int, curr_stock: int) -> None:
        """"""
        self.name = name
        self.gdp = gdp
        self.num_vaccines = num_vaccines  # Vaccines
        self.num_pop = num_pop  # Number of people
        self.curr_stock = curr_stock  # PPE
        self.vaccinated_pop_1dose = vaccinated_pop_1dose
        self.vaccinated_pop_2dose = vaccinated_pop_2dose
        country_master_list.append(self)

    def surplus(self) -> int:
        """This function return the surplus/deficit of vaccines"""
        return (self.num_vaccines - (self.num_pop - self.vaccinated_pop_1dose - self.vaccinated_pop_2dose) * 2 - self.vaccinated_pop_1dose)

    def donate(self, donatee: str, num_donation: int) -> None:
        """This function modifies the amount of vaccines a country has.
        One country can "donate" their vaccines to another country."""
        assert self.num_vaccines >= num_donation

        for country in country_master_list:
            if country.name == donatee:
                self.num_vaccines -= num_donation
                donatee.num_vaccines += num_donation
                print("Donation Successful.")
                break


if __name__ == '__main__':
    print("Test")
