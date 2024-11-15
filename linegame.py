import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Konstanta
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
CELL_SIZE = 40
FONT_SIZE = 24
BACKGROUND_COLOR = (255, 255, 255)
GRID_COLOR = (0, 0, 0)
SELECTED_COLOR = (255, 0, 0)
TEXT_COLOR = (0, 0, 0)

# Daftar kata target
TARGET_WORDS = ["PYTHON", "GAME", "SEARCH", "PUZZLE", "CODE"]

# Fungsi untuk membuat grid huruf
def create_grid(size, words):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    for word in words:
        placed = False
        while not placed:
            direction = random.choice(['horizontal', 'vertical', 'diagonal'])
            if direction == 'horizontal':
                row = random.randint(0, size - 1)
                col = random.randint(0, size - len(word))
                if all(grid[row][col + i] in (' ', word[i]) for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row][col + i] = word[i]
                    placed = True
            elif direction == 'vertical':
                row = random.randint(0, size - len(word))
                col = random.randint(0, size - 1)
                if all(grid[row + i][col] in (' ', word[i]) for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row + i][col] = word[i]
                    placed = True
            elif direction == 'diagonal':
                row = random.randint(0, size - len(word))
                col = random.randint(0, size - len(word))
                if all(grid[row + i][col + i] in (' ', word[i]) for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row + i][col + i] = word[i]
                    placed = True

    # Isi huruf acak untuk sel kosong
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    return grid

# Fungsi untuk menggambar grid
def draw_grid(screen, grid, selected_cells):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            cell_rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if (i, j) in selected_cells:
                pygame.draw.rect(screen, SELECTED_COLOR, cell_rect)
            else:
                pygame.draw.rect(screen, BACKGROUND_COLOR, cell_rect)
            pygame.draw.rect(screen, GRID_COLOR, cell_rect, 1)
            text = font.render(grid[i][j], True, TEXT_COLOR)
            screen.blit(text, (j * CELL_SIZE + 10, i * CELL_SIZE + 5))

# Fungsi utama
def main():
    global font
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Word Search Puzzle")
    font = pygame.font.Font(None, FONT_SIZE)

    grid = create_grid(GRID_SIZE, TARGET_WORDS)
    selected_cells = []
    running = True

    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_grid(screen, grid, selected_cells)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE
                if (row, col) not in selected_cells:
                    selected_cells.append((row, col))
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()