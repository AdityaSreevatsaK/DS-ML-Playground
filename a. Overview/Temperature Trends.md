# [Temperature Trends](../c.%20Jupyter%20Notebooks/Temperature%20Trends.ipynb)

## Project Overview
The project’s objective is to predict temperature in Celsius based on various environmental and seasonal settings using 
machine learning. A firm aims to establish a reliable model that can analyse multiple environmental factors, such as 
humidity, wind speed, visibility, and pressure, to anticipate temperature changes. This data-driven approach will 
support the firm’s resource planning and temperature-dependent operations.

## Objective
To build a predictive model that accurately forecasts temperature (in Celsius) based on environmental and seasonal 
features. By identifying patterns and relationships in the dataset, the firm aims to make data-driven decisions and 
enhance forecasting accuracy for future temperature conditions.

## Data Dictionary
- Formatted Date: Timestamp of the data recording, in a formatted date-time format (e.g., YYYY-MM-DD HH:MM:SS)
- Summary: Brief description of the weather conditions (e.g., Clear, Partly Cloudy, Rain)
- Precip Type: Type of precipitation, if any (e.g., Rain, Snow, None)
- Temperature (C): Recorded temperature in Celsius, serving as the target variable
- Humidity: Relative humidity, represented as a fraction (0 to 1)
- Wind Speed (km/h): Speed of the wind in kilometres per hour
- Wind Bearing (degrees): Direction of the wind in degrees, where 0 represents north
- Visibility (km): Visibility distance in kilometres
- Cloud Cover: Fractional cloud cover, representing the portion of the sky covered by clouds (range: 0 to 1, where 0 
indicates a clear sky and 1 indicates complete cloud cover).
- description if it’s a typo for "Cloud Cover")
- Pressure (millibars): Atmospheric pressure in millibars
- Daily Summary: Summary of the day's weather (e.g., Partly Cloudy throughout the day, Rain in the morning)

## Technology Stack [(View code)](../c.%20Jupyter%20Notebooks/Temperature%20Trends.ipynb)
- Language: Python
- Machine Learning Model: Ridge Regression through Bayesian Optimisation.
