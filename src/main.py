from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# 1. Initialize the FastAPI app
app = FastAPI()

# 2. Load the "Brain" we created in Phase 1
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# 3. Define what the incoming data should look like (Pydantic)
# This is where your Stats background helps with data types!
class PatientData(BaseModel):
    age: int
    sex: int      # 0 for male, 1 for female
    bmi: float
    children: int
    smoker: int   # 1 for yes, 0 for no

# 4. Create the "Predict" endpoint
@app.post("/predict")
def predict_charges(data: PatientData):
    # Convert the incoming JSON data into a format the model understands
    features = np.array([[data.age, data.sex, data.bmi, data.children, data.smoker]])
    
    # Make the prediction
    prediction = model.predict(features)
    
    # Return the result as JSON
    return {"estimated_charges": round(float(prediction[0]), 2)}