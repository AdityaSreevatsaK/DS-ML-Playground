# [Brain Stroke](../c.%20Jupyter%20Notebooks/Brain%20Stroke.ipynb)


## Problem Statement
Stroke is a leading cause of death and long-term disability worldwide. Early detection of individuals at risk can help 
in timely intervention and medical care. Using available patient data, the goal is to build a machine learning model 
that predicts whether a person is likely to have a stroke based on demographic, health, and lifestyle factors.
## Data Dictionary
- gender: The gender of the individual (Male/Female/Other)
- age: Age of the individual in years
- hypertension: Whether the individual has hypertension (0 = No, 1 = Yes)
- heart_disease: Whether the individual has heart disease (0 = No, 1 = Yes)
- ever_married: Marital status of the individual (Yes/No)
- work_type: Type of employment (e.g., Private, Govt job, Self-employed)
- Residence_type: Type of residence (Urban/Rural)
- avg_glucose_level: Average blood glucose level (mg/dL)
- bmi: Body Mass Index of the individual
- smoking_status: Smoking habits (Never smoked, Formerly smoked, Smokes)
- stroke: Target variable indicating whether the individual had a stroke (0 = No, 1 = Yes)

## Objective
Develop a machine learning model that accurately predicts the likelihood of a stroke based on patient demographics, 
medical history, and lifestyle factors. The model should assist healthcare professionals in identifying high-risk 
individuals for preventive measures.

## Technology Stack <small>[(View code)](../c.%20Jupyter%20Notebooks/Brain%20Stroke.ipynb)</small>
- Language: Python
- Machine Learning Algorithm: Voting classifier (XGBoost, Random Forest) with Logistic Regression as meta-model.
