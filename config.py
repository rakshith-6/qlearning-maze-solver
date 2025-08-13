# Maze parameters - The grid size is 40X40 with each cell size being 25
GRID_WIDTH = 40
GRID_HEIGHT = 40
CELL_SIZE = 25
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE

# Maze Layout
START_STATE = (0, 0)
GOAL_STATE = (GRID_WIDTH - 1, GRID_HEIGHT - 1)
OBSTACLES_POS = [
        [(8, 8), (8, 9), (9, 8), (9, 9), (10, 8)],
        [(18, 18), (18, 19), (19, 18), (19, 19), (20, 18), (19, 17)],
        [(25, 25), (25, 26), (26, 25), (26, 26), (27, 25)], 
        [(30, 10), (30, 11), (31, 10), (31, 11), (32, 10)], 
        [(35, 35), (35, 36), (36, 35), (36, 36), (37, 35)]  
]
OBSTACLES = {cell for group in OBSTACLES_POS for cell in group}

# Colors
'''
Grid cells - white
Obstacles - blackpass
Start cell - red
Goal cell - green
Agent - yellow
Final path - blue

'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (170, 170, 170)
YELLOW = (255, 255, 0)

# Q-Learning parameters - Learning rate, Discount factor and exploration rate respectively
ALPHA = 0.1
GAMMA = 0.99
EPSILON = 1.0
EPSILON_DECAY_RATE = 0.9995
EPSILON_MIN = 0.01
NUM_EPISODES = 10000

# Reward structure
'''
We have three types of rewards here
1) Reward for taking a step - Negative, as it should solve in less number of steps
2) Reward for obstacles avoidance - Highly negative, more penalty for going close to the obstacle
3) Reward for reaching the goal - High positive, encouraging reaching the goal state
'''
STEP_REWARD = -1
OBSTACLE_AVOIDANCE_REWARD = -200
GOAL_REWARD = 200
