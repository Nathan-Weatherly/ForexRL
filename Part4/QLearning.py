from TicTacToeEnv import TicTacToeEnv
import numpy as np
import random
import matplotlib.pyplot as plt
    
alpha = 0.05

gamma = 0.99

epsilon = 1

epsilon_decay = 0.000025

epsilon_end = 0.001

episodes = 50000

env = TicTacToeEnv()

qtableidx = np.zeros((1, 9, 1))

qtable = np.zeros((1, 9, 1))

wins = []

for episode in range(episodes+1):
    
    state = env.reset()
    
    step = 0
    
    newstate = True
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
    
    while True:
        print(f'Step: {step}')
        print(f'Episode: {episode}')
        randn = random.uniform(0, 1)
        if randn > epsilon:
            choices = np.argsort(qvalues[:, 0])
            nextchoice = 8
            action = choices[nextchoice]
        else:
            action = random.randint(0, 8)
        while state[action, 0] != 0:
            if randn > epsilon:
                nextchoice -= 1
                action = choices[nextchoice]
            else:
                action = random.randint(0, 8)

        print(f'Agent: {action}')
        state, reward, done = env.step(action)
        
        newstate = True
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
        
        qtable[previdx, action, 0] = qtable[previdx, action, 0] * (1 - alpha) + alpha * (reward + gamma * np.max(qvalues))
        
        previdx = idx
        step += 1
        env.render()
            
        if done:
            
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
    
    epsilon = epsilon - epsilon_decay
    if epsilon < epsilon_end:
        epsilon = epsilon_end

avg = np.convolve(np.asarray(wins), np.ones((1000,))/1000, mode='valid')

plt.plot(avg)
plt.show()

np.save("qtable.npy", qtable)       
np.save("qtableidx.npy", qtableidx)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        