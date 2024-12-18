import pickle
from snake import SnackEnv
import time
from IPython.display import display, clear_output

def train(env, episodes, epsilon=1, epsilon_min=0.0001, epsilon_decay=0.9995, alpha=0.4, alpha_min=0.01, alpha_decay=0.9995, gamma=0.3):
    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0
        while not done:
            action = env.choose_action(state, epsilon)
            next_state, reward, done = env.step(action)

            if next_state not in env.q_table:
                env.q_table[next_state] = [0] * env.action_space.n
            
            # Cập nhật Q-table
            env.q_table[state][action] = env.q_table[state][action] + alpha * (
                reward + gamma * (max(env.q_table[next_state])) - env.q_table[state][action]
            )

            state = next_state
            total_reward += reward
        
        epsilon = max(epsilon_decay * epsilon, epsilon_min)
        # alpha = max(alpha*alpha_decay, alpha_min)
        print(f"Episode {episode + 1}: Total Reward = {total_reward}")

    # Lưu Q-table sau khi huấn luyện
    with open(f"q_table_train_{env.grid_size}_test.pkl", "wb") as f:
        pickle.dump(env.q_table, f)

    print("Training completed and Q-table saved!")

# Train
# env = SnackEnv(20)
# st = time.time()
# total_rewards = train(env, episodes=20000)
# et = time.time()
# print(f"Training time: {et - st} seconds")