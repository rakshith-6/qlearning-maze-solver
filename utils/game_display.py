import pygame
import numpy as np
from config import *

def drawDisplay(MazeSolver, cur_pos=None, epi_num=None, q_show=False):
    
    screen = MazeSolver.screen
    screen.fill(WHITE)
    
    # Grid lines
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WINDOW_WIDTH, y))

    # Start and Goal cells
    start_rect = pygame.Rect(START_STATE[0] * CELL_SIZE, START_STATE[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, start_rect)
    goal_rect = pygame.Rect(GOAL_STATE[0] * CELL_SIZE, GOAL_STATE[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, GREEN, goal_rect)

    # Obstacle cells
    for obs in OBSTACLES:
        rect = pygame.Rect(obs[0] * CELL_SIZE, obs[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLACK, rect)

    # Q-values as arrows
    if q_show:
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if (x, y) in OBSTACLES or (x, y) == GOAL_STATE: continue
                best_action = np.argmax(MazeSolver.q_table[x, y])
                cx, cy = x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2
                if best_action == 0:
                    pygame.draw.line(screen, BLUE, (cx, cy), (cx, cy - CELL_SIZE//3), 2) 
                elif best_action == 1:
                    pygame.draw.line(screen, BLUE, (cx, cy), (cx, cy + CELL_SIZE//3), 2) 
                elif best_action == 2:
                    pygame.draw.line(screen, BLUE, (cx, cy), (cx - CELL_SIZE//3, cy), 2) 
                elif best_action == 3:
                    pygame.draw.line(screen, BLUE, (cx, cy), (cx + CELL_SIZE//3, cy), 2) 
    
    # Agent
    if cur_pos:
        agent_rect = pygame.Rect(cur_pos[0] * CELL_SIZE, cur_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, YELLOW, agent_rect)

    # Episode Text
    if epi_num is not None:
        text = MazeSolver.font.render(f"Episodes: {epi_num}", True, BLACK)
        screen.blit(text, (10, 10))


