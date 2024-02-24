from abc import ABC,abstractclassmethod
from pydantic import BaseModel

class Vehicle(ABC,BaseModel):

    @abstractclassmethod
    def get_description(self) -> str:
        pass