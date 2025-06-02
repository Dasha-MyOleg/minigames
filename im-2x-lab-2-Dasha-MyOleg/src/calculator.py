class CalculatorState:
    """
    Клас для відстеження стану калькулятора.
    """
    def __init__(self):
        self.screen = 0                   # Число, яке відображається на екрані
        self.first_number = None          # Перше введене число
        self.op = None                    # Операція ("+", "-", "*", "/")
        self.start_second_number = False  # Чи почалося введення другого числа


def handle_key_press(state: CalculatorState, key: str):
    """
    Обробляє натискання клавіш і змінює стан калькулятора.
    Відхиляє некоректні послідовності клавіш.

    Args:
        state (CalculatorState): Об'єкт стану калькулятора.
        key (str): Натиснута клавіша.
    """
    if key.isdigit():  # Якщо клавіша - цифра
        digit = int(key)
        if state.start_second_number:
            state.screen = digit  # Починаємо введення другого числа
            state.start_second_number = False
        else:
            state.screen = state.screen * 10 + digit  # Додаємо цифру до поточного числа
    elif key in ["+", "-", "*", "/"]:  # Якщо клавіша - операція
        if state.op is not None and state.start_second_number:
            raise ValueError("Не можна натискати дві операції поспіль.")
        state.first_number = state.screen
        state.op = key
        state.start_second_number = True
    elif key == "=":  # Якщо клавіша - "="
        if state.first_number is None or state.op is None:
            raise ValueError("Операція не може бути виконана без двох операндів.")
        if state.op == "+":
            state.screen = state.first_number + state.screen
        elif state.op == "-":
            state.screen = state.first_number - state.screen
        elif state.op == "*":
            state.screen = state.first_number * state.screen
        elif state.op == "/":
            if state.screen == 0:
                raise ValueError("Ділення на нуль неможливе.")
            state.screen = state.first_number // state.screen  # Цілочисельне ділення
        state.first_number = None  # Скидаємо стан
        state.op = None
    else:
        raise ValueError(f"Невідома клавіша: {key}")


def parse(input_string: str) -> list:
    """
    Приймає рядок клавіш і розбиває його на список клавіш.

    Args:
        input_string (str): Рядок, що містить натиснуті клавіші, розділені пробілами.

    Returns:
        list: Масив клавіш.
    """
    if not input_string.strip():
        raise ValueError("Вхідний рядок не може бути порожнім.")
    return input_string.strip().split()


def calculate(keys: list) -> str:
    """
    Обробляє послідовність клавіш і повертає результат разом із прикладом.
    """
    state = CalculatorState()
    example = []  # Зберігаємо приклад для виводу
    for key in keys:
        if key != "=":  # Додаємо клавіші до прикладу, крім "="
            example.append(key)
        handle_key_press(state, key)
    # Формуємо приклад у вигляді рядка
    example_str = " ".join(example)
    return f"{example_str} = {state.screen}"


def process_file_input_output(input_file: str, output_file: str):
    """
    Зчитує клавіші з вхідного файлу, обчислює результат і записує його у вихідний файл.

    Args:
        input_file (str): Шлях до вхідного файлу.
        output_file (str): Шлях до вихідного файлу.
    """
    try:
        # Зчитуємо дані з файлу
        with open(input_file, "r", encoding="utf-8") as file:
            input_data = file.read().strip()

        # Обробляємо дані
        keys = parse(input_data)
        result = calculate(keys)

        # Записуємо результат у файл
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(result)

    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")
    except ValueError as e:
        print(f"Помилка обробки даних: {e}")


if __name__ == "__main__":
    # Приклад використання з файлами
    input_file = "input.txt"
    output_file = "output.txt"

    process_file_input_output(input_file, output_file)
    print(f"Результат записано у файл {output_file}.")
