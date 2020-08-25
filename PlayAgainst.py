import numpy as np

class TicTacToe():
    
    def __init__(self):
        
        self.board = np.zeros((9, 1))
        self.observation = self.board
        self.done = False
        
    def computer(self, qtable, qtableidx):
        
        for i in range(qtableidx.shape[0] - 1):
            if (qtableidx[i, :, :] == self.board).all():
                qvalues = qtable[i, :, :]
                break

        choices = np.argsort(qvalues[:, 0])
        nextchoice = 8
        action = choices[nextchoice]

        while self.board[action, 0] != 0:
            
            nextchoice -= 1
            action = choices[nextchoice]

        self.board[action, :] = 1
        
        reward = 0
        self.observation = self.board 
        
        if self.observation[0, 0] == 1 and self.observation[1, 0] == 1 and self.observation[2, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[3, 0] == 1 and self.observation[4, 0] == 1 and self.observation[5, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[6, 0] == 1 and self.observation[7, 0] == 1 and self.observation[8, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[0, 0] == 1 and self.observation[3, 0] == 1 and self.observation[6, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[1, 0] == 1 and self.observation[4, 0] == 1 and self.observation[7, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[2, 0] == 1 and self.observation[5, 0] == 1 and self.observation[8, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[0, 0] == 1 and self.observation[4, 0] == 1 and self.observation[8, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[2, 0] == 1 and self.observation[4, 0] == 1 and self.observation[6, 0] == 1:
            self.done = True
            reward = 1
            
        if reward == 1:
            
            print('The AI beat you')
            
        if np.nonzero(self.observation==0)[0].shape[0] == 0:
            
            self.done = True
            
            print('You tied the AI')
        
    def human(self, action):
    
        self.board[action, :] = -1
        
        reward = 0
        self.observation = self.board 
        
        if self.observation[0, 0] == -1 and self.observation[1, 0] == -1 and self.observation[2, 0] == -1:
            self.done = True
            reward = -1
        if self.observation[3, 0] == -1 and self.observation[4, 0] == -1 and self.observation[5, 0] == -1:
            self.done = True
            reward = -1
        if self.observation[6, 0] == -1 and self.observation[7, 0] == -1 and self.observation[8, 0] == -1:
            self.done = True
            reward = -1
        if self.observation[0, 0] == -1 and self.observation[3, 0] == -1 and self.observation[6, 0] == -1:
            self.done = True
            reward = -1
        if self.observation[1, 0] == -1 and self.observation[4, 0] == -1 and self.observation[7, 0] == -1:
            self.done = True
            reward = -1
        if self.observation[2, 0] == -1 and self.observation[5, 0] == -1 and self.observation[8, 0] == -1:
            self.done = True
            reward = -1
        if self.observation[0, 0] == -1 and self.observation[4, 0] == -1 and self.observation[8, 0] == -1:
            self.done = True
            reward = -1
        if self.observation[2, 0] == -1 and self.observation[4, 0] == -1 and self.observation[6, 0] == -1:
            self.done = True
            reward = -1 
            
        if reward == -1:
            
            print('You have won!')
            
        if np.nonzero(self.observation==0)[0].shape[0] == 0:
            
            self.done = True
            
            print('You tied the AI')
        
    def reset(self):
        
        self.board = np.zeros((9, 1))
        self.observation = self.board
        self.done = False
        
    def printboard(self):
        
        
        def letter(number):
        
            if number == 0:
                mark = " "
            elif number < 0:
                    mark = "O"
            elif number > 0:
                    mark = "X"
                
            return mark
        
        print(f'   |   |   ')
        print(f' {letter(self.observation[0, 0])} | {letter(self.observation[1, 0])} | {letter(self.observation[2, 0])} ')
        print(f'___|___|___')
        print(f'   |   |   ')
        print(f' {letter(self.observation[3, 0])} | {letter(self.observation[4, 0])} | {letter(self.observation[5, 0])} ')
        print(f'___|___|___')
        print(f'   |   |   ')
        print(f' {letter(self.observation[6, 0])} | {letter(self.observation[7, 0])} | {letter(self.observation[8, 0])} ')
        print(f'   |   |   \n')

qtable = np.load("qtable.npy")
qtableidx = np.load("qtableidx.npy")

game = TicTacToe()

playgame = True

while playgame:
    
    while True:
        
        game.computer(qtable, qtableidx)
        game.printboard()
        if game.done:
            game.reset()
            break
        action = int(input('Your turn (0-8): '))
        game.human(action)
        game.printboard()
        if game.done:
            game.reset()
            break
    
    playagain = input('Play again? (y/n): ')
    
    playgame = playagain == 'y' or playagain == 'Y'































