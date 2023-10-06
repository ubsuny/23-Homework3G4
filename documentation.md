**Introduction to the example**
Calculating work done. we can also call in work energy theorem. $W=\Delta K E$
Work can be calculated through many other ways but if we have a moving objects with a certain mass and has different velocities at different positions, we can apply work energy theore, and calculate work done. 
$W=\Delta K E$, Here, W is the work done, KE \Delta KE is change in kinetic energy. Here in this example, the change occurese due to change in velocities, mass remains the same. if can be furher simplified by deviding the kinetic energy into KE_before and KE_after and do the calculations.  
**Background:**
A brief introduction of lambda function and map function is given.

**Lambda Function:**
A lambda function, also known as an anonymous function or lambda expression, is a way to create small, inline, and nameless functions in Python. Lambda functions are typically used for simple operations or calculations.


**Example of Lambda function**
- add = lambda x, y: x + y  
result = add(3, 5)  
print(result)
##### Output: 8  
- numbers = [1, 2, 3, 4, 5]  
squared = list(map(lambda x: x**2, numbers))  
print(squared)
##### Output: [1, 4, 9, 16, 25]  



**Map Function:**

The map() function in Python is used to apply a given function to all elements of an iterable (e.g., a list, tuple, or other iterable data structures) and return an iterator. It takes two arguments: the function to apply and the iterable to apply it to. The result is an iterator that yields the results of applying the function to each element of the iterable one by one.



**Example of syntax of map function**

- numbers = [1, 2, 3, 4, 5]  
  squared = list(map(lambda x: x**2, numbers))  
 print(squared)
  ##### Output: [1, 4, 9, 16, 25]



>**Work Calculation and Testing Script by using lambda function and map function:**

This Python script defines a function for calculating work done by a car as a function of its velocities and mass.
It also includes a test function to ensure the correctness of the work calculation function.


**Steps:**
1) Define a function calculate_work_done(velocities, mass).
2) Calculates the work done by a car based on its velocities and mass.
3) Define parameters.
   velocities (list of float): A list of velocities (in m/s) at different points in time.
   mass (float): The mass of the car (in kilograms).
4) Returns:
    - `work_done` (list of float): A list of work done (in joules) at each point in time.
5) test_calculate_work_done()`: Tests the `calculate_work_done` function to ensure its correctness.

6) Usage:
    1. Defines given data (velocities in mph, conversion factor, mass of car).
    2. Converts velocities from mph to m/s by using the lambda function.
    3. Get a list of velocities in m/s by using the map function.
    4. Manually calculate the expected work done at each point.
    5. Calls `calculate_work_done` to calculate work done.
    6. Compares the calculated and expected values within a small tolerance.
    7. Prints the calculated work done.


**Code**
```python
# hw_work_done_G4.py

def calculate_work_done(velocities, mass):
    """
    Calculate and yield the work done at each velocity point.

    Args:
        velocities (list): List of velocities in meters per second.
        mass (float): Mass of the car in kilograms.

    Yields:
        float: Work done at each velocity point in Joules.
    """
    prev_velocity = 0
    for velocity in velocities:
        # Calculate the change in kinetic energy (delta_ke) using the formula for kinetic energy
        delta_ke = 0.5 * mass * (velocity**2 - prev_velocity**2)
        prev_velocity = velocity  # Update the previous velocity for the next iteration
        yield delta_ke  # Yield the calculated work done at each point
     

%%writefile hw_work_done_G4.py
     
Writing hw_work_done_G4.py

import hw_work_done_G4  # Import the function from the module

# Given data
velocities_mph = [10, 20, 30, 40, 50]  # List of velocities in miles per hour
time_hours = 1  # Time in hours
mph_to_mps = 0.44704  # Conversion factor to convert miles per hour to meters per second
mass_of_car = 1000  # Mass of the car in kilograms

# Convert velocities from miles per hour to meters per second using a lambda function
convert_to_mps = lambda v_mph: v_mph * mph_to_mps
velocities_mps = list(map(convert_to_mps, velocities_mph))

# Calculate work done at each point and store it in a list
work_done_list = list(calculate_work_done(velocities_mps, mass_of_car))
print(work_done_list)  # Print the list of work done at each velocity point
```
[WorkDonebyMapAndLambda.md](https://github.com/sharmistharanit/23-Homework3G4/files/12807475/WorkDonebyMapAndLambda.md)

**Pylint Output**
[pylint_output_WorkDone.txt](https://github.com/sharmistharanit/23-Homework3G4/files/12810929/pylint_output_WorkDone.txt)

**References:**
1) https://docs.python.org/3/howto/functional.html#small-functions-and-the-lambda-expression
2) https://docs.python.org/3/library/functions.html#map
3) https://docs.python.org/3/howto/functional.html
4) ChatGPT
