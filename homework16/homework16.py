class TrainCar:
    car_count = 0

    def __init__(self, car_type, capacity):
        self.car_type = car_type
        self.capacity = capacity
        self.passengers = []

        TrainCar.car_count += 1
        self.car_number = TrainCar.car_count

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
        else:
            print(f"TrainCar {self.car_number} is already full.")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        res = f'"traincar": "{self.car_number}"\n'
        for i, passenger in enumerate(self.passengers, start=1):
            res += f'"passanger_name": "{passenger.name}", "destination": "{passenger.destination}", "place": {i}\n'
        return res


class Train:
    def __init__(self, locomotive):
        self.locomotive = locomotive
        self.cars = []

    def add_car(self, train_car):
        self.cars.append(train_car)

    def __len__(self):
        return len(self.cars)

    def __str__(self):
        res = ""
        for car in self.cars:
            res += str(car)
        return res


class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination


# Example Usage
passenger1 = Passenger("Oksana", "Station A")
passenger2 = Passenger("Ivan", "Station B")

train = Train("Locomotive")
train.add_car(TrainCar("Passenger", 2))
train.cars[0].add_passenger(passenger1)
train.cars[0].add_passenger(passenger2)

print(train)  # Print the train information as described