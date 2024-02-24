from abc import ABC

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand