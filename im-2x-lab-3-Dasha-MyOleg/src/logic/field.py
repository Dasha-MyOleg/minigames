# Цей файл залишено для логіки роботи з ігровим полем
class Field:
    def __init__(self, dimensions, grid):
        self.rows, self.cols = dimensions
        self.landscape = set()  # Координати ландшафту
        self.figure = set()  # Координати фігури

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "#":
                    self.landscape.add((r, c))
                elif cell == "p":
                    self.figure.add((r, c))

    def is_within_bounds(self, row, col):
        """Перевіряє, чи координати знаходяться в межах поля."""
        return 0 <= row < self.rows and 0 <= col < self.cols

    def move_down(self):
        """Зсуває кожну частину фігури вниз, якщо це можливо."""
        new_positions = set()
        stopped = set()

        # Всі координати, які вже зайняті (ландшафт + поточна фігура)
        occupied = self.landscape.union(self.figure)

        for r, c in self.figure:
            new_pos = (r + 1, c)
            # Перевіряємо зіткнення з ландшафтом або іншими частинами фігури
            if new_pos in self.landscape or new_pos in stopped or new_pos in self.figure or not self.is_within_bounds(
                    *new_pos):
                stopped.add((r, c))
            else:
                new_positions.add(new_pos)

        # Оновлюємо стан фігури
        self.figure = new_positions.union(stopped)

        # Якщо всі частини зупинилися, рух припиняється
        return bool(new_positions)

    def drop_figure(self):
        """Циклічно зміщує фігуру вниз до моменту зіткнення."""
        while self.move_down():
            print("Current field state:")
            for row in self.render():
                print(row)
        self.landscape.update(self.figure)  # Фігура стає частиною ландшафту
        self.figure.clear()

    def render(self):
        """Повертає поле у вигляді списку рядків."""
        grid = [["."] * self.cols for _ in range(self.rows)]
        for r, c in self.landscape:
            grid[r][c] = "#"
        for r, c in self.figure:
            grid[r][c] = "p"
        return ["".join(row) for row in grid]
