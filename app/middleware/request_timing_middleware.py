from fastapi import Request,FastAPI
from time import perf_counter
from app.api.routes.api_key import router as api_router
from app.api.routes.auth import router as auth_router
from app.api.routes.usage_tracker import router as usage_router

app = FastAPI()

async def request_details(request : Request,call_next):
    start = perf_counter()
    print("request recevied")
    response =await call_next(request)
    end= perf_counter()    
    process_time= end - start
    response.headers["Process-Time"] = str(process_time)
    print("response genrated")
    return response

