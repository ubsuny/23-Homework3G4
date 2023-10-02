import numpy as np

def calculate_kinetic_energy(mass, velocity):
    """Calculates the kinetic energy of a body.

    Args:
        mass: Mass of the body (in kg).
        velocity: Velocity of the body (in m/s).

    Returns:
        Kinetic energy (in Joules).
    """
    return 0.5 * mass * velocity**2

def calculate_work_done(initial_kinetic_energy, final_kinetic_energy):
    """Calculates the work done on a body based on initial and final kinetic energies.

    Args:
        initial_kinetic_energy: Initial kinetic energy (in Joules).
        final_kinetic_energy: Final kinetic energy (in Joules).

    Returns:
        Work done on the body (in Joules).
    """
    return final_kinetic_energy - initial_kinetic_energy

# Example usage:
mass = 2.0  # Mass of the body in kg
initial_velocity = 3.0  # Initial velocity in m/s
final_velocity = 4.0  # Final velocity in m/s

# Calculate initial and final kinetic energies using map.
initial_kinetic_energy = calculate_kinetic_energy(mass, initial_velocity)
final_kinetic_energy = calculate_kinetic_energy(mass, final_velocity)

# Calculate work done using the calculate_work_done function.
work_done = calculate_work_done(initial_kinetic_energy, final_kinetic_energy)

print(f"Initial Kinetic Energy: {initial_kinetic_energy:.2f} J")
print(f"Final Kinetic Energy: {final_kinetic_energy:.2f} J")
print(f"Work Done: {work_done:.2f} J")
