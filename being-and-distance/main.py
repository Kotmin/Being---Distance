from db.Driver import Driver
from db.Car import Car
from db.Being import Being


def main() -> None:
    Being.total_distance_moved = 0

    car = Car(brand='Toyota', model="Yaris")
    driver1 = Driver(name='Kasia', vehicle=car)
    driver2 = Driver(name='Tomek', vehicle=car)

    driver1.drive(distance=10)
    driver2.drive(distance=15.5)

    print(
        f"Total distance moved by all persons: {driver1.total_distance_moved}")
    print(
        f"Total distance moved by {driver1.name}: {driver1.total_distance_moved_by_person}")
    print(
        f"Total distance moved by {driver2.name}: {driver2.total_distance_moved_by_person}")


if __name__ == "__main__":
    main()
