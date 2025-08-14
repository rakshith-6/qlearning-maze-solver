from solver import MazeSolver
from utils.path_extract import final_path
from utils.game_display import drawDisplay

import pygame

if __name__ == '__main__':
    
    maze_solver = MazeSolver()
    maze_solver.train(drawDisplay)
    
    final_path(maze_solver)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()