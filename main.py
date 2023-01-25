#################################################
# BLOCK WITH API ROUTES                         #
#################################################
# create instance of the app
import uvicorn
from fastapi import FastAPI, APIRouter

app = FastAPI(title='luchanos-oxford-university')
user_router = APIRouter()

# create the instance of the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(user_router, prefix='/user', tags=["user"])
app.include_router(main_api_router)


if __name__ == '__main__':
    # run uvicorn server on host & port
    uvicorn.run(app, host="0.0.0.0", port=8000)
