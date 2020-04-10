

import sys

import gym
import numpy as np
import gym.spaces


class FishbornEnv(gym.Env):
    metadata = {'render.modes': ['human', 'ansi']}
    MAX_STEPS = 100


    def __init__(self):
        super().__init__()
        # action_space, observation_space, reward_range を設定する
        #角度:足場の上を0度とする

        self.action_space = gym.spaces.Discrete(3)  
        self.observation_space = gym.spaces.Box(
            low=0,
            high=36.0,
            shape=(2,)
        )
        self.reward_range = [-1., 1.]
        self.rotate_arg = 30
        self._reset()

    def _reset(self):
        self.done = False
        self.fish_born = [[0, 90, 180, 270] for _ in range(9)]  # 7:考え得る足場の数
        self.fish_born[0] = []
        self.fish_born[8] = []
        self.pos = 0
        pass

    def _step(self, action):
        # 1ステップ進める処理を記述。戻り値は observation, reward, done(ゲーム終了したか), info(追加の情報の辞書)
        pre_pos = self.pos
        reward = -0.1
        
        if (action == 0):
            pass
        elif (action == 1):
            self.pos += 1
        elif(action == 2):
            self.pos += 2
        if (self.pos >= 8):
            reward = 1
            self.done = True
            

        for j in range(9):
#            self.fish_born[j] = [self.fish_born[j][i] + self.rotate_arg if self.fish_born[j][i] + self.rotate_arg < 360 else self.fish_born[j][i] + self.rotate_arg - 360 for i in range(len(self.fish_born[j]))]
            for i in range(len(self.fish_born[j])):
                self.fish_born[j][i] += self.rotate_arg
                if (self.fish_born[j][i] >= 360):
                    self.fish_born[j][i] -= 360
        
        
        for j in range(pre_pos, self.pos + 1):
            if (self.pos >= 8):
                break
            for i in range(len(self.fish_born[j])):
                if (self.fish_born[j][i] < self.rotate_arg):
                #ボーンにぶつかった
                    reward = -1
                    self.done = True
                    
                 
        observation = [self.pos, self.fish_born[1][0] / 10]
        return observation, reward, self.done, {}

    def _render(self, mode='human', close=False):
        # human の場合はコンソールに出力。ansiの場合は StringIO を返す
        pass

    def _close(self):
        pass

    def _seed(self, seed=None):
        pass
