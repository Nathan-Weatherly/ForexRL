from TicTacToeEnv import TicTacToeEnv # Imports all dependencies
import numpy as np
import random
import matplotlib.pyplot as plt

env = TicTacToeEnv() # Step 1, (Define Environment, Reward Function, Action Space, Observation Space)

qtableidx = np.zeros((1, 9, 1)) # Step 2, (Initialize Epsilon, Min Epsilon, Epsilon Decrement, Gamma, Alpha, Q-Table, Number of Episodes)
qtable = np.zeros((1, 9, 1)) 
alpha = 0.05 
gamma = 0.99
epsilon = 1
epsilon_decay = 0.000025
epsilon_end = 0.001
episodes = 50000

wins = [] # Creates a place to store training data for visualization

for episode in range(episodes+1): # Step 3, (Iterate over Number of Episodes)
    
    state = env.reset() # Step 3.1, (Define the initial State)
    step = 0

    newstate = True # Checks if the state is in the Q-Table, if not, then updates the index and Q-Table to include the state
    for i in range(qtableidx.shape[0] - 1): 
        if (qtableidx[i, :, :] == state).all():
            newstate = False
            previdx = i
            break
    if newstate:
        qtableidx = np.concatenate((qtableidx, state[np.newaxis, :, :]))
        qtable = np.concatenate((qtable, np.zeros((1, 9, 1))))
        previdx = qtable.shape[0] - 1
    qvalues = qtable[previdx ,: ,:]
    
    while True: # Step 3.2, (Iterate until a Terminal State is reached)
        
        print(f'Step: {step}') # Prints progress in episodes and states
        print(f'Episode: {episode}')
        
        randn = random.uniform(0, 1) # Step 3.2(a), (Choose whether to Exploit or Explore based on current Epsilon)
        if randn > epsilon:
            
            choices = np.argsort(qvalues[:, 0]) # Step 3.2(b), (Pick action using Q-Table given the State and Exploit/Explore)
            nextchoice = 8
            action = choices[nextchoice]
        else:
            action = random.randint(0, 8)
           
        while state[action, 0] != 0: # Makes sure that the selected action is a valid one given the state
            if randn > epsilon:
                nextchoice -= 1
                action = choices[nextchoice]
            else:
                action = random.randint(0, 8)

        print(f'Agent: {action}') # Prints action taken
        
        state, reward, done = env.step(action)# Step 3.2(c), (Take action and receive Next State and Reward from Environment)
        
        newstate = True # Checks if the new state is in the Q-Table, if not, then updates the index and Q-Table to include the state
        for i in range(qtableidx.shape[0] - 1):
            if (qtableidx[i, :, :] == state).all():
                newstate = False
                idx = i
                break
        if newstate:
            qtableidx = np.concatenate((qtableidx, state[np.newaxis, :, :]))
            qtable = np.concatenate((qtable, np.zeros((1, 9, 1))))
            idx = qtable.shape[0] - 1
        qvalues = qtable[idx ,: ,:]
        
        qtable[previdx, action, 0] = qtable[previdx, action, 0] * (1 - alpha) + alpha * (reward + gamma * np.max(qvalues)) # Step 3.2(d), (Calculate Optimal Q-Value using Bellman Equation with Gamma) + Step 3.2(e), (Update Q-Table using Alpha and Optimal Q-Value)
        
        previdx = idx # Transfers new state to old state value in preperation for another step
        step += 1
        
        env.render() # Renders a visualization of the current state
            
        if done: # Exits the step loop if a terminal state has been reached and adds the data to the "wins" list
            if reward == 1:
                print("win")
                wins.append(1)
            elif reward == -1:
                print("lose")
                wins.append(-1) 
            elif reward == 0:
                print("tie")
                wins.append(0)
            break
    
    epsilon = epsilon - epsilon_decay # Step 3.3, (Update Epsilon using the three Epsilon parameters)
    if epsilon < epsilon_end:
        epsilon = epsilon_end

avg = np.convolve(np.asarray(wins), np.ones((1000,))/1000, mode='valid') # Plots the competency of the model over time using "wins"
plt.plot(avg)
plt.show()

np.save("qtable.npy", qtable) # Saves the trained model       
np.save("qtableidx.npy", qtableidx)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
