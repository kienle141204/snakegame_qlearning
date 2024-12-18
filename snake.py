import gym
import numpy as np
import random
from gym import spaces
import pickle

class SnackEnv(gym.Env):
    def __init__(self, grid_size):
        super(SnackEnv, self).__init__() # khởi tạo lớp cha
        self.grid_size = grid_size
        self.action_space = spaces.Discrete(4) # khởi tạo không gian hành động
        self.q_table = {}
        self.start_point = (self.grid_size//2, self.grid_size//2)
        self.points = 0
        self.reset()
    
    def reset(self):
        self.snake = [self.start_point]
        self.food = (np.random.randint(0,self.grid_size), np.random.randint(0,self.grid_size))
        self.current_direction = "right"
        self.done = False
        return self.get_obs()

    def get_obs(self):
        head_x, head_y = self.snake[0]
        food_x, food_y = self.food
        
        food_direction = [
            food_x < head_x, # up
            food_x > head_x, # down
            food_y < head_y, # left
            food_y > head_y # right
        ]
        
        # chướng ngại vật (tường và thân rắn)
        obstacles = [
            head_x - 1 < 0 or (head_x - 1, head_y) in self.snake,  # Up
            head_x + 1 >= self.grid_size or (head_x + 1, head_y) in self.snake,  # Down
            head_y - 1 < 0 or (head_x, head_y - 1) in self.snake,  # Left
            head_y + 1 >= self.grid_size or (head_x, head_y + 1) in self.snake   # Right
        ]
        
    
        # Trạng thái: Food direction, obstacles, current direction
        obs = (tuple(food_direction), tuple(obstacles), self.current_direction)
        return obs

    
    def step(self, action):
        head_x, head_y = self.snake[0]
        if action == 0:
            self.current_direction = "up"
            head_x -=1
        elif action == 1:
            self.current_direction = "down"
            head_x +=1
        elif action == 2:
            self.current_direction = "left"
            head_y -=1
        else :
            self.current_direction = "right"
            head_y +=1
        
        if  head_x < 0 or head_x >= self.grid_size or head_y < 0 or head_y >= self.grid_size or (head_x, head_y) in self.snake:
            reward = -10
            self.done = True
        else:
            self.snake.insert(0,(head_x, head_y))
            
            if (head_x, head_y) == self.food:
                reward = 10
                self.points += 1
                (x, y) = (np.random.randint(0,self.grid_size), np.random.randint(0,self.grid_size))
                while (x,y) in self.snake:
                    (x, y) = (np.random.randint(0,self.grid_size), np.random.randint(0,self.grid_size))
                self.food = (x,y)
            else:
                reward = 1
                self.snake.pop()
            # if len(self.snake) == 10:
            #     self.snake = self.snake[0]
            
        
        return self.get_obs(), reward, self.done

    def choose_action(self, state, epsilon):
        if state not in self.q_table:
            self.q_table[state] = [0] * self.action_space.n
        
        if random.uniform(0,1) < epsilon:
            return self.action_space.sample()
        else:
            return np.argmax(self.q_table[state])
    
            
    
