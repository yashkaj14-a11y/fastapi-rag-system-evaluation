import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Environment variables safely load karna
load_dotenv()

app = FastAPI(
    title="Secure Production API",
    description="Clean and secure backend template for portfolio",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Backend API is running securely!"
    }
