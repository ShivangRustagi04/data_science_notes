import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import streamlit as st

# Load the dataset (replace 'data.csv' with your dataset file)
data = pd.read_csv('practice.csv')

# Assuming you have features and a target column 'failure'
X = data.drop('failure', axis=1)
y = data['failure']

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

# Initialize the Random Forest classifier
model = RandomForestClassifier(random_state=42)

# Hyperparameter tuning using GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1)
grid_search.fit(X_train_scaled, y_train)

# Get the best model from the grid search
best_model = grid_search.best_estimator_

# Make predictions on the validation set
y_pred = best_model.predict(X_val_scaled)

# Evaluate the model
evaluation_report = classification_report(y_val, y_pred)

# Streamlit Web App for Prediction
def predict_failure(data):
    data_scaled = scaler.transform(data)
    prediction = best_model.predict(data_scaled)
    return prediction

st.title("Equipment Failure Prediction")
st.write("Enter sensor data to predict if equipment failure is imminent.")

input_data = []
for feature in X.columns:
    value = st.number_input(f"Enter {feature}", step=0.01)
    input_data.append(value)

if st.button("Predict"):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = predict_failure(input_array)
    st.write("Prediction:", prediction[0])

st.write("Model Evaluation Report:")
st.code(evaluation_report)
