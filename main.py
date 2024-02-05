<<<<<<< HEAD
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
=======
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
>>>>>>> a0676271efa1b02b3d4aad7de7f1a5647288a51c
uvicorn.run(app)