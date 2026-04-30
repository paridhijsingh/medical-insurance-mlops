import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# 1. DATA PREPARATION (The Stats Foundation)
# In a real scenario, you'd use: df = pd.read_csv('insurance.csv')
data = {
    'age': [19, 18, 28, 33, 32, 31, 46, 37, 37, 60],
    'sex': [1, 0, 0, 0, 0, 1, 1, 1, 0, 1], # 1=female, 0=male
    'bmi': [27.9, 33.7, 33.0, 22.7, 28.8, 25.7, 33.4, 27.7, 29.8, 25.8],
    'children': [0, 1, 3, 0, 0, 0, 1, 3, 2, 0],
    'smoker': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 1=yes, 0=no
    'charges': [16884, 1725, 4449, 21984, 3866, 3756, 8240, 7281, 6406, 28923]
}
df = pd.DataFrame(data)

# 2. FEATURE SELECTION
# X = Independent variables (Predictors), y = Dependent variable (What we predict)
X = df[['age', 'sex', 'bmi', 'children', 'smoker']]
y = df['charges']

# 3. TRAIN-TEST SPLIT (Avoiding Overfitting)
# We hide 20% of the data (X_test/y_test) to evaluate the model later.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. MODEL SELECTION & TRAINING
# Linear Regression finds the line that minimizes the squared distance to all points.
model = LinearRegression()
model.fit(X_train, y_train)

# 5. SERIALIZATION (The Engineering Step)
# We save the trained model as a binary file called 'model.pkl'
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Success! 'model.pkl' created. The brain is trained.")