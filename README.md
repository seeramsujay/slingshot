# Slingshot (DustVision)

Adaptive Urban Dust Mitigation Framework.

## Project Structure
- `control/`: Logic engines, orchestrators, and APIs.
- `ml/`: PM forecasting models and feature engineering.
- `data/`: Sensor data and fused events.
- `scripts/`: Simulation and fusion scripts.
- `docs/`: System documentation.
- `conductor/`: Project context (managed).
- `Archives/`: Internal roadmap and future steps.

## Quick Start
1. **Initialise**: Python 3.10+ required.
2. **Setup**: `pip install -r requirements.txt`.
3. **Train**: `python ml/pm_forecast.py` to generate the model.
4. **Run**: `python control/orchestrator.py` to start the simulation loop.

## Components
- **Orchestrator**: Integrates all modules in `control/orchestrator.py`.
- **Severity Engine**: Classified AQI in `control/aq_severity_engine.py`.
- **Action Dispatcher**: Mitigation triggers in `control/action_mapping_system.py`.

## License
MIT
