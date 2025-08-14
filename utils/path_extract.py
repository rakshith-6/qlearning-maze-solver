from config import *
from utils.game_display import drawDisplay

import numpy as np
import pygame
import time

def final_path(MazeSolver):
    print("Extracting Final Path.....")
    state = START_STATE
    path = [state]
    drawDisplay(MazeSolver, cur_pos=None, epi_num=None, q_show=True)
    pygame.display.flip()
    time.sleep(2)

    while state != GOAL_STATE:
        '''
        Greedy policy to extract the path - using Q-values we will choose the best or the 
        greedy actions from start to goal 
        '''
        action_index = np.argmax(MazeSolver.q_table[state])
        next_state,_, done = MazeSolver.step(state, action_index)
        
        if done and next_state != GOAL_STATE:
            print("Could not find a path")
            break
        
        state = next_state
        path.append(state)
        
        drawDisplay(MazeSolver, cur_pos=state, epi_num=None, q_show=True)
        
        if len(path) > 1:
            pygame.draw.lines(MazeSolver.screen, BLUE, False, [(p[0] * CELL_SIZE + CELL_SIZE//2, p[1] * CELL_SIZE + CELL_SIZE//2) for p in path], 5)
        pygame.display.flip()
        MazeSolver.clock.tick(10)
        
    print("Path found!")
    print(f"Path length : {len(path)}")