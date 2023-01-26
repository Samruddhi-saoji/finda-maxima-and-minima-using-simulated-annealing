import numpy as np
from random import random


#######################################################################
def minima(domain, start_temp, min_temp, cooling_rate) :
    #domain = [x_min, x_max]
    x_min = domain[0]
    x_max = domain[1]

    #the best state found yet
    best_state = 0
    #best state = lowest f(x) value

    temp = start_temp
    state = 0 #current state
    while temp > min_temp :
        #select a random x coordinate in the domain as the next possible state
        neighbour = x_min + (x_max - x_min)*random()

        #should we make the transition (state --> neighbour)
        if transition(state, neighbour, temp) == True :
            #update value of current state
            state = neighbour

        #is this new state better than the best state yet?
        #lower f(x) value = better state
        if f(state) < f(best_state) :
            #update best state value
            best_state = state

        # temperature decay
        temp = temp*cooling_rate
    ### iterations over ####

    #print the results
    print(f"Global minima is  x = {best_state} and y = {f(best_state)}")



#returns true if we should transition (current_state --> neighbour)
def transition( state, neighbour, temp) :
    #cost of current  and neighbour states
    current_cost = f(state)
    neighbour_cost = f(neighbour)

    #if its a good move
    if neighbour_cost < current_cost : #low cost = better state
        return True

    #its a bad move
    # probability of accepting a bad move = value of metropolis function
    diff = current_cost - neighbour_cost
    probability = np.exp( diff/temp )

    if random() < probability :
        return True
    else:
        return False

#######################################################################



###### driver code ###########
#define the function whose minima is to be found
def f(x) :
    return (x-0.5)**3 + (x*x) -7*x + 5 
#cost function   #cost = f(state)

domain = [-2,2]
minima(domain, 100, 1e-1 , 0.95 )
#start temp = 100   #min temp = 1 x 10^(-1)

#expected answer
# x btw 1.5 and 2 
# y just less than -2
