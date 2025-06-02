import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from communication.game_runner import GameRunner
from logic.field import Field


class MockIOHandler:
    def __init__(self):
        self.input_data = None
        self.output_data = []

    def read_input(self, file_path):
        return (5, 6), [
            ['.', '.', 'p', '.', '.', 'p'],
            ['#', '.', '.', '.', 'p', '.'],
            ['p', '.', 'p', '.', '.', '.'],
            ['.', '.', '#', '.', '#', '.'],
            ['#', '.', '', 'p', '.', '.'],
        ]

    def print_output(self, grid):
        self.output_data = grid


def test_game_runner():
    mock_io = MockIOHandler()
    runner = GameRunner(mock_io)
    runner.run("mock_file_path")
    assert mock_io.output_data == [
        "......",
        "#.#...",
        "..#.#.",
        "#.#.#.",
        "#..#.#",
    ]

