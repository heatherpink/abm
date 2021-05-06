#Agent-Based Model

This repository contains software written to run a basic agent-based model.

##Repository Contents
-license
-model
-agentframework
-documentation
	-model
	-agentframework
-in

##Software purpose
The software is designed to run an agent-based model. The environment is constructed from 
the data contained in the in file, and the agents interact with this environment, eating it
ten units at a time. As the agents consume the environment their store increases. When two
agents interact, their stores are shared equally between them. The model will run for either
the specified number of iterations, or until the agent's store reaches the specified amount.

##How to run
The model is run through the use of the 'run model' button in the presented gui. Once
pressed, an animation will run and will continue until the stopping condition is met.
