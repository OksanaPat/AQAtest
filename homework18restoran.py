from abc import ABC, abstractmethod

class Dish(ABC):
    @abstractmethod
    def get_dish_name(self):
        pass

class Risotto(Dish):
    def get_dish_name(self):
        return "Risotto"

class Pasta(Dish):
    def get_dish_name(self):
        return "Pasta"

class Pizza(Dish):
    def get_dish_name(self):
        return "Pizza"

class OrderPart:
    def get_specific_dish(self, dish_type):
        if dish_type == "Risotto":
            return Risotto().get_dish_name()
        elif dish_type == "Pasta":
            return Pasta().get_dish_name()
        elif dish_type == "Pizza":
            return Pizza().get_dish_name()
        else:
            return "Dish not found"

# Example usage:
order_part = OrderPart()
print(order_part.get_specific_dish("Risotto"))  # Output: Risotto
print(order_part.get_specific_dish("Pasta"))  # Output: Pasta
print(order_part.get_specific_dish("Pizza"))  # Output: Pizza
print(order_part.get_specific_dish("Burger"))  # Output: Dish not found