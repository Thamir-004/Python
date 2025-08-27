class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = speed  # Encapsulation: protected attribute

    def accelerate(self, amount):
        self._speed += amount
        print(f"{self.brand} {self.model} accelerates to {self._speed} km/h.")

    def brake(self, amount):
        self._speed = max(0, self._speed - amount)
        print(f"{self.brand} {self.model} slows down to {self._speed} km/h.")

    def display_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year}), Speed: {self._speed} km/h")


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity, speed=0):
        super().__init__(brand, model, year, speed)
        self.battery_capacity = battery_capacity  # Unique attribute for electric cars

    def charge(self):
        print(f"{self.brand} {self.model} is charging... Battery at 100%!")

    # Polymorphism: Overrides accelerate() to behave differently
    def accelerate(self, amount):
        self._speed += amount
        print(f"{self.brand} {self.model} (Electric) silently speeds up to {self._speed} km/h.")


# ---- Test the Classes ----
if __name__ == "__main__":
    # Create regular car
    car1 = Car("Toyota", "Corolla", 2020)
    car1.display_info()
    car1.accelerate(30)
    car1.brake(10)

    print("\n---\n")

    # Create electric car
    tesla = ElectricCar("Tesla", "Model S", 2023, 100)
    tesla.display_info()
    tesla.accelerate(50)
    tesla.charge()
