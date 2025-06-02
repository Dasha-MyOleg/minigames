def read_input(filename):
    """Зчитує дані з файлу."""
    with open(filename, 'r') as f:
        generations = int(f.readline().strip())  # Кількість поколінь
        rows, cols = map(int, f.readline().strip().split())  # Розміри поля
        grid = [list(f.readline().strip()) for _ in range(rows)]  # Поле
    return generations, rows, cols, grid


def count_neighbors(grid, x, y, rows, cols):
    """Підрахунок сусідів із тороїдальним з'єднанням."""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        # Тороїдальне з'єднання країв
        nx, ny = (x + dx) % rows, (y + dy) % cols
        if grid[nx][ny] == 'x':
            count += 1
    return count


def next_generation(grid, rows, cols):
    """Обчислення наступного покоління з тороїдальним з'єднанням."""
    new_grid = [['.' for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            live_neighbors = count_neighbors(grid, x, y, rows, cols)
            if grid[x][y] == 'x' and live_neighbors in [2, 3]:  # Жива клітина і Залишається живою
                new_grid[x][y] = 'x'
            elif grid[x][y] == '.' and live_neighbors == 3: # Народжується нове життя
                new_grid[x][y] = 'x'
    return new_grid


def simulate(grid, generations, rows, cols):
    """Обчислення всіх поколінь."""
    all_generations = [grid]
    for _ in range(generations):
        grid = next_generation(grid, rows, cols)
        all_generations.append(grid)
    return all_generations


def write_output(filename, grid):
    """Записує поле у файл."""
    with open(filename, 'w') as f:
        for row in grid:
            f.write(''.join(row) + '\n')


if __name__ == "__main__":
    # Зчитання даних з файлу input.txt
    generations, rows, cols, grid = read_input('input.txt')

    # Виводження початкового поля
    print("Початкове поле:")
    for row in grid:
        print(''.join(row))

    # Обчисленяя всіх поколінь
    all_generations = simulate(grid, generations, rows, cols)

    # Виводження фінального поля
    print("\nФінальне поле:")
    for row in all_generations[-1]:
        print(''.join(row))

    # Запис усіх поколінь у файл
    with open('output.txt', 'w') as f:
        for i, generation in enumerate(all_generations):
            f.write(f"Generation {i}:\n")
            for row in generation:
                f.write(''.join(row) + '\n')
            f.write('\n')
