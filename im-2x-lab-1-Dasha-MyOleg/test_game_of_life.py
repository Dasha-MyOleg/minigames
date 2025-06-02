from game_of_life import simulate

def test_simulate_multiple_generations():
    grid = [
        ['.', '.', '.', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', '.', '.', '.'],
    ]
    expected_last_generation = [
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', 'x', 'x', 'x', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
    ]

    # Симуляція 1 покоління
    all_generations = simulate(grid, 1, 5, 5)

    # Перевірка останнього покоління
    assert all_generations[-1] == expected_last_generation
