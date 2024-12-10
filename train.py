import pickle
from snake import SnackEnv

def train(env, episodes, epsilon=1.0, epsilon_min=0.1, epsilon_decay=0.99, alpha=0.1, gamma=0.9):
    for episode in range(episodes):
        state = env.reset()
        done = False
        while not done:
            action = env.choose_action(state, epsilon)
            next_state, reward, done = env.step(action)

            if next_state not in env.q_table:
                env.q_table[next_state] = [0]*env.action_space.n
            
            # cap nhat bang
            env.q_table[state][action] = env.q_table[state][action] + alpha*(reward + gamma*(max(env.q_table[next_state])) - env.q_table[state][action])

            state = next_state
        
        epsilon = max(epsilon_decay*epsilon, epsilon_min)
    
    with open("q_table_train.pkl", "wb") as f:
        pickle.dump(env.q_table, f)

    print("Training completed and Q-table saved!")


#train
env = SnackEnv()
train(env,episodes=100000)