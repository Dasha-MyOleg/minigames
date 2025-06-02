# src/tetris.py
from src.communication.game_runner import GameRunner
from src.io.file_io import read_input, print_output

if __name__ == "__main__":
    file_path = "../input.txt"  # Вкажіть шлях до файлу
    io_handler = type("IOHandler", (), {"read_input": read_input, "print_output": print_output})
    game = GameRunner(io_handler)
    game.run(file_path)
