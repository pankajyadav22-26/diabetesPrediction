import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import pickle

# Step 1: Load the Dataset
print("Loading dataset...")
diabetes_dataset = pd.read_csv('data/diabetes.csv')

# Step 2: Data Inspection (Optional for Debugging)
print("First few rows of the dataset:")
print(diabetes_dataset.head())
print("Dataset Shape:", diabetes_dataset.shape)
print("Outcome Distribution:")
print(diabetes_dataset['Outcome'].value_counts())

# Step 3: Data Preparation
print("Preparing data...")
X = diabetes_dataset.drop(columns='Outcome', axis=1)  # Features
Y = diabetes_dataset['Outcome']  # Target

# Step 4: Data Standardization
print("Standardizing data...")
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)

# Step 5: Train-Test Split
print("Splitting data...")
X_train, X_test, Y_train, Y_test = train_test_split(
    standardized_data, Y, test_size=0.2, stratify=Y, random_state=2
)

# Step 6: Train the Model
print("Training the model...")
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Step 7: Evaluate the Model
print("Evaluating the model...")
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
print(f"Training Accuracy: {training_data_accuracy * 100:.2f}%")

X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
print(f"Test Accuracy: {test_data_accuracy * 100:.2f}%")

# Step 8: Save the Model and Scaler
print("Saving the model and scaler...")
with open('backend/diabetes_model.pkl', 'wb') as model_file:
    pickle.dump(classifier, model_file)

with open('backend/scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print("Model and scaler saved successfully.")