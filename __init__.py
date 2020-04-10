from gym.envs.registration import register

register(
    id='Fishborn-v0',
    entry_point='Fishborn_AI.env:FishbornEnv'
)