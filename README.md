# gym-forex
Forex trading environments for OpenAI Gym.

# ForexEnv0
Simple forex environment for trading only USD/CHF.

Episodes:

 - Each episode is one trading day (12/25 and 1/01 are not considered due to their holiday nature)
 - Each timestep is one minute so there are 1440 timesteps per episode
 - Weeks are chosen at random from a bank of data between Jan 1 2016 and Dec 31 2018 (Obtained from Dukascopy historical archives)

Actions:

 - Discrete of -1 and 1.
 - 1 is 100% of portfolio with a longposition
 - -1 is 100% of portfolio with a short position
 
Observations:

 - Past trading week of minute data for ask and bid (O/H/L/C/V) 
 - O/H/L/C at 0.00001 or 1/100,000 accuracy (0.1 pip)
 - V at 10,000s
 - 3D array of bid 2D array stacked on ask 2D array of this format:

Index | Open | High | Low | Close | Volume 
------ | ------ | ------ | ------ | ------ | ------ 
0 | ... | ... | ... | ... | ... 
... | ... | ... | ... | ... | ... 
7199 | ... | ... | ... | ... | ... 

 - 72,000 individual data points
 
Rewards:

 - Reward is the pip change in portfolio value (avg of bid/ask close prices) from previous timestep
 - Portfolio value is measured in USD 
 - Initial portfolio value for each episode is 100,000 USD or 1 Lot of USD/CHF
 - Formula: (current portfolio value)/(previous portfolio value) * 10,000

 



