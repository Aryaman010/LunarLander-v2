import gym
from stable_baselines import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

env_name = 'LunarLander-v2'

env = gym.make(env_name)

episodes = 100

for episode in range(1,episodes-1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score+= reward
    print('Episode:{} Score{}'.format(episode,score))
env.close()