# [Relay States](../c.%20Jupyter%20Notebooks/Relay%20States.ipynb)

## Data Dictionary
- N1 - N14: Numeric features representing process parameters such as measurements, environmental factors, or control 
settings.
- M3: Relay position, indicating the state or action of the relay switch.

## Classification
### Project Overview (Classification)
This project involves building a classification model to predict the relay position (M3) based on process monitoring 
data. The dataset includes numeric features representing process parameters and a categorical target feature indicating 
the relay state. The model will help in automating the identification of relay states for improved process control and 
efficiency.

### Objective (Classification)
To develop a supervised classification model that predicts the relay position (M3) based on numeric process parameters, 
enabling automated and accurate detection of operating states for process monitoring and optimisation.

## Clustering
### Project Overview (Clustering)
This project explores the use of clustering techniques to analyse relay state data, aiming to uncover inherent patterns 
and relationships between process monitoring parameters (N11–N14). By grouping data into clusters, the project seeks to 
provide insights into operational behaviours, helping in identifying potential anomalies or operational regimes without 
relying on labelled data. This analysis could guide improvements in process efficiency and control strategies.

### Objective (Clustering)
To perform unsupervised clustering on process monitoring data (N11–N14) to identify distinct groups or patterns, 
enabling better understanding of operational behaviours and supporting data-driven optimisation of relay state 
management.

### Technology Stack <small>[(View Code)](../c.%20Jupyter%20Notebooks/Relay%20States.ipynb)</small>
- Language: Python.
- Machine Learning Algorithm: Agglomerative (Hierarchical) Clustering & Random Forest Classifier.  
