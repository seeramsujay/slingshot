# Slingshot: Future Roadmap & Architectural Evolution

Slingshot pairs predictive machine learning with automated cyber-physical feedback loops to suppress dense urban particulate matter (PM2.5/PM10). This document highlights strategic technical expansions.

---

## 1. Spatial-Temporal Forecasting & Atmospheric Modeling

- **Spatial Graph Neural Networks (GNNs)**:
  - Migrate from isolated point regression models to spatiotemporal GNNs (ST-GCN) that model fluid air masses, wind direction vectors, and urban canyon effects across multi-station sensor networks.
- **Satellite Multi-Spectral Calibration**:
  - Ingest real-time Aerosol Optical Depth (AOD) data from Copernicus Sentinel-5P and NASA MODIS satellites to calibrate ground sensor drift automatically.

---

## 2. Cyber-Physical Actuation & LoRaWAN Mesh

- **LoRaWAN Autonomous Actuator Telemetry**:
  - Deploy long-range, low-power LoRaWAN nodes on municipal misting cannons, vegetative green barrier irrigation, and HEPA ventilation intakes.
  - Implement zero-trust cryptographic signature validation for all remote trigger commands.
- **Traffic Signal Synchronization Gateway**:
  - Direct integration into municipal smart city traffic management centers to dynamically route heavy diesel freight traffic away from stagnant particulate hot spots.

---

## 3. Hardware Deployment & Microcontroller Edge

- **Embedded MicroPython / C++ Edge Controller**:
  - Port severity classification and safety fallback logic to low-power ESP32-S3 and Raspberry Pi Zero 2W units for continuous off-grid solar-powered operation.
