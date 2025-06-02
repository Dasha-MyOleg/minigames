import unittest
from unittest.mock import MagicMock
from src.logic.field import Field
from src.io.file_io import print_output  # Імпорт функції для виведення стану гри

show_steps_tests = True


class TestField(unittest.TestCase):
    """Тести для логіки гри."""

    def setUp(self):
        """Метод, який виконується перед кожним тестом."""
        self.dimensions = (5, 6)
        self.mock_print_output = MagicMock()

    def tearDown(self):
        """Метод викликається після кожного тесту."""
        if self.mock_print_output.call_count > 0:
            print("Last field state:")
            for call_args in self.mock_print_output.call_args_list:
                print_output(call_args[0][0])

    def test_fall_independent_figures(self):
        """Тест перевіряє, що незалежні фігури падають правильно."""
        grid = [
            ['.', '.', 'p', '.', '.', '.'],
            ['p', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'p', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]

        # Перевірка з show_steps=False
        field = Field(self.dimensions, grid)
        field.drop_figure(show_steps=False)
        self.last_render = field.render()  # Збереження останнього стану гри

        # Оновлений очікуваний фінальний стан
        expected_output = [
            "......",
            "......",
            "......",
            "......",
            "#.#.#.",
        ]
        self.assertEqual(self.last_render, expected_output)

        # Перевірка з show_steps=True
        field = Field(self.dimensions, grid)
        field.render_steps = []  # Очищення списку станів
        field.drop_figure(show_steps=show_steps_tests)

        # Оновлені проміжні стани
        expected_steps = [
            [
                "......",
                "..p...",
                "p.....",
                "....p.",
                "......",
            ],
            [
                "......",
                "......",
                "..p...",
                "p.....",
                "....p.",
            ],
            [
                "......",
                "......",
                "......",
                "..p...",
                "p...#.",
            ],
            [
                "......",
                "......",
                "......",
                "......",
                "#.p.#.",
            ],
        ]

        self.assertEqual(field.render_steps[:-1], expected_steps)  # Виключаємо останній стан


if __name__ == "__main__":
    unittest.main()
