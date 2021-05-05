# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:00:52 2021

@author: Heather
"""
import random


class Agent():
    
    """
    A class to represent an agent.
    
    ...
    
    Attributes
    ----------
    
    environment: list
        a reference to the environment the agents will interact with and within
    y: int
        y co-ordinate of agent's position
    x: int
        x co-ordinate of agent's position
    agents: list
        a reference to the list of other agents within the model
    store: int
        the amount of the environment the agent has consumed
    
    Methods
    -------
    
    distance_between
        Calculates the distance between agents
    move
        Move the agents around the environment randomly
    eat
        The agents consume the environment and the amount is added to the
        agent's store
    share_with_neighbours
        If two agents come into contact, shares both agents stores equally 
        between them
    """
    
       
    #Creates each agent within the environment, each containing an x and y 
    #value, a list of other agents, and a store
    def __init__(self, environment, y, x, agents):
        """
        Constructs an agent.
        
        Parameters
        ----------
        environment: list
            a reference to the environment the agents will interact with and
            within
        y: int
            y co-ordinate of agent's position
        x: int
            x co-ordinate of agent's position
        agents: list
            a reference to the list of other agents within the model
        store: int
            the amount of the environment the agent has consumed

        Returns
        -------
        None.

        """
        self.environment = environment
        self.y = y
        self.x = x
        self.agents = agents
        self.store = 0
    
    
    #Calculates the distance between each agent    
    def distance_between(self, agent):
        """
        Calculates the distance between each agent.

        Parameters
        ----------
        agent : list
            DESCRIPTION.

        Returns
        -------
        int
            The distance calculated between agents

        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5


    #Moves each agent, the direction is determined by a random number generator
    def move(self):
        """
        Randomly moves each agent.
        
        The x and y co-ordinates of each agent are changed based off of a 
        randomly-generated number.

        Returns
        -------
        None.

        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
            
        if random.random()  <0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
    
    
    #The agent 'eats' the environment and the value is added to the agent's 
    #store        
    def eat(self): 
        """
        The agent eats the environment.
        
        When moving to a new position within the environment, the agent removes
        10 from the environment (where the value of the location in the
        environment is greater than 10. This is then added to the agent's store.

        Returns
        -------
        None.

        """
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    
    
    #If the agent comes into contact with another agent, the store of each 
    #agent is shared equally between them
    def share_with_neighbours(self, neighbourhood):
        """
        Agents coming into contact with each other share their store.
        
        When two agents move to within a defined distance of each other their
        store is added together and divided equally between them.

        Parameters
        ----------
        neighbourhood : int
            An integer defined within the neighbourhood variable

        Returns
        -------
        None.

        """    
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum / 2
                    self.store = ave
                    agent.store = ave
                    
            
                    