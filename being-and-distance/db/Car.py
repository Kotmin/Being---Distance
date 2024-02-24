from db.Vehicle import Vehicle
from pydantic import BaseModel


class Car(Vehicle,BaseModel):
    brand: str
    model:str
    additional_info: str = None

    def get_description(self) -> str:
        return f"{self.brand} {self.model}"
    
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True