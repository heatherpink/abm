# Agent-Based Model

This repository contains software written to run a basic agent-based model.

## Repository Contents
Contents | Description
-------- | -----------
license  | Details of the software licence
model    | Code that runs model
agentframework | Code that defines agentframework class
model documentation | Documentation for model code
agentframework documentation | Documentation for agentframework class
in | Data used to construct environment

## Software purpose
The software is designed to run an agent-based model. The environment is constructed from 
the data contained in the in file, and the agents interact with this environment, eating it
ten units at a time. As the agents consume the environment their store increases. When two
agents interact, their stores are shared equally between them. The model will run for either
the specified number of iterations, or until the agent's store reaches the specified amount.

## How to run
The model is run through the use of the 'run model' button in the presented GUI. Once
pressed, an animation will run and will continue until the stopping condition is met.

##Testing
The code contains a number of ways to check that the model is working correctly using the 
print command. These have been commented out so that the model runs efficiently.

##Further Development
The usability of the model could be improved by allowing the user to define the number of 
agents and iterations before the animation begins.
