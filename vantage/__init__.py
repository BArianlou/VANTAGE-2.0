"""
VANTAGE 2.0 - Core Engine Package
Exposes the fundamental substrates and engines of the manifold.
Proprietary Architecture - (c) 2026 BArianlou
"""

from .normalization import NormalizationSubstrate
from .regime_classifier import RegimeClassifier
from .drift_engine import DriftEngine
from .trajectory_engine import TrajectoryEngine

__version__ = "1.1.0"
__author__ = "BArianlou"

# This ensures that when someone imports 'core', 
# they have immediate access to the high-force engines.
