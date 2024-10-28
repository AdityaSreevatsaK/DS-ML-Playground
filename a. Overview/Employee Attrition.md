# [Employee Attrition Prediction](../c.%20Jupyter%20Notebooks/Employee%20Attrition.ipynb)


## Project Overview
Attrition in human resources (HR) refers to the reduction of workforce through employee exits such as retirements or 
resignations. High attrition rates pose significant challenges for companies, incurring both the costs of hiring and 
training new employees and impacting brand value. This project aims to build a predictive model for employee attrition 
using historical employee data, enabling the company to take proactive steps in managing workforce stability.

## Dataset Dictionary
- EmployeeID: Unique employee identifier
- Attrition: Attrition status (1 = Yes, 0 = No)
- Age: Employee's age
- TravelProfile: Travel requirement in the job profile
- Department: Employee's department
- HomeToWork: Distance from home to work (in km or miles)
- EducationField: Employee's field of education
- Gender: Gender of the employee
- HourlnWeek: Weekly work hours of the employee
- Involvement: Employee's engagement level in HR activities (1 = Lowest, 5 = Highest)
- WorklifeBalance: Work-life balance rating (1 = Lowest, 5 = Highest)
- Designation: Employee's job designation
- JobSatisfaction: Job satisfaction rating (1 = Lowest, 5 = Highest)
- ESOPS: Ownership of company ESOPs (1 = Yes, 0 = No)
- NumCompaniesWorked: Number of previous companies worked at
- OverTime: Overtime eligibility (1 = Yes, 0 = No)
- SalaryHikelastYear: Percentage of salary hike in the last cycle
- WorkExperience: Total years of work experience
- LastPromotion: Years since last promotion
- CurrentProfile: Years in the current job profile
- MaritalStatus: Marital status of the employee
- MonthlyIncome: Gross monthly income of the employee

## Objective
The primary goal is to predict the likelihood of an employee leaving the company based on multiple factors provided in 
the dataset, such as demographics, job role, and work experience.

## Technology Stack <small>[(View code)](../c.%20Jupyter%20Notebooks/Employee%20Attrition.ipynb)</small>
- Language: Python
- Machine Learning Algorithm: XGBoost (Extreme Gradient Boosting).
