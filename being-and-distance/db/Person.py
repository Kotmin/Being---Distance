from db.Being import Being


class Person(Being):
    total_distance_moved_by_person: int = 0

    def move(self, distance: float | int) -> None:
        self.total_distance_moved_by_person += distance
        super().move(distance)
