from abc import ABC, abstractmethod

class Being(ABC):
    total_distance_moved:int = 0

    def __init__(self, name:str) -> None:
        self.name = name

    @abstractmethod
    def move(self, distance: float | int ) -> None:
        pass


