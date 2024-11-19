# [Bike Rental Demand](../c.%20Jupyter%20Notebooks/Bike%20Rental%20Demand.ipynb)


## Problem Statement
The aim of this project is to predict the daily bike rental count based on various environmental and seasonal factors. 
A bike rental firm seeks to leverage machine learning to understand the key drivers of daily rental demand, enabling 
more effective planning and resource allocation. By analysing patterns within the dataset, the firm aims to anticipate 
future bike demand based on the current and upcoming environmental and seasonal conditions.

## Data Dictionary
- index: Unique identifier for each row
- date: Date of data recording (in YYYY-MM-DD format)
- season: Encoded season variable (1 = Spring, 2 = Summer, 3 = Autumn, 4 = Winter)
- year: Year of recording (0 = First year, 1 = Second year)
- month: Month of recording (1 = January, 12 = December)
- holiday: Indicates if the day is a holiday (1 = Yes, 0 = No)
- weekday: Day of the week (0 = Sunday, 6 = Saturday)
- workingday: Indicates if the day is a working day (1 = Yes, 0 = No)
- weather: Encoded weather condition (1 = Clear, 2 = Cloudy, 3 = Light Rain/Snow, 4 = Heavy Rain/Snow)
- temp: Actual temperature in Celsius
- atemp: Feels-like temperature (adjusted for humidity and wind)
- humidity: Relative humidity percentage
- windspeed: Wind speed, possibly in km/h
- count: Total bike rental count for the day (target variable)

## Objective
To develop a model that accurately predicts the daily count of bike rentals based on environmental and seasonal 
settings. This model will help the firm to forecast demand more effectively, allowing for optimised fleet management 
and improved customer satisfaction.

## Technology Stack <small> [(View code)](../c.%20Jupyter%20Notebooks/Bike%20Rental%20Demand.ipynb) </small>
- Language: Python
- Machine Learning Algorithm: Linear Regression.
