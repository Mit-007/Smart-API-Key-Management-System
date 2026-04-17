from fastapi import FastAPI 
from app.api.routes import auth,api_key,usage_tracker
from app.middleware.request_timing_middleware import request_details

app = FastAPI()

app.middleware("http")(request_details)

app.include_router(auth.router)
app.include_router(api_key.router)
app.include_router(usage_tracker.router)