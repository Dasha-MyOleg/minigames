# src/communication/game_runner.py
from logic.field import Field
from src.io.file_io import read_input, print_output

class GameRunner:
    def __init__(self, io_handler):
        self.io_handler = io_handler

    def run(self, file_path):
        dimensions, grid = self.io_handler.read_input(file_path)
        field = Field(dimensions, grid)
        field.drop_figure()
        output = field.render()
        self.io_handler.print_output(output)
