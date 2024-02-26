
from pydantic import BaseModel, validator


class Being(BaseModel):
    name: str
    total_distance_moved: float | int = 0

    def move(self, distance: float | int) -> None:
        Being.total_distance_moved += int(distance)

    @validator('name')
    def name_must_not_be_empty(cls, value):
        if not value:
            raise ValueError("Name cannot be empty")
        return value


# class BeingMeta(BaseModel):
#     total_distance_moved: int = 0


# class Being(BeingMeta, BaseModel):
#     name: str

#     def move(self, distance: int) -> None:
#         BeingMeta.total_distance_moved += distance

#     @validator('name')
#     def name_must_not_be_empty(cls, value):
#         if not value:
#             raise ValueError("Name cannot be empty")
#         return value
