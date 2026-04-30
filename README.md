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

![API Success Documentation](./Evidence/Screenshot_Success_200.png)
_(Replace this with the actual filename of your "200 Success" screenshot)_

## 🏃 How to Run Locally

1. **Start the API:** `uvicorn src.main:app --reload`
2. **Start the UI:** `streamlit run streamlit_app.py`
