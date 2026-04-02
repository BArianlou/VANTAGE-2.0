"""
VANTAGE 2.0 - Phase Space Module
Defines the 3D geometric state [Fuel, Entropy, Maturity].
Proprietary Architecture - (c) 2026 BArianlou
"""

import numpy as np

class PhaseSpace:
    def __init__(self, f_init=0.5, s_init=0.5, m_init=0.1):
        """
        Initializes the system state in the 3D manifold.
        F = Fuel (Kinetic Potential)
        S = Entropy (Structural Friction)
        M = Maturity (Temporal Scaling / Inertia)
        """
        self.state = np.array([f_init, s_init, m_init])

    def update_state(self, new_vector):
        """Updates the current coordinates within the manifold."""
        self.state = np.array(new_vector)

    def get_coordinates(self):
        """Returns the current [F, S, M] state."""
        return self.state

    def calculate_distance_from_origin(self):
        """
        Calculates the Euclidean distance to the (0,0,0) singularity.
        Used to measure system density and collapse probability.
        """
        return np.linalg.norm(self.state)

if __name__ == "__main__":
    # Simulate a 'Melt-Up' State (High Fuel, Low Entropy, Low Maturity)
    system = PhaseSpace(f_init=0.9, s_init=0.1, m_init=0.2)
    coords = system.get_coordinates()
    
    print(f"VANTAGE 2.0 Phase Space Coordinates: F={coords[0]}, S={coords[1]}, M={coords[2]}")
    print(f"System Density Metric: {system.calculate_distance_from_origin():.4f}")
