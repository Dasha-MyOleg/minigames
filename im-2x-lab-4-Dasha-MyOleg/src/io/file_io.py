# src/io/file_io.py
def read_input(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        dimensions = tuple(map(int, lines[0].strip().split()))
        grid = [list(line.strip()) for line in lines[1:]]
        return dimensions, grid
    except Exception:
        raise ValueError("Некоректні дані")


def print_output(grid):
    print("Last field state:")
    for row in grid:
        print(row)
