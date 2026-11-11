import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "control")))
from aq_severity_engine import SeverityRuleEngine
from action_mapping_system import ActionDispatcher

def test_severity_rule_engine_bins():
    engine = SeverityRuleEngine()

    assert engine.classify(30)['level'] == 'good'
    assert engine.classify(75)['level'] == 'satisfactory'
    assert engine.classify(150)['level'] == 'moderate'
    assert engine.classify(300)['level'] == 'poor'
    assert engine.classify(400)['level'] == 'very_poor'
    assert engine.classify(500)['level'] == 'severe'

def test_severity_wind_bias():
    engine = SeverityRuleEngine()

    # 45 is good without wind alignment
    assert engine.classify(45, wind_speed=0, wind_aligned=0)['level'] == 'good'

    # 45 with wind_aligned=1 and wind_speed=6.0 becomes 45 * 1.2 = 54 ('satisfactory')
    assert engine.classify(45, wind_speed=6.0, wind_aligned=1)['level'] == 'satisfactory'

def test_action_dispatcher(tmp_path):
    log_file = tmp_path / "test_actions.json"
    dispatcher = ActionDispatcher(log_path=str(log_file))

    # Test severe actions
    res = dispatcher.dispatch('severe', {'location': 'Zone_B'})
    actions = res['actions_executed']
    assert len(actions) == 2
    types = [a['type'] for a in actions]
    assert 'water_mist' in types
    assert 'site_alert' in types

    # Test moderate actions
    res_mod = dispatcher.dispatch('moderate', {'location': 'Zone_C'})
    actions_mod = res_mod['actions_executed']
    assert len(actions_mod) == 1
    assert actions_mod[0]['type'] == 'water_mist'
    assert actions_mod[0]['intensity'] == 'LOW'

    # Verify log file exists and has records
    assert log_file.exists()
