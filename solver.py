import config
import numpy as np
import pygame
import random
import time

# The environment setup and agent decision making is encoded in this "MazeSolver" class  

class MazeSolver:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        self.font = pygame.font.SysFont('arial', 14)
        self.clock = pygame.time.Clock()

        '''
        - In agent can take 4 actions i.e, UP(0), DOWN(1), RIGHT(3) and LEFT(4) from any cell.
        - We initialize the Q-table to zero(Q-values correcting to all state and action are taken zero)
        - We start with epsilon of 1(exploration) and eventually decay to 0.01(exploitation)   
        '''
        self.actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.q_table = np.zeros((config.GRID_WIDTH, config.GRID_HEIGHT, len(self.actions)))
        self.epsilon = config.EPSILON

    def select_action(self, state):
        '''
        Epsilon Greedy Approach: With probability EPSILON we will select a random action and with probability 1 - EPSILON 
        we will select the action with highest Q-value(greedy action selection)
        '''
        if random.uniform(0, 1) < self.epsilon:
            return random.random.choice(range(len(self.actions)))
        else:
            return np.argmax(self.q_table[state])
        
    def is_valid_state(self, state):
        x, y = state
        return 0 <= x < config.GRID_WIDTH and 0 <= y < config.GRID_HEIGHT and state not in config.OBSTACLES
        
    def step(self, state, action_index):

        '''
        - We will move to the next state by taking the action selected and also get the some reward for doing so.
        - The agent will end up in the same cell it started in when it tries to move to the obstacles cells or hit 
          the wall with some action. A negative reward is given so as to achieve obstacle avoidance.
        - We end the episode if the agent reaches the goal or hits obstacles or the wall.
        '''
        action = self.actions[action_index]
        next_state_choice = (state[0]+ action[0], state[1]+ action[1])

        if not self.is_valid_pos(next_state_choice):
            reward = config.OBSTACLE_AVOIDANCE_REWARD
            next_state = state
            done = True
        elif next_state_choice == config.GOAL_STATE:
            reward = config.GOAL_REWARD
            next_state = next_state_choice
            done = True
        else:
            reward = config.STEP_REWARD
            next_state = next_state_choice
            done = False

        return next_state, reward, done
    
    def qValue_update(self, state, action_index, reward, next_state):
        '''
        We will update the Q-values using the bellman equation as follows, 
        Q_newVal(s, a) <-- Q_currVal(s, a) + alpha * [r + gamma * argmax_a'(Q(s', a')) - Q_curVal(s, a)] 
        '''
        old_QValOf_curState = self.q_table[state][action_index]
        next_state_maxQ = np.max(self.q_table[next_state])

        new_QValOf_curState = old_QValOf_curState + config.ALPHA * (reward + config.GAMMA * next_state_maxQ - old_QValOf_curState)
        self.q_table[state][action_index] = new_QValOf_curState

    def train(self):
        '''
        - We will run this tabular Q-learning traing loop for some number of episodes. Each episode will run until the goal is 
          reached or if it hits wall or obstacles
        - Everytime we will select an action using epsilon greedy approach, then we take that action form the current state(s) and 
          arrive in the next state(s') recieving some reward, will check if its a goal state or some restricted state, then update 
          the Q-value of state s and then terminate or repeat.
        '''
        print("---Starting Training---")
        for epis in range(config.NUM_EPISODES):
            state = config.START_STATE
            done = False
            total_reward = 0

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                action_index = self.select_action(state)
                next_state, reward, done = self.step(state, action_index)
                self.qValue_update(state, action_index, reward, next_state)

                state = next_state
                total_reward += reward

            # Every 1000 episode animate the learning process 
            if epis % 1000 == 0:
                self.draw(state, epis)
                pygame.display.flip()
                self.clock.tick(60)

        # Epsilon decay
        self.epsilon = np.maximum(self.epsilon * config.EPSILON_DECAY_RATE, config.EPSILON_MIN)
        if (epis + 1) % 100 == 0: 
            print(f"Epsiode : {epis + 1}/{config.NUM_EPISODES},Reward : {total_reward}, Epsilon : {self.epsilon:.4f}")
        print("---Training Finished---")