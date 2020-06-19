# gym-forex
Forex trading environment for OpenAI Gym.

# forexv1
Simple forex env for trading only USD/CHF.

Episodes:

 - Each episode is one trading week or 5 days (12/24, 12/25, 1/01 weeks are holiday and therefore not considered)
 - Each minute is a one tick so their are 1440 * 5 = 7200 timesteps per episode
 - Weeks are chosen at random from a bank of data from Jan 1 2016 to Dec 31 2018

Actions:

 - Continuous between -1 and 1.
 - 1 is 100% USD with long position
 - -1 is 100% CHF with short position
 - 0 is 50% USD, 50% CHF so it is essentially the same as zero position
 - etc.
 
Observations:

 - Past 4 trading weeks of minute data for ask and bid (O/H/L/C/V) 
 - O/H/L/C at 0.00001 or 1/100000 accuracy (0.1 pip)
 - V at 10000s
 - 3D array formatted as such:

| Ask | 3d layer 0 |
| Index | Open | High | Low | Close | Volume |
| ------ | 0 | ------ | ------ | ------ | 4 |
| 0 | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
| 7199 | ... | ... | ... | ... | ... |

 



