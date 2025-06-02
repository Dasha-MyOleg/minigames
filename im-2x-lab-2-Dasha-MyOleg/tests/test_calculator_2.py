import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import CalculatorState, handle_key_press, calculate, parse

def test_calculate_edge_cases():
    # Простий випадок
    assert calculate(["1", "+", "2", "="]) == "1 + 2 = 3"

    # Ділення на нуль
    try:
        calculate(["5", "/", "0", "="])
    except ValueError as e:
        assert str(e) == "Ділення на нуль неможливе."

    # Довга послідовність
    assert calculate(["1", "2", "3", "+", "4", "5", "6", "="]) == "1 2 3 + 4 5 6 = 579"

    # Повторення операцій
    try:
        calculate(["1", "+", "+", "2", "="])
    except ValueError as e:
        assert str(e) == "Не можна натискати дві операції поспіль."

    # Натискання "=" без операції
    try:
        calculate(["1", "="])
    except ValueError as e:
        assert str(e) == "Операція не може бути виконана без двох операндів."



