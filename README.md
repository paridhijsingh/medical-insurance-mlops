# Medical Insurance & Clinical Intelligence (End-to-End MLOps)

This project demonstrates a full machine learning lifecycle—integrating statistical regression with **Natural Language Processing (NLP)**—deployed on a production-grade AWS Kubernetes (EKS) cluster.

## 🚀 Key Features

- **Multi-Model API:** Single FastAPI gateway for insurance cost prediction and clinical entity extraction.
- **Named Entity Recognition (NER):** Extracts critical data points (Patients, Hospitals, Dates) from unstructured medical notes.
- **Scalable Infrastructure:** Deployed on AWS EKS with Elastic Load Balancing.
- **Containerized:** Dockerized environment including pre-trained neural network models.

## 🛠 Tech Stack

- **Language:** Python 3.12 (MacBook Air Dev Environment)
- **ML & NLP:** Scikit-Learn, Pandas, **spaCy (en_core_web_sm)**
- **Cloud & DevOps:** AWS (ECR, EKS, ELB), Docker, Kubernetes, Jenkins
- **Frameworks:** FastAPI, Pydantic

## 📸 Deployment & NLP Proof

### 1. Insurance Cost Prediction

Verification of the service successfully processing structured data and returning a cost prediction:
![API Success Prediction](./Evidence/success_prediction.png)

### 2. Clinical Entity Extraction (NER)

Proof of the NLP "brain" parsing unstructured clinical notes to identify key entities:
![Clinical NLP Success](./Evidence/Screenshot 2026-04-30 at 11.57.35 AM.png)

## 🏃 How to Run Locally

1. **Install Dependencies:**
   ````bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```It feels great because it looks like a legitimate production service now! You’ve moved from a single-purpose prediction tool to a multi-functional AI platform.
   ````

Your current README is solid, but we need to update it to reflect your new **NLP/Clinical Data** capabilities and the **spaCy** tech stack. Here is how you should structure the updated version to catch a recruiter's eye:

---

# Medical Insurance & Clinical Intelligence (End-to-End MLOps)

This project demonstrates a full machine learning lifecycle—integrating statistical regression with **Natural Language Processing (NLP)**—deployed on a production-grade AWS Kubernetes (EKS) cluster.

## 🚀 Key Features

- **Multi-Model API:** Single FastAPI gateway for insurance cost prediction and clinical entity extraction.
- **Named Entity Recognition (NER):** Extracts critical data points (Patients, Hospitals, Dates) from unstructured medical notes.
- **Scalable Infrastructure:** Deployed on AWS EKS with Elastic Load Balancing.
- **Containerized:** Dockerized environment including pre-trained neural network models.

## 🛠 Tech Stack

- **Language:** Python 3.12 (MacBook Air Dev Environment)
- **ML & NLP:** Scikit-Learn, Pandas, **spaCy (en_core_web_sm)**
- **Cloud & DevOps:** AWS (ECR, EKS, ELB), Docker, Kubernetes, Jenkins
- **Frameworks:** FastAPI, Pydantic

## 📸 Deployment & NLP Proof

### 1. Insurance Cost Prediction

Verification of the service successfully processing structured data and returning a cost prediction:
![API Success Prediction](./Evidence/success_prediction.png)

### 2. Clinical Entity Extraction (NER)

Proof of the NLP "brain" parsing unstructured clinical notes to identify key entities:

![Clinical NLP Success](./Evidence/clinical_nlp_success.png)

## 🏃 How to Run Locally

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
2. **Start the API (Backend):** - uvicorn src.main:app --reload
3. **Start the UI:** - streamlit run streamlit_app.py
