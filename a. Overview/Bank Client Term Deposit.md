# [Bank Client Term Deposit](../c.%20Jupyter%20Notebooks/Bank%20Client%20Term%20Deposits.ipynb)


## Project Overview
This project analyses a bank's client data to understand the social, economic, and behavioural factors influencing a 
client's likelihood to subscribe to a term deposit. The study leverages campaign interaction history, economic 
indicators, and client characteristics.

## Data Dictionary
- Client Attributes:
    - age: Age of the client (years). 
    - duration: Duration of the last contact (seconds). 

- Campaign Details:
  - campaign: Number of contacts made with the client during the current campaign. 
  - pdays: Days since last contact in a previous campaign (999 indicates no prior contact). 
  - previous: Number of contacts before the current campaign.

- Economic Indicators:
  - emp.var.rate: Employment variation rate (quarterly).
  - cons.price.idx: Consumer price index (monthly). 
  - cons.conf.idx: Consumer confidence index (monthly). 
  - euribor3m: Euribor 3-month rate (daily). 
  - nr.employed: Number of employees (quarterly).

- Target Variable:
  - y: Indicates if the client subscribed to a term deposit (yes or no).

## Objective
To build a predictive model that identifies clients who are likely to subscribe to a term deposit, enabling targeted 
marketing efforts and improving campaign efficiency.

## Technology Stack <small>[(View code)](../c.%20Jupyter%20Notebooks/Bank%20Client%20Term%20Deposits.ipynb)</small>
- Language: Python.
- Machine Learning Model: 
