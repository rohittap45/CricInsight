
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
data = pd.read_csv('C:\\Users\\rohit\\OneDrive\\Desktop\\Python\\CAD\\backend\\static\\dataset.csv')
X = data[['batting_team', 'bowling_team', 'city', 'runs_left', 'balls_left', 'wickets_remaining', 'total_run_x']]
y = data['results']  # Target variable

# One-hot encode the categorical features
categorical_features = ['batting_team', 'bowling_team', 'city']
numerical_features = ['runs_left', 'balls_left', 'wickets_remaining', 'total_run_x']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_features),
        ('num', StandardScaler(), numerical_features)
    ])

# Create the pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
pipeline.fit(X_train, y_train)

# Save the model to a file
import joblib
joblib.dump(pipeline, 'ipl_victory_predictor.pkl')

# Evaluate the model
accuracy = pipeline.score(X_test, y_test)
