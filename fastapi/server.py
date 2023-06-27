from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def hellow_world():
    return "Server running."