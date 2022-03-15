import gym
import numpy as np
import matplotlib


# okay, use the gym.make to set up the env
# basic parameter set up

env = gym.make('MountainCar-v0')
LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 25000
SHOW_EVERY = 1000

# here is the observation of the statement
# like...[0.6  0.07]
# ok now we know the second number is v of the car
# what we do is separate it (highest to lowest) into 20 parts
# and then the environment can be described by 20 kinds(no!!!!!) 20*20 is 400!!! kinds!!!
# each policy of the table is depend on the observation, each state have 3 actions to choose

D_O_S = [20] * len(env.observation_space.high)
discrete_o_w_s = (env.observation_space.high - env.observation_space.low) / D_O_S
# epsilon = 0.1
# START_EPSILON_DECAYING = 1
# END_EPSILON_DECAYING = EPISODES // 2
# epsilon_decay_value = epsilon/(END_EPSILON_DECAYING - START_EPSILON_DECAYING)

# make the continuous observation to the discrete numbers
# the size is 20*20*3


q_table = np.random.uniform(low=-2, high=0, size=(D_O_S + [env.action_space.n]))

# so for every possible combination of observation these are three actions
# for each action there will be a value for it
# ok so that is a random starting Q-value for every action at every combination of observation

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / discrete_o_w_s
    return tuple(discrete_state.astype(np.int64))

#



for episode in range(EPISODES):

    if episode % SHOW_EVERY == 0:
        render = True
    else:
        render = False


    discrete_state = get_discrete_state(env.reset())
    done = False
  

    while not done:

        # if np.random.random() > epsilon:
        #     action = np.argmax(q_table[discrete_state])
        # else:
        #     action = np.random.randint(0, env.action_space.n)
        action = np.random.randint(0, env.action_space.n)
        new_state, reward, done, _ = env.step(action)
        new_discrete_state = get_discrete_state(new_state)
        if render:
            print(f'num of episodes {episode}')
            render = False
            env.render()

        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action, )]
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            q_table[discrete_state + (action, )] = new_q
        elif new_state[0] >= env.goal_position:

            q_table[discrete_state + (action, )] = 0

        discrete_state = new_discrete_state
    # if END_EPSILON_DECAYING >= epsilon >= START_EPSILON_DECAYING:
    #     epsilon -= epsilon_decay_value
env.close()