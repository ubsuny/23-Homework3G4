# Tentative Idea of HW3G4 Task
Our main intention in this task is to find the work done by a body moving with different velocities from point A to E. First of all, we will find the initial kinetic energy of the body by using its initial velocity, and again we will calculate the final kinetic energy by using the final velocity, at each point. And at last, we will find the work done by using the concept: work done is equal to change in kinetic energy. For this, we will proceed as follows;
- We will first convert a list of velocities from miles per hour to meters per second using the map function and the lambda           function "convert_to_mps". 
- We define a generator function "calculate_work_done" that calculates the work done at each point along the way by calculating the   change in kinetic energy.
- The generator yields the work done at each point.
- Finally, we iterate through the generator to calculate the work done at each point and accumulate it to find the overall work       done.
