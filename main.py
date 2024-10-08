import calculator, os


def print_directory_contents(directory):
    for file in os.listdir(directory):
        print(file)

if __name__ == '__main__':
    calc = calculator.Calculator()
    calc.add_car(
        calculator.Car("Toyota Corolla", 30000, 6.1, 600, 1000),
    )
    calc.add_car(
        calculator.ElectricCar("Tesla Model 3", 60000, 1100, 17),
    )
    calc.add_car(
        calculator.Car("Range Rover", 80000, 10.1, 1000, 1500),
    )

    calc.print_cars()