# src/cafe_machine.py

class CoffeeMachine:
    def __init__(self):
        self.available_cups = {"small": 3, "medium": 5, "large": 7}
        self.available_sugar = 0

    def select_cup_size(self, size):
        if size not in self.available_cups:
            raise ValueError("Invalid cup size.")
        return self.available_cups[size]

    def select_sugar_spoons(self, spoons):
        self.available_sugar = spoons
        return spoons

    def dispense_coffee(self):
        if not self.available_cups:
            raise ValueError("No cups available.")
        if self.available_sugar < 0:
            raise ValueError("Invalid sugar spoons.")
        return "Coffee dispensed!"
