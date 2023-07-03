from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hellow_world():
    return { "status": 200,
            "message": "Server running."
            }