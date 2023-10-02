import numpy as np
import matplotlib.pyplot as plt

# Numerical values for initial velocity and launch angle
initial_velocity = 2.0  # Initial velocity in m/s
launch_angle_degrees = 45.0  # Launch angle in degrees

def calculate_height(time, initial_velocity, launch_angle_radians):
    """Calculates the height of the projectile at a given time.

    Args:
        time: Time at which to calculate the height (in seconds).
        initial_velocity: Initial velocity of the projectile (in m/s).
        launch_angle_radians: Launch angle of the projectile (in radians).

    Returns:
        Height of the projectile at the given time (in meters).
    """
    g = 9.81  # Acceleration due to gravity (m/s^2)
    vertical_velocity = initial_velocity * np.sin(launch_angle_radians)
    return vertical_velocity * time - 0.5 * g * time**2

def calculate_horizontal_distance(time, initial_velocity, launch_angle_radians):
    """Calculates the horizontal distance traveled by the projectile at a given time.

    Args:
        time: Time at which to calculate the horizontal distance (in seconds).
        initial_velocity: Initial velocity of the projectile (in m/s).
        launch_angle_radians: Launch angle of the projectile (in radians).

    Returns:
        Horizontal distance traveled by the projectile at the given time (in meters).
    """
    horizontal_velocity = initial_velocity * np.cos(launch_angle_radians)
    return horizontal_velocity * time

def projectile_motion_parameters(initial_velocity, launch_angle_degrees):
    """Calculates various parameters of projectile motion.

    Args:
        initial_velocity: Initial velocity of the projectile (in m/s).
        launch_angle_degrees: Launch angle of the projectile (in degrees).

    Returns:
        A dictionary containing the following parameters:
        - maximum_height: Maximum height reached by the projectile (in meters).
        - maximum_range: Maximum horizontal range of the projectile (in meters).
        - time_of_flight: Total time of flight (in seconds).
        - velocity_at_time: Function to calculate velocity at a given time.
    """
    # Convert launch angle from degrees to radians.
    launch_angle_radians = np.radians(launch_angle_degrees)

    # Calculate time of flight using kinematic equation.
    time_of_flight = (2 * initial_velocity * np.sin(launch_angle_radians)) / 9.81

    # Calculate maximum height using time of flight.
    maximum_height = calculate_height(time_of_flight / 2, initial_velocity, launch_angle_radians)

    # Calculate maximum range using time of flight and initial horizontal velocity.
    maximum_range = initial_velocity**2 * np.sin(2 * launch_angle_radians) / 9.81

    # Define a function to calculate velocity at any given time.
    def velocity_at_time(time):
        return np.sqrt((initial_velocity * np.cos(launch_angle_radians))**2 +
                       (initial_velocity * np.sin(launch_angle_radians) - 9.81 * time)**2)

    return {
        "maximum_height": maximum_height,
        "maximum_range": maximum_range,
        "time_of_flight": time_of_flight,
        "velocity_at_time": velocity_at_time
    }

parameters = projectile_motion_parameters(initial_velocity, launch_angle_degrees)

# Create an array of time values for plotting the trajectory.
time_values = np.linspace(0, parameters["time_of_flight"], num=1000)

# Use map to calculate the x and y coordinates for the trajectory.
x_coordinates = list(map(lambda t: calculate_horizontal_distance(t, initial_velocity, np.radians(launch_angle_degrees)), time_values))
y_coordinates = list(map(lambda t: calculate_height(t, initial_velocity, np.radians(launch_angle_degrees)), time_values))

# Plot the trajectory (y vs. x).
plt.figure(figsize=(8, 6))
plt.plot(x_coordinates, y_coordinates)
plt.title("Projectile Motion: Trajectory (y vs. x)")
plt.xlabel("Range (m)")
plt.ylabel("Height (m)")
plt.grid(True)

# Print the calculated parameters explicitly.
print("Projectile Motion Parameters:")
print(f"Maximum Height: {parameters['maximum_height']:.2f} meters")
print(f"Maximum Range: {parameters['maximum_range']:.2f} meters")
print(f"Time of Flight: {parameters['time_of_flight']:.2f} seconds")

plt.show()
