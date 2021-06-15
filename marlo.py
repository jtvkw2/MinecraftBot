import marlo
client_pool = [('127.0.0.1', 10000)]
join_tokens = marlo.make('MarLo-DefaultWorld-v0',
                          params={
                            "client_pool": client_pool,
                            "agent_names":["Agent-0"]
                          })
# As this is a single agent scenario,
# there will just be a single token
assert len(join_tokens) == 1
join_token = join_tokens[0]

env = marlo.init(join_token)

observation = env.reset()

done = False
while not done:
    _action = env.action_space.sample()
    obs, reward, done, info = env.step(_action)
    print("reward:", reward)
    print("done:", done)
    print("info", info)
env.close()
