# decaying e-greedy - Exploit and Exploration
# discounted future reward with gamma -> choose action that maximizes (discounted) future reward
# backward calculation with discount (gamma = 0.9) present reward = 0 + 0.9 * max(future reward)
# Converging Q in deterministic world (fixed reward) & in finite state

import gym
import numpy as np
import matplotlib.pyplot as plt
from gym.envs.registration import register

# Register FrozenLake with is_slippery False
register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery' : False}
)

env = gym.make("FrozenLake-v3")

# Initalize table with all zeros
Q = np.zeros([env.observation_space.n, env.action_space.n])
# Discount factor
dis = .99
#Set learning parameters
num_episodes = 2000

# create lists to contain total rewards and steps per episode
rList = []

for i in range(num_episodes):
    # Reset environment and get first new observation
    state = env.reset()
    rAll = 0
    done = False

    e = 1. / ((i // 100) + 1) # Python 2&3

    # the Q-Table learning algorithm
    while not done:
        # Choose an action by e-greedy
        if np.random.rand(1) < e:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])

        # Get new state and reward from environment
        new_state, reward, done, _ = env.step(action)

        # Update Q-Table with new knowledge using learning rate
        Q[state, action] = reward + dis * np.max(Q[new_state, :])

        rAll += reward
        state = new_state

    rList.append(rAll)

print("Success rate: " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print("LEFT DOWN RIGHT UP")
print(Q)

plt.bar(range(len(rList)), rList, color="blue")
# plt.bar(range(len(rList)), rList, color='b', alpha=0.4)
plt.show()
