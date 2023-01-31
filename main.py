#################################################
# BLOCK WITH API ROUTES                         #
#################################################
# create instance of the app
import uvicorn
from fastapi import FastAPI, APIRouter

from api.handlers import user_router
from db.models import Base
from db.session import engine

app = FastAPI(title='luchanos-oxford-university')

# create the instance of the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(user_router, prefix='/user', tags=["user"])
app.include_router(main_api_router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    # run uvicorn server on host & port
    uvicorn.run(app, host="0.0.0.0", port=8000)
