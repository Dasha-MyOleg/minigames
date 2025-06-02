
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import CalculatorState, handle_key_press, calculate, parse


def test_handle_key_press_extended():


    state = CalculatorState()

    # Додавання чисел
    handle_key_press(state, "1")
    handle_key_press(state, "0")
    assert state.screen == 10  # Перевірка після натискання двох цифр

    # Операція "+"
    handle_key_press(state, "+")
    assert state.first_number == 10
    assert state.op == "+"
    assert state.start_second_number is True

    # Введення другого числа
    handle_key_press(state, "2")
    assert state.screen == 2

    # Завершення операції
    handle_key_press(state, "=")
    assert state.screen == 12
