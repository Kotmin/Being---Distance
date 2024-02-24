from db.Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand:str, model:str):
        super().__init__(brand)
        self.model = model