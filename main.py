from fastapi import FastAPI


app = FastAPI(title="Fonoma - Backend Developer Test", version="1.0.0")


@app.get("/")
async def root():
    return "Welcome, Thanks for use Fonoma - Backend Developer Test"

