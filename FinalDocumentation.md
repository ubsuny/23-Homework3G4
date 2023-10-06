[WorkDonebyMapAndLambda (1).md](https://github.com/sharmistharanit/23-Homework3G4/files/12826582/WorkDonebyMapAndLambda.1.md)[pylint_output_WorkDone.txt](https://github.com/sharmistharanit/23-Homework3G4/files/12810929/pylint_output_WorkDone.txt)**Background:**
A brief introduction of lambda function and map function is given.

**Lambda Function:**
A lambda function, also known as an anonymous function or lambda expression, is a way to create small, inline, and nameless functions in Python. Lambda functions are typically used for simple operations or calculations.


**Map Function:**

The map() function in Python is used to apply a given function to all elements of an iterable (e.g., a list, tuple, or other iterable data structures) and return an iterator. It takes two arguments: the function to apply and the iterable to apply it to. The result is an iterator that yields the results of applying the function to each element of the iterable one by one.


**Generator function**
In Python, a generator function is a special type of function that allows you to iterate over a potentially large sequence of values without generating and storing them all in memory at once. Instead of using the return keyword to return a single result, a generator function uses the yield keyword to yield a series of values one at a time.


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

## Stacked Bar Plot Documentation

## Introduction
This code generates a stacked bar plot using Matplotlib to visualize the relationship between velocity and work done. The plot displays work done (in Joules) at different velocities (in mph).

## Code Explanation
The code consists of several components:
**Setting Figure Size**: 
   - `plt.figure(figsize=(10, 6))`: This line sets the size of the figure to be 10 inches in width and 6 inches in height.

2. **Creating the Stacked Bar Plot**:
   - `plt.bar(velocities_mph, work_done_list, width=10, align='center', label='Work Done (Joules)')`: This line creates a stacked bar plot using the `bar()` function from Matplotlib. It uses `velocities_mph` as the x-axis values, `work_done_list` as the y-axis values, sets the bar width to 10 units, aligns the bars to the center of each x-value, and labels the bars as 'Work Done (Joules)'.

3. **Axis Labels and Title**:
   - `plt.xlabel('Velocity (mph)')`: Sets the label for the x-axis as 'Velocity (mph)'.
   - `plt.ylabel('Work Done (Joules)')`: Sets the label for the y-axis as 'Work Done (Joules)'.
   - `plt.title('Work Done vs. Velocity (Stacked Bar Plot)')`: Sets the title of the plot as 'Work Done vs. Velocity (Stacked Bar Plot)'.

4. **Grid Lines**:
   - `plt.grid(axis='y', linestyle='--', alpha=0.7)`: Adds dashed grid lines to the y-axis with an alpha (transparency) value of 0.7 for improved readability.

5. **Legend**:
   - `plt.legend()`: Adds a legend to the plot, which will display the label 'Work Done (Joules)' to explain the meaning of the bars.
6. **Displaying the Plot**:
   - `plt.show()`: Finally, this line displays the generated plot to the user.

## Usage
To use this code, you need to provide values for `velocities_mph` and `work_done_list`, which represent the velocities (in mph) and the corresponding work done (in Joules) for your specific dataset. You can modify these values to create a stacked bar plot for your own data.

**Code**
[Uploading W```python
import math

# Define a function to calculate work done
def calculate_work_done(velocities, mass):
    work_done = []
    prev_velocity = 0
    for velocity in velocities:
        delta_ke = 0.5 * mass * (velocity**2 - prev_velocity**2)
        prev_velocity = velocity
        work_done.append(delta_ke)
    return work_done

# Define a function to test the calculate_work_done function
def test_calculate_work_done():
    # Given data
    velocities_mph = [10, 20, 30, 40, 0]
    mph_to_mps = 0.44704
    mass_of_car = 1000

    # Convert velocities from mph to m/s using the same lambda function
    convert_to_mps = lambda v_mph: v_mph * mph_to_mps
    velocities_mps = list(map(convert_to_mps, velocities_mph))
# Calculate the expected work done at each point manually
    expected_work_done = []
    prev_velocity = 0
    for velocity in velocities_mps:
        delta_ke = 0.5 * mass_of_car * (velocity**2 - prev_velocity**2)
        prev_velocity = velocity
        expected_work_done.append(delta_ke)

    # Calculate work done using the calculate_work_done function
    calculated_work_done = list(calculate_work_done(velocities_mps, mass_of_car))

    # Assert that the calculated work done matches the expected values
    for expected, calculated in zip(expected_work_done, calculated_work_done):
        assert math.isclose(expected, calculated, rel_tol=1e-9), f"Expected {expected}, but got {calculated}"

    print(calculated_work_done)

# Run the test function
test_calculate_work_done()
```

    [9992.238079999997, 29976.714239999994, 49961.1904, 69945.66655999998, -159875.80927999996]



```python

```
orkDonebyMapAndLambda (1).md…]()

![output_1_0](https://github.com/sharmistharanit/23-Homework3G4/assets/143737948/2bb3b4f0-59dd-48a1-8830-777e22dc304c)

**Pylint Output**
[U************* Module Untitled9
Untitled9.ipynb:cell_1:0:0: C0114: Missing module docstring (missing-module-docstring)
Untitled9.ipynb:cell_1:0:0: C0103: Module name "Untitled9" doesn't conform to snake_case naming style (invalid-name)
Untitled9.ipynb:cell_1:6:0: C0103: Constant name "mph_to_mps" doesn't conform to UPPER_CASE naming style (invalid-name)
Untitled9.ipynb:cell_1:7:0: C0103: Constant name "mass_of_car" doesn't conform to UPPER_CASE naming style (invalid-name)
Untitled9.ipynb:cell_1:10:17: C3001: Lambda expression assigned to a variable. Define a function using the "def" keyword instead. (unnecessary-lambda-assignment)
Untitled9.ipynb:cell_1:16:0: C0116: Missing function or method docstring (missing-function-docstring)
Untitled9.ipynb:cell_2:1:0: C0413: Import "from google.colab import drive" should be placed at the top of the module (wrong-import-position)
Untitled9.ipynb:cell_5:1:0: W0104: Statement seems to have no effect (pointless-statement)
Untitled9.ipynb:cell_5:1:0: E0602: Undefined variable 'ls' (undefined-variable)
Untitled9.ipynb:cell_7:1:0: W0104: Statement seems to have no effect (pointless-statement)
Untitled9.ipynb:cell_7:1:0: E0602: Undefined variable 'ls' (undefined-variable)
Untitled9.ipynb:cell_8:1:0: W0104: Statement seems to have no effect (pointless-statement)
Untitled9.ipynb:cell_8:1:0: E0602: Undefined variable 'cd' (undefined-variable)
Untitled9.ipynb:cell_8:1:4: E0602: Undefined variable 'content' (undefined-variable)
Untitled9.ipynb:cell_8:1:18: E0602: Undefined variable 'mydrive' (undefined-variable)
Untitled9.ipynb:cell_8:1:26: E0602: Undefined variable 'colab' (undefined-variable)
Untitled9.ipynb:cell_9:1:0: W0104: Statement seems to have no effect (pointless-statement)
Untitled9.ipynb:cell_9:1:0: E0602: Undefined variable 'ls' (undefined-variable)
Untitled9.ipynb:cell_11:1:0: W0104: Statement seems to have no effect (pointless-statement)
Untitled9.ipynb:cell_11:1:0: E0602: Undefined variable 'ls' (undefined-variable)
Untitled9.ipynb:cell_13:1:0: W0104: Statement seems to have no effect (pointless-statement)
Untitled9.ipynb:cell_13:1:0: E0602: Undefined variable 'ls' (undefined-variable)
Untitled9.ipynb:cell_14:1:0: W0104: Statement seems to have no effect (pointless-statement)
Untitled9.ipynb:cell_14:1:0: E0602: Undefined variable 'ls' (undefined-variable)

-----------------------------------
Your code has been rated at 0.00/10

ploading pylint_output_WorkDone.txt…]()


**References:**
1) https://docs.python.org/3/howto/functional.html#small-functions-and-the-lambda-expression
2) https://docs.python.org/3/library/functions.html#map
3) https://docs.python.org/3/howto/functional.html
4) Chatgpt
