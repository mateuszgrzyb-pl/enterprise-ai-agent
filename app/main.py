from fastapi import FastAPI
from app.api.v1.health import router as health_router

app = FastAPI(
    title="Enterprise AI Agent",
    description="Enterprise-grade AI banking assistant",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Hello from Banking AI Agent!"}

# Include API routes
app.include_router(health_router, prefix="/api/v1")
