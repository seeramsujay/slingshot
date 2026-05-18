"""
DustVision: Action Mapping System (Refined)
===========================================
Dispatched specific mitigation actions based on severity.
Logs all actions to 'action_log.json' for smart-city governance.
"""

import json
import os
from datetime import datetime

class ActionDispatcher:
    def __init__(self, log_path='control/action_log.json'):
        self.log_path = log_path
        print(f"🚀 Action Dispatcher Online (Logging to {log_path})")

    def dispatch(self, severity_level, context):
        """
        Processes severity and triggers mapped actions.
        """
        actions = []
        
        # 1. Define mapped actions
        if severity_level in ['poor', 'very_poor', 'severe']:
            actions.append({
                'type': 'water_mist',
                'intensity': 'HIGH',
                'duration': 600 if severity_level == 'severe' else 300,
                'target': context.get('location', 'Site_A')
            })
            
            if severity_level == 'severe':
                actions.append({
                    'type': 'site_alert',
                    'message': 'CRITICAL: Cease high-dust operations immediately.',
                    'recipient': 'Site_Manager'
                })
        
        elif severity_level == 'moderate':
            actions.append({
                'type': 'water_mist',
                'intensity': 'LOW',
                'duration': 120,
                'target': context.get('location', 'Site_A')
            })
            
        # 2. Record findings
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'severity': severity_level,
            'node': context.get('location', 'unknown'),
            'predicted_pm10': context.get('predicted_pm10', 0),
            'actions': actions
        }
        
        self._write_to_log(log_entry)
        
        return {
            'success': True,
            'actions_executed': actions,
            'log_entry': log_entry
        }

    def _write_to_log(self, entry):
        """Appends entry to JSON log file."""
        data = []
        if os.path.exists(self.log_path):
            try:
                with open(self.log_path, 'r') as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = []
        
        data.append(entry)
        
        # Keep log size manageable in simulation
        if len(data) > 500:
            data = data[-500:]
            
        with open(self.log_path, 'w') as f:
            json.dump(data, f, indent=4)
