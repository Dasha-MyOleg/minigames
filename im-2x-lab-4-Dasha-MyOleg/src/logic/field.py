class Field:
    def __init__(self, dimensions, grid):
        self.dimensions = dimensions
        self.grid = grid
        self.figure = self.extract_figure()
        self.landscape = self.extract_landscape()
        self.render_steps = []  # Список для збереження проміжних станів

    def render(self):
        """Рендеринг поля в текстовому форматі."""
        rendered = [['.' for _ in range(self.dimensions[1])] for _ in range(self.dimensions[0])]
        for x, y in self.landscape:
            rendered[x][y] = '#'
        for x, y in self.figure:
            rendered[x][y] = 'p'
        return [''.join(row) for row in rendered]

    def move_down(self):
        """Рухає всі фігури вниз, якщо це можливо."""
        # Фільтруємо фігури, які вже зіткнулися з ландшафтом або рамкою
        moving_figure = set()
        for x, y in self.figure:
            if (x + 1, y) in self.landscape or x + 1 >= self.dimensions[0]:
                self.landscape.add((x, y))  # Перетворюємо цю частину на ландшафт
            else:
                moving_figure.add((x + 1, y))

        # Якщо всі частини фігури перетворилися на ландшафт, зупиняємо рух
        if not moving_figure:
            return False

        self.figure = moving_figure
        return True

    def drop_figure(self, show_steps=False):
        """Циклічно зміщує фігури вниз до моменту зіткнення."""
        step = 0
        while self.move_down():
            current_state = self.render()
            self.render_steps.append(current_state)  # Збереження стану
            if show_steps:
                print(f"STEP {step}")
                for row in current_state:
                    print(row)
            step += 1

        # Перетворення фігури на ландшафт
        self.landscape.update(self.figure)
        self.figure.clear()

        # Збереження останнього стану
        final_state = self.render()
        self.render_steps.append(final_state)
        if not show_steps:
            print("Last field state:")
            for row in final_state:
                print(row)

    def extract_figure(self):
        """Витягує координати фігури."""
        return {(i, j) for i, row in enumerate(self.grid) for j, cell in enumerate(row) if cell == 'p'}

    def extract_landscape(self):
        """Витягує координати ландшафту."""
        return {(i, j) for i, row in enumerate(self.grid) for j, cell in enumerate(row) if cell == '#'}
