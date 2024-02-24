from db.Person import Person

from pydantic import BaseModel
from db.Vehicle import Vehicle


class Driver(Person,BaseModel):
    vehicle: Vehicle

    def drive(self, distance:int | float ):
        print(f"{self.name} is driving the {self.vehicle.brand} {self.vehicle.model}.\
              \n{self.vehicle.get_description()}")
        self.move(distance)


