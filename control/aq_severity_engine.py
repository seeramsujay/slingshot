"""
DustVision: AQ Severity Rule Engine (Refined)
=============================================
Classifies predicted/actual Air Quality levels using Indian AQI standards.
Includes "Wind-Alignment" risk factors for construction sites.
"""

class SeverityRuleEngine:
    def __init__(self):
        # Define severity thresholds (Indian AQI PM10 Bins)
        self.levels = {
            'good': {'max': 50, 'display_name': 'Good', 'color': 'GREEN'},
            'satisfactory': {'max': 100, 'display_name': 'Satisfactory', 'color': 'LIGHT_GREEN'},
            'moderate': {'max': 250, 'display_name': 'Moderate', 'color': 'YELLOW'},
            'poor': {'max': 350, 'display_name': 'Poor', 'color': 'ORANGE'},
            'very_poor': {'max': 430, 'display_name': 'Very Poor', 'color': 'RED'},
            'severe': {'max': float('inf'), 'display_name': 'Severe', 'color': 'DARK_RED'}
        }

    def classify(self, pm10, pm25=None, wind_speed=0, wind_aligned=0, humidity=None):
        """
        Takes environmental data and returns severity classification.
        Applies a 'Wind Risk' bias if dust is blowing towards sensors.
        """
        # 1. Apply Wind Risk Bias
        # If wind is strong and aligned, we treat the PM as technically 'riskier'
        effective_pm10 = pm10
        if wind_aligned == 1 and wind_speed > 5.0:
            effective_pm10 = pm10 * 1.2 # 20% risk buffer
            
        # 2. Assign Bin
        level_key = 'severe'
        if effective_pm10 <= 50:
            level_key = 'good'
        elif effective_pm10 <= 100:
            level_key = 'satisfactory'
        elif effective_pm10 <= 250:
            level_key = 'moderate'
        elif effective_pm10 <= 350:
            level_key = 'poor'
        elif effective_pm10 <= 430:
            level_key = 'very_poor'
        else:
            level_key = 'severe'
            
        result = self.levels[level_key]
        
        return {
            'level': level_key,
            'display_name': result['display_name'],
            'color': result['color'],
            'effective_pm10': round(effective_pm10, 2),
            'risk_applied': effective_pm10 > pm10
        }
