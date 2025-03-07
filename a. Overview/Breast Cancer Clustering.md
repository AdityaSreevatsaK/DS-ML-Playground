# [Breast Cancer](../c.%20Jupyter%20Notebooks/Breast%20Cancer%20Clustering.ipynb)


## Project Overview
This project involves analysing a breast cancer dataset to identify natural groupings within tumour characteristics. 
The dataset includes various features representing tumour measurements and derived statistics, providing critical 
insights into potential patterns and similarities among cases.

## Data Dictionary
- ID: Unique identification number for each observation.
- Diagnosis: The diagnosis of breast tissues (M = malignant, B = benign).
- radius_mean: Average distance from the centre to points on the perimeter.
- texture_mean: Standard deviation of grey-scale values.
- perimeter_mean: Average size of the core tumour perimeter.
- area_mean: Average size of the core tumour area.
- smoothness_mean: Average local variation in radius lengths.
- compactness_mean: Average value of (perimeter²/area - 1.0).
- concavity_mean: Average severity of concave portions of the tumour's contour.
- concave points_mean: Average count of concave portions in the tumour's contour.
- symmetry_mean: Average symmetry of the tumour.
- fractal_dimension_mean: Average "coastline approximation" (fractal dimension).
- radius_se: Standard error for the average distance from the centre to points on the perimeter.
- texture_se: Standard error for standard deviation of grey-scale values.
- perimeter_se: Standard error of the perimeter.
- area_se: Standard error of the area.
- smoothness_se: Standard error for local variation in radius lengths.
- compactness_se: Standard error for (perimeter²/area - 1.0).
- concavity_se: Standard error for severity of concave portions of the contour.
- concave points_se: Standard error for count of concave portions in the tumour's contour.
- symmetry_se: Standard error of the symmetry.
- fractal_dimension_se: Standard error for "coastline approximation" (fractal dimension).
- radius_worst: Largest average distance from the centre to points on the perimeter.
- texture_worst: Largest standard deviation of grey-scale values.
- perimeter_worst: Largest tumour perimeter.
- area_worst: Largest tumour area.
- smoothness_worst: Largest local variation in radius lengths.
- compactness_worst: Largest value of (perimeter²/area - 1.0).
- concavity_worst: Largest severity of concave portions of the tumour's contour.
- concave points_worst: Largest count of concave portions in the tumour's contour.
- symmetry_worst: Largest symmetry of the tumour.
- fractal_dimension_worst: Largest "coastline approximation" (fractal dimension).

## Objective
The objective is to apply unsupervised learning techniques to cluster tumours into distinct groups based on their 
features. This analysis can help in understanding hidden structures in the data, aiding further research and exploratory 
insights into tumour classification.

## Technology Stack <small>[(View Code)](../c.%20Jupyter%20Notebooks/Breast%20Cancer%20Clustering.ipynb)</small>
- Language: Python.
- Machine Learning Algorithm: Agglomerative Clustering.
