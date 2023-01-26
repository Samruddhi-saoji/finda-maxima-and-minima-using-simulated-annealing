import numpy as np
from random import random


#the continuous function
def f(x) :
    return (x-0.3)**3 - (5*x) + (x*x) - 2
#the objective function
#obj value = f(state)  # state = x coordinate
#higher f(x) value is better


########## simulated annealing ##################
class Maxima :
    def __init__(self, x_min, x_max, max_temp, min_temp, cooling_rate ) -> None:
        #domain = [x_min, x_max]
        self.x_min = x_min
        self.x_max = x_max
        
        #temperature
        self.max_temp = max_temp  #starting temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp #final temp
            #once temp reaches this minimum value, dont decay it furthur

        #the states (x coordinates)
        self.state = 0 #current state
        self.neighbour = 0 #the next state
        self.best_state = 0

    
    #the actual algorithm
    def annealing(self) :
        #set the starting temperature
        temp = self.max_temp
        min_temp = self.min_temp

        while temp > min_temp :
            #generetes the new state based 
            neighbour = self.generate_neighbour()

            #value of obj function for the states (energy)
            current_energy = f(self.state)
            neighbour_energy = f(neighbour)

            #should we transition to next state?
            if self.transition(current_energy, neighbour_energy, temp) == True :
                #update current state value
                self.state = neighbour
            
            #is this new current state better than the best state found yet ?
            # higher f(x) value = better state
            if f(self.state) > f(self.best_state) :
                #update value of best state
                self.best_state = self.state

            #temperature decay
            temp = temp*(1 - self.cooling_rate)

        #atleast near-optimal solution found
        print(f"Global maxima is  x = {self.best_state} and y = {f(self.best_state)}")
        


    #generate the next state
    #returns a random x coordinate w/in the domain
    def generate_neighbour(self) :
        return self.x_min + (self.x_max - self.x_min)*random()

    
    #return True if we should transition (current state --> neighbour)
    #higher energy = better state
    def transition(self, current_energy, neighbour_energy, temp) :
        if neighbour_energy > current_energy :
            #next state is better
            return True
        else : #next state is worse
            #we accept bad moves only if value of metropolis function is greater than a random value btw (0,1)
            diff = current_energy - neighbour_energy
            #metropolis = e^(cost diff/temp)
            metropolis = np.exp( diff/temp ) #value of metropolis function 
            if metropolis > random() : return True
            else: return False



####################### driver code ###########################
max = Maxima(-2, 2, 100 , 1e-1, 0.02)
max.annealing()

