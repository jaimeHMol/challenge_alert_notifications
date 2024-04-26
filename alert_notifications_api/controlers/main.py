from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def status():
    return {"message": "The service is up and running :)"}