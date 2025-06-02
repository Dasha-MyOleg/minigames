import unittest
from unittest.mock import MagicMock
from src.logic.field import Field
from src.io.file_io import print_output  # Імпорт функції для виведення стану гри

show_steps_tests = True


class TestField(unittest.TestCase):
    """Тести для логіки падіння фігури."""

    def setUp(self):
        """Метод для ініціалізації спільних даних перед кожним тестом."""
        self.dimensions = (5, 6)
        self.grid = [
            ['.', '.', 'p', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]
        self.mock_print_output = MagicMock()

    def tearDown(self):
        """Метод викликається після кожного тесту."""
        if self.mock_print_output.call_count > 0:
            print("Final state:")
            for call_args in self.mock_print_output.call_args_list:
                print_output(call_args[0][0])

    def test_simple_fall(self):
        """Тест перевіряє, що фігура падає вниз правильно."""
        field = Field(self.dimensions, self.grid)

        # Перевірка з show_steps=True
        field.drop_figure(show_steps=show_steps_tests)
        expected_output = [
            "......",
            "......",
            "......",
            "......",
            "..#...",
        ]
        self.assertEqual(field.render(), expected_output)

        # Перевірка збереження станів у render_steps
        expected_steps = [
            [
                "......",
                "..p...",
                "......",
                "......",
                "......",
            ],
            [
                "......",
                "......",
                "..p...",
                "......",
                "......",
            ],
            [
                "......",
                "......",
                "......",
                "..p...",
                "......",
            ],
            [
                "......",
                "......",
                "......",
                "......",
                "..p...",
            ],
        ]
        self.assertEqual(field.render_steps[:-1], expected_steps)  # Виключаємо останній стан


if __name__ == "__main__":
    unittest.main()
