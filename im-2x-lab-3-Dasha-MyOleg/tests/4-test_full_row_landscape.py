import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from communication.game_runner import GameRunner
from logic.field import Field


class TestField:
    """Тести для логіки падіння фігур."""

    def setup_method(self):
        """Ініціалізація спільних параметрів для всіх тестів."""
        self.dimensions = (5, 6)

    def test_full_row_landscape(self):
        """Тест перевіряє, що фігура падає на повний ряд ландшафту."""
        grid = [
            ['.', '.', 'p', '.', '.', '.'],
            ['.', '.', '.', '.', 'p', '.'],
            ['.', 'p', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '#', '#'],
            ['.', '.', '.', '.', '.', '.'],
        ]
        field = Field(self.dimensions, grid)
        field.drop_figure()
        assert field.render() == [
            "......",
            "......",
            ".##.#.",
            "######",
            "......",
        ]
