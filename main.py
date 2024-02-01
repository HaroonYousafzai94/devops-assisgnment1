import uvicorn                  # pip install uvicorn
from fastapi import FastAPI     # pip install fastapi

app = FastAPI()

# Define a Home Route
@app.get("/")
def get_home():
    return {"api_version": "1.0"}

# Define a Home Route
@app.get("/test")
def get_test_route():
    return {"test_version": "2.0"}

# RUN the Server
uvicorn.run(app)