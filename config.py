# Maze parameters - The grid size is 40X40 with each cell size being 25
GRID_WIDTH = 30
GRID_HEIGHT = 30
CELL_SIZE = 30
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE

# Maze Layout
START_STATE = (0, 0)
GOAL_STATE = (GRID_WIDTH - 1, GRID_HEIGHT - 1)

top_wall = [(x, 8) for x in range(4, 9)] + [(x, 8) for x in range(8, 23)] + [(x, 8) for x in range(23, 27)]
bottom_wall = [(x, 22) for x in range(8, 23)]
left_wall_entrance =  [(8, y) for y in range(4, 9)] + [(8, y) for y in range(8, 14)] + [(8, y) for y in range(17, 23)]
right_wall_exit = [(22, y) for y in range(8, 15)] + [(22, y) for y in range(16, 23)]
random_wall1 = [(x, 15) for x in range(0, 6)]
random_wall2 = [(15, y) for y in range(25, 30)]
random_wall3 = [(17, y) for y in range(0, 5)]
random_wall4 = [(x, 20) for x in range(25, 30)]

OBSTACLES_POS = [
    top_wall,
    bottom_wall,
    left_wall_entrance,
    right_wall_exit,
    random_wall1,
    random_wall2,
    random_wall3,
    random_wall4
]

OBSTACLES = {cell for group in OBSTACLES_POS for cell in group}

# Colors
'''
Grid backround - white
Grid line - grey
Obstacles - blackpass
Start cell - red
Goal cell - green
Agent - yellow
Final path - blue
'''
WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
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
OBSTACLE_AVOIDANCE_REWARD = -300
GOAL_REWARD = 100

# Early stopping parameters
CONVERGENCE_THRESHOLD = 1e-3
PATIENCE_COUNT = 5
