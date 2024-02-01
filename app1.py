import uvicorn                  # pip install uvicorn
from fastapi import FastAPI     # pip install fastapi

app = FastAPI()

# Define a counter
counter = 0


@app.get("/")
def get_home():
    """
    returns the response for the home route
    """
    return {"api_version": "1.0"}

# Define a Home Route
@app.get("/hits")
def get_test_hits():
    """
    Returns the number of hits done on the webpage
    """
    global counter
    counter = counter + 1
    return {"test_version": "2.0"}
if __name__=="__main__":
# RUN the Server'
    uvicorn.run(app, host="0.0.0.0", port = 1010)