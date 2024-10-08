from apis import get_gas_price, get_power_price


class Calculator:
    def __init__(self, mileage=15000, years=10, year_lost=10):
        self.mileage = mileage
        self.cars = {}  # Car : Year Price
        self.years = years
        self.years_lost = year_lost / 100

    def add_car(self, car):
        year_cost = car.year_cost(self.mileage)
        price_per_year = car.price / self.years
        left_price = self.get_left_price(car) / self.years
        self.cars[car] = year_cost + price_per_year - left_price

    def get_left_price(self, car):
        left_price = car.price
        for i in range(self.years):
            left_price -= left_price * self.years_lost
        return left_price

    def print_cars(self):
        for car, year_price in self.cars.items():
            print(f"{car.name}:\t\t{year_price}")


class Car:
    def __init__(self, name: str, price: float, fuel_economy: float, service_costs: int, insurance_cost: int):
        self.name = name
        self.price = price
        self.fuel_economy = fuel_economy
        self.service_costs = service_costs
        self.insurance_cost = insurance_cost

    def static_year_cost(self) -> float:
        return self.service_costs + self.insurance_cost

    def dynamic_year_cost(self, mileage: int) -> float:
        return self.fuel_economy * mileage / 100 + get_gas_price()

    def year_cost(self, mileage: int):
        return self.static_year_cost() + self.dynamic_year_cost(mileage)


class ElectricCar(Car):
    def __init__(self, name: str, price: int, insurance_cost: int, power_consumption: int):
        super().__init__(name=name, price=price, fuel_economy=0, service_costs=0, insurance_cost=insurance_cost)
        self.power_consumption = power_consumption # Wt / 1 km

    def dynamic_year_cost(self, mileage: int):
        return self.power_consumption * mileage / 1000 + get_power_price()


    class Motorcycle(Car):
        pass