import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import CalculatorState, handle_key_press, calculate, parse

def test_calculate():
    assert calculate(["1", "2", "+", "3", "="]) == "1 2 + 3 = 15"
    assert calculate(["5", "0", "-", "2", "5", "="]) == "5 0 - 2 5 = 25"
    assert calculate(["1", "0", "*", "4", "="]) == "1 0 * 4 = 40"
    assert calculate(["8", "/", "2", "="]) == "8 / 2 = 4"
    assert calculate(["9", "/", "4", "="]) == "9 / 4 = 2"  # Цілочисельне ділення


def test_handle_key_press():
    state = CalculatorState()
    handle_key_press(state, "1")
    assert state.screen == 1

    handle_key_press(state, "2")
    assert state.screen == 12

    handle_key_press(state, "+")
    assert state.first_number == 12
    assert state.op == "+"
    assert state.start_second_number is True

    handle_key_press(state, "3")
    assert state.screen == 3
    assert state.start_second_number is False

    handle_key_press(state, "=")
    assert state.screen == 15


