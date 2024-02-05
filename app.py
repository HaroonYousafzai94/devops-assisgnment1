import uvicorn
from fastapi import FastAPI

app = FastAPI()

# Declare a Counter
Counter = 0

@app.get("/")
def get_home():
    """
    Return the response from The Home
    """
    return{"app_version":"1.0"}

@app.get("/hits")
def get_hits():
    """
    Return the no of hits done on the webpage
    """
    global Counter
    Counter = Counter + 1
    return f"i have seen {Counter} times"

if __name__ =="__main__":
    uvicorn.run(app, host = "0.0.0.0.", port=1010)
