import pytest
from homework16.homework16 import TrainCar
from homework16.homework16 import Train
from homework16.homework16 import Passenger

class Test_Passenger:
    @pytest.mark.smoke
    def test_passenger_name(self):
        self.name = 'Oksana'
        assert self.name == 'Oksana'

    @pytest.mark.smoke
    def test_passenger_destination(self):
        self.destination = "Station A"
        assert self.destination == "Station A"

    @pytest.mark.smoke
    def test_passenger_destination_false(self):
        self.destination = "Station A"
        assert self.destination == "Station C"


class Test_Traine:
    @pytest.mark.smoke
    def test_traine_locomotive(self):
        self.locomotive = "Locomotive"
        assert self.locomotive == "Locomotive"

    @pytest.mark.smoke
    def test_cars(self):
        self.cars = [2]
        assert self.cars == [2]

   # def test_add_car(self, train_car):
    #    self.cars.append(train_car) = TrainCar("Passenger", 2)


class Test_TrainCar:
    def __init__(self):
        self.passengers = []

    @pytest.mark.smoke
    def test_cartyoe(self):
        self.car_type = "Passenger"
        assert self.car_type == "Passenger"

    @pytest.mark.smoke
    def test_capacity(self):
        self.capacity = 2
        assert self.capacity == 2


