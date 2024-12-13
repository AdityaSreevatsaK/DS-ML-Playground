# [Industrial System Monitoring](../c.%20Jupyter%20Notebooks/Industrial%20System%20Monitoring.ipynb)


## Project Overview
This project focuses on analyzing real-time monitoring data from industrial equipment (turbines, compressors, pumps). 
The dataset includes sensor readings like temperature, pressure, vibration, and humidity to detect faulty equipment and 
predict maintenance needs. The goal is to optimize equipment performance, reduce downtime, and enable predictive 
maintenance.

## Data Dictionary
- temperature: The temperature reading (in °C) of the equipment at the time of observation.
- pressure: The pressure reading (in bar) of the equipment at the time of observation.
- vibration: The vibration level (normalized units) indicating mechanical vibrations in the equipment.
- humidity: The humidity percentage recorded at the location of the equipment.
- equipment: The type of industrial equipment being monitored (e.g., Turbine, Compressor, Pump).
- location: The city where the equipment is located.
- faulty: A binary indicator (0 = Not Faulty, 1 = Faulty) specifying if the equipment requires maintenance.

## Objective
The primary objective of this project is to detect the operational status of industrial equipment (such as turbines, 
compressors, and pumps) based on real-time sensor data, including temperature, pressure, vibration, and humidity. By 
building a monitoring system, the goal is to identify faulty equipment, enabling timely maintenance and improving 
operational efficiency.

## Technology Stack <small>[(View Code)](../c.%20Jupyter%20Notebooks/Industrial%20System%20Monitoring.ipynb)</small>
- Language: Python.
- Machine Learning Algorithm: Support Vector Classifier (SVC).
