"""
VANTAGE 2.0 - Regime Classification Engine
Maps normalized vectors to system-state quadrants.
Proprietary Architecture - (c) 2026 BArianlou
"""

class RegimeClassifier:
    def __init__(self):
        # Quadrant mapping based on F and S vectors
        self.quadrants = {
            (True, False): "Q1: MELT-UP (+F, -S)",
            (True, True):  "Q2: BULL (+F, +S)",
            (False, True): "Q3: STALL (-F, +S)",
            (False, False): "Q4: CRASH (-F, -S)"
        }

    def get_regime(self, f_normalized, s_normalized):
        """
        Calculates the instantaneous quadrant state.
        F > 0.5 is considered +F (Kinetic Potential).
        S > 0.5 is considered +S (Structural Friction).
        """
        f_sign = f_normalized > 0.5
        s_sign = s_normalized > 0.5
        
        return self.quadrants.get((f_sign, s_sign))

# Test implementation
if __name__ == "__main__":
    classifier = RegimeClassifier()
    # Example: High Fuel, Low Entropy
    print(f"Status: {classifier.get_regime(0.8, 0.2)}")
