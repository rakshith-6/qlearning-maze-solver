import pygame
import numpy as np
from config import *

def drawArrow(screen, color, start, end, width):
    pygame.draw.line(screen, color, start, end, width)
    
    dir = np.arctan2(end[1] - start[1], end[0] - start[0])
    arrow_size = 8
    head_ang1 = dir - np.pi/6
    head_ang2 = dir + np.pi/6
    p1 = (end[0] - arrow_size * np.cos(head_ang1), end[1] - arrow_size * np.sin(head_ang1))
    p2 = (end[0] - arrow_size * np.cos(head_ang2), end[1] - arrow_size * np.sin(head_ang2))
    pygame.draw.polygon(screen, color, [end, p1, p2])

def drawDisplay(MazeSolver, cur_pos=None, epi_num=None, q_show=True):
    
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
                offset = CELL_SIZE // 3
                cx, cy = x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2
                
                if best_action == 0:
                    drawArrow(screen, BLUE, (cx, cy), (cx, cy - offset), 2) 
                elif best_action == 1:
                    drawArrow(screen, BLUE, (cx, cy), (cx, cy + offset), 2) 
                elif best_action == 2:
                    drawArrow(screen, BLUE, (cx, cy), (cx - offset, cy), 2) 
                elif best_action == 3:
                    drawArrow(screen, BLUE, (cx, cy), (cx + offset, cy), 2) 
    
    # Agent
    if cur_pos:
        agent_rect = pygame.Rect(cur_pos[0] * CELL_SIZE, cur_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, YELLOW, agent_rect)

    # Episode Text
    if epi_num is not None:
        text = MazeSolver.font.render(f"Episodes: {epi_num}", True, BLACK)
        screen.blit(text, (12, 12))

