import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as random
P = np.array([[0.2972,0.1693,0.2205,0.313],
              [0.2338,0.2633,0.2849,0.2181],
              [0.2071,0.3077,0.2663,0.2189],
              [0.2593,0.2613,0.2279,0.2515]])
state=np.array([[1, 0.0, 0.0,0.0]])
stateHist=state
dfStateHist=pd.DataFrame(state)
distr_hist = [[0,0,0,0]]
for x in range(5):
  state=np.dot(state,P)
  print(state)
  stateHist=np.append(stateHist,state,axis=0)
  dfDistrHist = pd.DataFrame(stateHist)
  dfDistrHist.plot()
  plt.legend([1,2,3,4])
  plt.title('N-State Transition')
  plt.xlabel('Number of transitions')
  plt.ylabel('Transition Probability')
 

fig = plt.figure()
fig.suptitle("Apple Stock Price Simulation")

Number_of_simulations=1000

Final_stockprice=[]

for i in range(Number_of_simulations):
    
    Stock_simulation_days = 50
    initial_price = 166
    state_list=[1,2,3,4]
    state_dict={1:(-12.87,-0.76),
                2:(-0.77,0.08),
                3:(0.09,1.03),
                4:(1.04,11.97)}
    current_price = initial_price
    stock_price=[initial_price]
    return_rate=[]
    state_transition=[1]
    dynamic_state=[1]
    
    for i in range(Stock_simulation_days):
        dynamic_state = random.choices(state_list,weights=tuple(P[dynamic_state[0]-1,:]),k=1)
        state_transition.append(dynamic_state[0])
        change_percent = (random.random() * (state_dict[dynamic_state[0]][1]-state_dict[dynamic_state[0]][0]) + state_dict[dynamic_state[0]][0])
        current_price = current_price * (1 + (change_percent / 100)) 
        return_rate.append(change_percent)
        stock_price.append(current_price)
        
    plt.plot(stock_price,linewidth=0.5)
    plt.legend('', frameon=False)
    plt.xlabel('Day')
    plt.ylabel('Stock Price ($)')
    Final_stockprice.append(current_price)

fig2 = plt.figure()
fig2.suptitle("Predicted Range of Apple Stock Price")
plt.hist(Final_stockprice,10)
plt.xlabel('Predicted Price ($)')
plt.ylabel('Count')
