# Medical Insurance Cost Predictor (End-to-End MLOps)

This project demonstrates a full machine learning lifecycle—from training a regression model to deploying it on a production-grade AWS Kubernetes (EKS) cluster.

## 🚀 Key Features

- **Scalable Infrastructure:** Deployed on AWS EKS with Elastic Load Balancing.
- **Production API:** Built with FastAPI and validated with Pydantic.
- **Containerized:** Dockerized with multi-platform builds for cross-environment compatibility.

## 🛠 Tech Stack

- **Language:** Python 3.12-slim
- **Cloud:** AWS (ECR, EKS, ELB)
- **DevOps:** Docker, Kubernetes, kubectl, eksctl
- **ML:** Scikit-Learn, Pandas

## 📸 Deployment Proof

Below is the verification of the FastAPI service successfully processing a request and returning a prediction:

![API Success Prediction](./Evidence/Screenshot 2026-04-30 at 9.32.27 AM.png)

## 🏃 How to Run Locally

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Start the API (Backend):** - uvicorn src.main:app --reload
3. **Start the UI:** - streamlit run streamlit_app.py
