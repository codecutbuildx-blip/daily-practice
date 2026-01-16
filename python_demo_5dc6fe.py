# Objective: Train a simple AI to play the Google Chrome Dinosaur game using Python and basic reinforcement learning concepts.
# We will focus on teaching the AI to react to the presence of an obstacle.

# Import necessary libraries
import gym  # OpenAI Gym for creating the environment
import numpy as np  # For numerical operations, especially for representing states
import random  # For random actions
import time  # For pausing execution to observe the AI

# 1. Setting up the Environment
# We use OpenAI Gym's "MountainCar-v0" environment as a proxy
# for the Dino game's core mechanics: observe, make a decision, get a reward.
# In a real Dino game AI, we'd use screen scraping or a custom environment.
# MountainCar is a good pedagogical choice because it has a discrete state
# and action space, making it easier to grasp RL concepts.
env = gym.make('MountainCar-v0')

# 2. Understanding the State and Action Space
# State: Represents the current situation of the game.
# For MountainCar, it's [position, velocity].
# Action Space: The set of possible moves the AI can make.
# For MountainCar, it's [0: push left, 1: no push, 2: push right].
# In the Dino game, actions would be [jump, run].
print("Action Space:", env.action_space)
print("Observation Space:", env.observation_space)

# 3. Basic Reinforcement Learning Concept: Q-Learning
# Q-Learning is a model-free RL algorithm that learns an action-value function
# Q(s, a), which represents the expected future reward of taking action 'a'
# in state 's'. The goal is to find a policy that maximizes total reward.

# Q-Table: A lookup table storing Q(s, a) values.
# Since the state space is continuous, we need to discretize it.
# This is a simplification; real-world RL often uses deep neural networks for
# continuous state spaces.
# We'll divide the state space into bins.
# Number of bins for position and velocity.
pos_space = np.linspace(-1.2, 0.6, 10)
vel_space = np.linspace(-0.07, 0.07, 10)

# Initialize the Q-table with zeros.
# The dimensions are (num_pos_bins, num_vel_bins, num_actions).
q_table = np.zeros((len(pos_space), len(vel_space), env.action_space.n))

# 4. Learning Parameters
learning_rate = 0.1  # How much we update Q-values based on new information (alpha)
discount_factor = 0.99  # How much future rewards are valued (gamma)
epsilon = 1.0  # Starting exploration rate: probability of taking a random action
epsilon_decay_rate = 0.0001  # How quickly exploration decreases
max_epsilon = 1.0  # Maximum exploration rate
min_epsilon = 0.01  # Minimum exploration rate

# 5. Helper Function to Discretize State
# This function maps a continuous state (position, velocity) to an index
# in our Q-table. This is crucial for using a Q-table.
def discretize_state(state):
    # Find the index for position
    pos_idx = np.digitize(state[0], pos_space)
    # Find the index for velocity
    vel_idx = np.digitize(state[1], vel_space)
    # Ensure indices are within bounds
    pos_idx = min(pos_idx, len(pos_space) - 1)
    vel_idx = min(vel_idx, len(vel_space) - 1)
    return pos_idx, vel_idx

# 6. Training Loop
# We'll train for a number of episodes.
num_episodes = 20000  # Number of games to play for training

for episode in range(num_episodes):
    # Reset the environment to start a new game
    state, _ = env.reset()
    discretized_s = discretize_state(state)
    done = False  # Flag to check if the game is over
    total_reward = 0  # Accumulate reward for the episode

    # Epsilon-Greedy Strategy: Balance exploration and exploitation
    # With probability epsilon, take a random action (explore).
    # Otherwise, take the action with the highest Q-value for the current state (exploit).
    exploration_threshold = random.uniform(0, 1)

    # Loop for each step within an episode
    while not done:
        # Choose action
        if exploration_threshold > epsilon:
            # Exploit: choose the action with the highest Q-value
            action = np.argmax(q_table[discretized_s])
        else:
            # Explore: choose a random action
            action = env.action_space.sample()

        # Take the chosen action and observe the next state and reward
        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated  # Check if episode ended

        # Discretize the next state
        discretized_next_s = discretize_state(next_state)

        # Update Q-Table using the Q-Learning formula:
        # Q(s, a) = Q(s, a) + learning_rate * [reward + discount_factor * max(Q(s', a')) - Q(s, a)]
        current_q_value = q_table[discretized_s + (action,)]  # Get current Q-value for (s, a)
        max_future_q = np.max(q_table[discretized_next_s])  # Max Q-value for the next state s'

        # Calculate the new Q-value
        new_q_value = current_q_value + learning_rate * (reward + discount_factor * max_future_q - current_q_value)
        q_table[discretized_s + (action,)] = new_q_value  # Update Q-value in the table

        # Move to the next state
        discretized_s = discretized_next_s
        total_reward += reward

    # Decay epsilon after each episode
    epsilon = max(min_epsilon, epsilon - epsilon_decay_rate)

    # Print progress every 1000 episodes
    if (episode + 1) % 1000 == 0:
        print(f"Episode {episode + 1}/{num_episodes}, Epsilon: {epsilon:.2f}, Total Reward: {total_reward:.2f}")

print("Training finished!")

# 7. Example Usage: Running the trained AI
print("\n--- Running the trained AI ---")

# Reset environment for testing
state, _ = env.reset()
discretized_s = discretize_state(state)
done = False
total_reward = 0
steps = 0

# Run for a fixed number of steps or until done
while not done and steps < 1000:  # Limit steps to avoid infinite loops if AI fails
    # Choose action greedily (no exploration during testing)
    action = np.argmax(q_table[discretized_s])

    # Take the action
    next_state, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated

    # Discretize the next state
    discretized_next_s = discretize_state(next_state)

    # Move to the next state
    discretized_s = discretized_next_s
    total_reward += reward
    steps += 1

    # Optional: Render the environment to visualize the AI's performance
    # env.render() # Uncomment this line to see the AI play
    # time.sleep(0.01) # Small delay for visualization

env.close()  # Close the environment window

print(f"AI played for {steps} steps with a total reward of {total_reward:.2f}")