# The Elevator

## Challenge Description

a. Provide code that simulates an elevator.  You may use any language (recommend using java or Python). 

b. Please upload your code Git Hub for a discussion during your interview with our team.

c. Additionally, document all assumptions and any features that weren't implemented.

d. Please be prepared to discuss the assumptions and features that were not implemented during your interview!

## Running the Simulation
This simulation is developed in Python. Any somewhat recent version of Python 3 should be able to execute the code. There are no non-standard package imports.

All code is contained in the `elevator_challenge.py` file. At the top of the file are a few simulation parameters that can be set to modify how the simulation runs: 

### Simulation Parameters
`NUM_FLOORS`     : How many floors are in the elevator

`STARTING_FLOOR` : Which floor does the elevator start on in the simulation

`ITER_PAUSE`     : How long to pause between each iteration

`ARRIVAL_RATE`   : The chance that a person will press a button on a floor for each iteration

`MAX_ITERS`      : How many iterations to run the simulation

### Execution
Running `python ./elevator_challenge.py` from this directory will start the simulation.

### Simulation Output
One iteration of the simulation is when the elevator has to decide which direction to move and whether it needs to pick people up and/or drop them off.

Before each iteration, a `STATUS` message is outputted. This message includes the following:
- current floor of the elevator
- which floor the elevator is moving toward for the first person currently in the queue
- For each floor, how many people are waiting to go up, how many people are waiting to go down, and how many people are currently riding to

This helps determine the state of the simulation and if things are operating as one would expect.

While the iteration is running, the following outputs may be displayed:
- doors opening
- doors closing
- person selecting a floor after entering
- number of people entering the elevator
- number of people exiting the elevator
- elevator becoming idle (ie. no one waiting to get picked up or dropped off)

By tracking all the outputs, one can tell if the elevator is operating as intended as well as if the simulation is tracking people correctly.

## Assumptions and Methodology
Once a person enters the elevator and selects their floor, they will not select any subsequent floors while riding the elevator.

People waiting on the first floor can only press the `up` button, and people on the top floor can only press the `down` button.

Elevator operates in a "queued" fashion. In other words, once the first presses the up/down button, the elevator's priority is to pick that person up; although, it may pick other people up and drop them off along the way. Once it picks that first person up, its next priority is to drop them off. Again, it may pick other people up or drop them off along the way. Once it drops the first person off, it then looks at who is next in the queue from the remaining people on the elevator or waiting to get picked up. It then repeats the process. This ensures that no one gets stuck waiting for extended periods of time (or never gets picked up at all).

Elevator will stop at floors where people are waiting to go in the direction the elevator is already travelling. It will not stop if it passes a floor where a person(s) is waiting to go the opposite direction.





