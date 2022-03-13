import numpy as np
import gym
from gridworld import CliffWalkingWapper

env = gym.make('CliffWalking-v0')

obs = env.reset()
while True:
    action = np.random.randint(0, 4)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        break
