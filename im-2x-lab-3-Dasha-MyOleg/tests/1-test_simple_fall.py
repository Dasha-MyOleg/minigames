import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from communication.game_runner import GameRunner
from logic.field import Field


class TestField:
    """Тести для логіки падіння фігури."""

    def setup_method(self):
        """Метод для ініціалізації спільних даних перед кожним тестом."""
        self.dimensions = (5, 6)
        self.grid = [
            ['.', '.', 'p', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]

    def test_simple_fall(self):
        """Тест перевіряє, що фігура падає вниз правильно."""
        field = Field(self.dimensions, self.grid)
        field.drop_figure()
        assert field.render() == [
            "......",
            "......",
            "......",
            "......",
            "..#...",
        ]

