from db.Person import Person

from db.Vehicle import Vehicle


class Driver(Person):
    vehicle: Vehicle

    def drive(self, distance: int | float):
        print(f"{self.name} is driving the {self.vehicle.brand} {self.vehicle.model}.\
              \n{self.vehicle.get_description()}")
        self.move(distance)
