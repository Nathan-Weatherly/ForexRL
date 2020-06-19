# gym-forex
Forex trading environment for OpenAI Gym.

# forex-v0
Simple forex env for trading only USD/CHF.

Episodes:

 - Each episode is one trading week or 5 days (12/24, 12/25, 1/01 weeks are holiday and therefore not considered)
 - Each timestep is one minute so there are 7200 timesteps per episode
 - Weeks are chosen at random from a bank of data between Jan 1 2016 and Dec 31 2018 (Obtained from Dukascopy historical archives)

Actions:

 - Continuous between -1 and 1.
 - 1 is 100% USD with long position
 - -1 is 100% CHF with short position
 - 0 is 50% USD, 50% CHF so it is essentially the same as zero position
 - etc.
 
Observations:

 - Past 4 trading weeks of minute data for ask and bid (O/H/L/C/V) 
 - O/H/L/C at 0.00001 or 1/100,000 accuracy (0.1 pip)
 - V at 10,000s
 - 3D array of ask 2D array stacked on bid 2D array of this format:

Index | Open | High | Low | Close | Volume 
------ | ------ | ------ | ------ | ------ | ------ 
0 | ... | ... | ... | ... | ... 
... | ... | ... | ... | ... | ... 
7199 | ... | ... | ... | ... | ... 

 - 72,000 individual data points
 
Rewards:

 - Reward is the pip change in portfolio value from previous timestep
 - Portfolio value is measured in dollars
 - Formula: (current portfolio value)/(previous portfolio value) * 10,000

 



