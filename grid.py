# grid.py
import random
import string
from settings import GRID_SIZE, WORDS

def generate_empty_grid():
    return [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def place_word_in_grid(word, grid):
    word_len = len(word)
    direction = random.choice(['horizontal', 'vertical'])
    placed = False

    while not placed:
        if direction == 'horizontal':
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - word_len)
            if all(grid[row][col + i] == ' ' for i in range(word_len)):
                for i in range(word_len):
                    grid[row][col + i] = word[i]
                placed = True
        elif direction == 'vertical':
            row = random.randint(0, GRID_SIZE - word_len)
            col = random.randint(0, GRID_SIZE - 1)
            if all(grid[row + i][col] == ' ' for i in range(word_len)):
                for i in range(word_len):
                    grid[row + i][col] = word[i]
                placed = True

def fill_grid(grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == ' ':
                grid[row][col] = random.choice(string.ascii_uppercase)

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

if __name__ == "__main__":
    grid = generate_empty_grid()

    for word in WORDS:
        place_word_in_grid(word, grid)

    fill_grid(grid)

    print("Word Search Puzzle:")
    print_grid(grid)