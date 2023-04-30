from fastapi import FastAPI

from routers.order import order

app = FastAPI(title="Fonoma - Backend Developer Test", version="1.0.0")

# Routers
app.include_router(order, tags=["order"], prefix="/api/order")


@app.get("/")
async def root():
    return "Welcome, Thanks for use Fonoma - Backend Developer Test"

