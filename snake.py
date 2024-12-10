import gym
import numpy as np
import random
from gym import spaces
import pickle

class SnackEnv(gym.Env):
    def __init__(self):
        super(SnackEnv, self).__init__() # khởi tạo lớp cha
        self.grid_size = 10
        self.action_space = spaces.Discrete(4) # khởi tạo không gian hành động
        self.q_table = {}
        self.start_point = [(0,0), (0,9), (9,0), (9,9)]
        self.points = 0
        self.reset()
    
    def reset(self):
        self.snake = [random.choice(self.start_point)]
        self.food = (np.random.randint(0,self.grid_size), np.random.randint(0,self.grid_size))
        self.done = False
        return self.get_obs()

    def get_obs(self):
        head_x, head_y = self.snake[0]
        food_x, food_y = self.food
        obs = (head_x - food_x, head_y - food_y, food_x - head_x, food_y - head_y)
        return obs
    
    def step(self, action):
        head_x, head_y = self.snake[0]
        if action == 0:
            head_x -=1
        elif action == 1:
            head_x +=1
        elif action == 2:
            head_y -=1
        else :
            head_y +=1
        
        if  head_x < 0 or head_x >= self.grid_size or head_y < 0 or head_y >= self.grid_size:
            reward = -10
            self.done = True
        else:
            self.snake.insert(0,(head_x, head_y))
            if (head_x, head_y) == self.food:
                reward = 10
                self.points += 1
                self.food = (np.random.randint(0,self.grid_size), np.random.randint(0,self.grid_size))
            else:
                reward = 1
            self.snake.pop()
        
        return self.get_obs(), reward, self.done

    def choose_action(self, state, epsilon):
        if state not in self.q_table:
            self.q_table[state] = [0] * self.action_space.n
        
        if random.uniform(0,1) < epsilon:
            return self.action_space.sample()
        else:
            return np.argmax(self.q_table[state])
    
            
    
