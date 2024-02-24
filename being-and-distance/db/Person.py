from db.Being import Being

class Person(Being):
    def __init__(self, name):
        super().__init__(name)
        self.total_distance_moved_by_person = 0

    def move(self, distance):
        self.total_distance_moved_by_person += distance
        Being.total_distance_moved += distance
