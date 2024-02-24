from db.Driver import Driver
from db.Car import Car



def main() -> None:
    car = Car(brand='Toyota',model="Yaris")
    driver1 = Driver('Kasia',car)
    driver2 = Driver('Tomek',car)

    driver1.drive(10)
    driver2.drive(15.5)

    print(f"Total distance moved by all persons: {driver1.total_distance_moved}")
    print(f"Total distance moved by {driver1.name}: {driver1.total_distance_moved_by_person}")
    print(f"Total distance moved by {driver2.name}: {driver2.total_distance_moved_by_person}")


     

if __name__ == "__main__":
    main()
