"""
VANTAGE 2.0 - Drift Engine
Calculates state-vector velocity and directional bias.
Proprietary Architecture - (c) 2026 BArianlou
"""

import numpy as np

class DriftEngine:
    def __init__(self):
        self.last_state = None

    def calculate_drift_vector(self, current_state):
        """
        Computes the change in state (Fuel, Entropy) over time.
        Reveals the instantaneous 'Force' acting on the system.
        """
        curr = np.array(current_state)
        
        if self.last_state is None:
            self.last_state = curr
            return np.zeros(2) # Initial state has no drift

        # Drift = Current Position - Previous Position
        drift = curr - self.last_state
        self.last_state = curr
        
        return drift

    def get_drift_metrics(self, drift_vector):
        """
        Returns Magnitude (Speed) and Angle (Direction) of the drift.
        Angle is mapped to the [0, 2π] manifold.
        """
        magnitude = np.linalg.norm(drift_vector)
        angle = np.arctan2(drift_vector[1], drift_vector[0]) # y (Entropy), x (Fuel)
        
        return magnitude, angle

if __name__ == "__main__":
    engine = DriftEngine()
    
    # Simulate a move from Neutral toward Q2 (Bull)
    state_t0 = [0.5, 0.5]
    state_t1 = [0.55, 0.52]
    
    _ = engine.calculate_drift_vector(state_t0)
    v = engine.calculate_drift_vector(state_t1)
    
    mag, ang = engine.get_drift_metrics(v)
    print(f"VANTAGE 2.0 Drift Magnitude: {mag:.4f} | Angle: {ang:.4f} rad")
