import warnings

import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score, confusion_matrix, cohen_kappa_score, jaccard_score
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import PowerTransformer, StandardScaler

warnings.filterwarnings("ignore")

train_data = pd.read_csv('../a. Datasets/EmployeeAttrition/Train_Dataset.csv')
test_data = pd.read_csv('../a. Datasets/EmployeeAttrition/Test_Dataset.csv')

train_data = train_data.drop_duplicates(keep="first")

train_data.fillna(train_data.median(numeric_only=True), inplace=True)
test_data.fillna(test_data.median(numeric_only=True), inplace=True)

categorical_cols = train_data.select_dtypes(include=['object']).columns
label_encoder = LabelEncoder()

for col in categorical_cols:
    train_data[col] = label_encoder.fit_transform(train_data[col].astype(str))
    if col in test_data.columns:
        test_data[col] = label_encoder.transform(test_data[col].astype(str))

print("Basic clean-up complete.")

X = train_data.drop(columns=['EmployeeID', 'Attrition'])
y = train_data['Attrition']

scaler = StandardScaler()
yeo_johnson = PowerTransformer(method='yeo-johnson')

X = pd.DataFrame(yeo_johnson.fit_transform(X), columns=X.columns)
test_data_transformed = pd.DataFrame(yeo_johnson.transform(test_data.drop(columns=['EmployeeID'])),
                                     columns=test_data.drop(columns=['EmployeeID']).columns)
print("Data transformation complete.")

X = scaler.fit_transform(X)
test_data_scaled = scaler.transform(test_data_transformed)
print("Data scaling complete.")

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=0)

param_grid = {
    'n_estimators': [93, 94, 95, 96, 97, 98],  # Number of boosting rounds (higher = more complex, risk of overfitting)
    'learning_rate': [0.15, 0.20, 0.25, 0.30],
    # Step size shrinkage (lower = slower learning, higher = risk of overfitting)
    'max_depth': [7, 10, 15, 20],  # Maximum depth of each tree (higher = more complex model)
    'min_child_weight': [1.5, 1.55, 1.6, 1.65, 1.7],
    # Minimum sum of instance weight in a child node (higher = less complex)
    'subsample': [0.85, 0.9, 0.95, 1.0],  # Fraction of samples used per boosting round (higher = more data per tree)
    'colsample_bytree': [0.55, 0.56, 0.57, 0.58, 0.6],
    # Fraction of features used per tree (lower = more regularisation)
    'gamma': [0, 0.05, 0.08, 0.1, 0.25],
    # Minimum loss reduction required for a split (higher = more conservative splits)
    'reg_alpha': [0, 0.005, 0.008, 0.01, 0.012, 0.015],
    # L1 regularisation (helps reduce model complexity and overfitting)
    'reg_lambda': [0.5, 0.8, 1, 1.05, 1.1, 1.5],
    # L2 regularisation (also helps reduce complexity, controls weight size)
    'scale_pos_weight': [1, 2, 5, 10],
    # Balances classes by scaling positive instances (useful for imbalanced datasets)
    'max_delta_step': [0, 1, 2, 5],  # Maximum step for weights (useful for class imbalance, improves stability)
    'colsample_bylevel': [0.8, 0.9, 1.0],  # Fraction of features used per tree level (higher = more complex model)
    'colsample_bynode': [0.8, 0.9, 1.0],  # Fraction of features used per tree node (higher = more complex)
}

xgb_model = xgb.XGBClassifier(eval_metric='logloss')

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)

random_search = RandomizedSearchCV(estimator=xgb_model,
                                   param_distributions=param_grid,
                                   n_iter=30,
                                   scoring='accuracy',
                                   cv=cv,
                                   n_jobs=-1,
                                   verbose=1,
                                   random_state=0)

random_search.fit(X_train, y_train,
                  eval_set=[(X_val, y_val)],
                  verbose=False)
print("Model building complete.")

best_xgb_model = random_search.best_estimator_
best_hyperparameters = random_search.best_params_
print(f"Best hyperparameters: {best_hyperparameters}")

y_val_pred_xgb = best_xgb_model.predict(X_val)

val_accuracy_xgb = accuracy_score(y_val, y_val_pred_xgb)
print(f'Validation Accuracy: {val_accuracy_xgb}')

test_predictions_xgb = best_xgb_model.predict(test_data_scaled)

submission_df_xgb = pd.DataFrame({
    'EmployeeID': test_data['EmployeeID'],
    'Attrition': test_predictions_xgb
})

cm = confusion_matrix(y_val, y_val_pred_xgb)
confusion_accuracy = (cm[0, 0] + cm[1, 1]) / cm.sum()
print(f"Confusion Accuracy: {confusion_accuracy}")

kappa = cohen_kappa_score(y_val, y_val_pred_xgb)
print(f"Cohen Kappa Score: {kappa}")

jaccard = jaccard_score(y_val, y_val_pred_xgb)
print(f"Jaccard Score: {jaccard}")

submission_file_path_xgb = ('../d. Output Files/EmployeeAttrition/' + 'EmployeeAttrition_' +
                            str(val_accuracy_xgb)[2:8] + '.csv')
print(f"File name: {submission_file_path_xgb.split('/')[3]}")
submission_df_xgb.to_csv(submission_file_path_xgb, index=False)
