"""
DustVision: Action Mapping System
==================================
Dispatched specific mitigation actions based on severity.
"""

from datetime import datetime

class ActionDispatcher:
    def __init__(self):
        print("🚀 Action Dispatcher Online")

    def dispatch(self, severity_level, context):
        """
        Processes severity and triggers mapped actions.
        """
        actions = []
        success = True
        
        if severity_level == 'unhealthy':
            actions.append({
                'action_type': 'sprinkler',
                'details': {'intensity': 50, 'duration': 300},
                'message': 'Triggered low-intensity spray for unhealthy PM levels.'
            })
        elif severity_level == 'hazardous':
            actions.append({
                'action_type': 'sprinkler',
                'details': {'intensity': 100, 'duration': 600},
                'message': 'CRITICAL: Triggered high-intensity spray.'
            })
            actions.append({
                'action_type': 'notification',
                'details': {'target': 'site_manager'},
                'message': 'Alert sent to site manager.'
            })
            
        return {
            'success': success,
            'timestamp': datetime.now(),
            'severity': severity_level,
            'actions_executed': actions,
            'context': context
        }
