from db.Person import Person


class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def drive(self, distance:int | float ):
        print(f"{self.name} is driving the {self.vehicle.brand} {self.vehicle.model}.")
        self.move(distance)