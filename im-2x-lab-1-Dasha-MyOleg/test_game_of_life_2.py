import tempfile
from game_of_life import read_input

def test_read_input_with_tempfile():
    input_data = """3
5 5
.....
.x...
.x...
.x...
.....
"""
    with tempfile.NamedTemporaryFile('w+', delete=False) as temp_file:
        temp_file.write(input_data)
        temp_file.seek(0)
        generations, rows, cols, grid = read_input(temp_file.name)
        assert generations == 3
        assert rows == 5
        assert cols == 5
        assert grid == [
            ['.', '.', '.', '.', '.'],
            ['.', 'x', '.', '.', '.'],
            ['.', 'x', '.', '.', '.'],
            ['.', 'x', '.', '.', '.'],
            ['.', '.', '.', '.', '.']
        ]
