from db.Being import Being
from pydantic import BaseModel, validator

class Person(Being,BaseModel):
        name: str
        total_distance_moved_by_person:int = 0

    def move(self, distance: float | int) -> None:
        self.total_distance_moved_by_person += distance
        Being.total_distance_moved += distance

    @validator('name')
    def name_must_not_be_empty(cls, value):
       if not value:
             raise ValueError("Name cannot be empty")
        return value