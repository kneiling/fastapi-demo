from fastapi import FastAPI

from app.api.v1.api import api_router

app = FastAPI()

api_v1_prefix = "/api/v1"
app.include_router(api_router, prefix=api_v1_prefix)


@app.get("/")
def root():
    return {"message": "Hey"}
