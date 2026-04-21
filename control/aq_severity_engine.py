"""
DustVision: AQ Severity Rule Engine
===================================
Classifies predicted/actual Air Quality levels into severity categories.
"""

class SeverityRuleEngine:
    def __init__(self):
        # Define severity thresholds (Standard bins)
        # These can be moved to a Config later
        self.levels = {
            'good': {'max': 50, 'display_name': 'Good', 'color': 'GREEN'},
            'moderate': {'max': 100, 'display_name': 'Moderate', 'color': 'YELLOW'},
            'unhealthy': {'max': 250, 'display_name': 'Unhealthy', 'color': 'ORANGE'},
            'hazardous': {'max': float('inf'), 'display_name': 'Hazardous', 'color': 'RED'}
        }

    def classify(self, pm10, pm25=None, wind_speed=None, humidity=None):
        """
        Takes environmental data and returns severity classification.
        """
        result = self.levels['hazardous'] # Default
        
        if pm10 <= 50:
            result = self.levels['good']
        elif pm10 <= 100:
            result = self.levels['moderate']
        elif pm10 <= 250:
            result = self.levels['unhealthy']
        else:
            result = self.levels['hazardous']
            
        # Optional: Boost severity if wind is high or humidity is low
        # To be implemented in Track 1 refinement
        
        return {
            'level': [k for k, v in self.levels.items() if v == result][0],
            'display_name': result['display_name'],
            'color': result['color']
        }
