# 1. Use a stable, standard Python slim image
FROM python:3.12-slim

# 2. Set the "home" folder inside the container
WORKDIR /app

# 3. Apply security updates
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# 4. Copy project files (ensure these files are in the same folder!)
COPY main.py .
COPY model.pkl .

# 5. Install libraries
RUN pip install --no-cache-dir fastapi uvicorn scikit-learn pandas numpy

# 6. Run as a non-root user (Professional Security Practice)
RUN useradd -m appuser
USER appuser

# 7. Start the API server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]