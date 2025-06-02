from src.communication.game_runner import GameRunner
from src.io.file_io import read_input, print_output
import sys

if __name__ == "__main__":
    file_path = "../input.txt"

    # Значення за замовчуванням
    show_steps = True

    # Перевіряємо, чи є параметр "show_steps" у командному рядку
    if "show_steps" in sys.argv:
        show_steps = True

    # Ініціалізація IOHandler
    io_handler = type(
        "IOHandler",
        (object,),
        {"read_input": read_input, "print_output": print_output}
    )

    # Ініціалізація GameRunner
    game = GameRunner(io_handler)

    # Передача параметра show_steps у GameRunner
    game.run(file_path, show_steps=show_steps)
