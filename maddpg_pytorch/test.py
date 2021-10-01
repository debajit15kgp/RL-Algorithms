import numpy as np
from make_env import make_env

env = make_env('simple_adversary')
print('number of agents', env.n)
print('observation space', env.observation_space)
print('action_space',env.action_space)
print('n actions', env.action_space[0].n)

observation = env.reset()

no_op = np.array([1, 0, 0, 0, 0])
action = [no_op, no_op, no_op, no_op]
obs_, reward, done, info = env.step(action)
print(reward)
print(done)
