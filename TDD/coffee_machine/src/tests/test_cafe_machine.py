# tests/test_cafe_machine.py
import pytest
from src.cafe_machine import CoffeeMachine

def test_select_cup_size():
    coffee_machine = CoffeeMachine()
    assert coffee_machine.select_cup_size("small") == 3
    assert coffee_machine.select_cup_size("medium") == 5
    assert coffee_machine.select_cup_size("large") == 7

def test_select_sugar_spoons():
    coffee_machine = CoffeeMachine()
    assert coffee_machine.select_sugar_spoons(2) == 2

def test_dispense_coffee():
    coffee_machine = CoffeeMachine()
    coffee_machine.select_cup_size("medium")
    coffee_machine.select_sugar_spoons(1)
    assert coffee_machine.dispense_coffee() == "Coffee dispensed!"

def test_dispense_coffee_no_cups():
    coffee_machine = CoffeeMachine()
    with pytest.raises(ValueError, match="No cups available."):
        coffee_machine.dispense_coffee()
