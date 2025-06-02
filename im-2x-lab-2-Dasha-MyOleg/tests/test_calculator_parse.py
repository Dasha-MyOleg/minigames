import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import CalculatorState, handle_key_press, calculate, parse


def test_parse_edge_cases():

    
    # Простий випадок
    assert parse("1 2 + 3 =") == ["1", "2", "+", "3", "="]

    # Випадок з додатковими пробілами
    assert parse("  9 /  4  = ") == ["9", "/", "4", "="]

    # Порожній рядок
    try:
        parse("")
    except ValueError as e:
        assert str(e) == "Вхідний рядок не може бути порожнім."

    # Некоректний ввід
    try:
        parse("abc")
    except ValueError as e:
        assert str(e) == "Вхідний рядок не може бути порожнім."
