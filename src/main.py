from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os
import spacy

app = FastAPI()

# Load the model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

# 1. FIX: Added 'region' here so the API knows to expect it!
class PatientData(BaseModel):
    age: int
    sex: int      
    bmi: float
    children: int
    smoker: int   
    region: int = 0  

@app.post("/predict")
def predict(input_data: PatientData):
    try:
        # 1. Prepare features - MATCHING THE 5 EXPECTED COLUMNS
        # Check your Phase 1 training to see which 5 you used.
        # It is usually: age, bmi, children, smoker, sex
        features = np.array([[
        input_data.age, 
        input_data.sex, 
        input_data.bmi, 
        input_data.children,
        input_data.smoker
    ]])
        
        # 2. Get prediction
        prediction_output = model.predict(features)
        
        # 3. Apply the "Safety Floor" and return
        raw_val = model.predict(features)[0]
        print(f"DEBUG: Raw model output is {raw_val}") # Check your terminal for this!
        final_prediction = max(0, float(raw_val))
        return {"estimated_charges": final_prediction}
    except Exception as e:
        print(f"Prediction Error: {e}")
        return {"error": str(e)}

# Load the spacy model
nlp = spacy.load("en_core_web_sm")

@app.post("/extract_clinical")
async def extract_clinical(data: dict):
    text = data.get("note", "")
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {
        "status": "success",
        "entities_found": entities
    }