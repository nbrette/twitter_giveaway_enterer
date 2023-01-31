from controllers.firestore_controller import FirestoreController
import uvicorn
from fastapi import APIRouter, FastAPI
from services.router import enterer 


api_router = APIRouter()
api_router.include_router(enterer.router)

app = FastAPI()
app.include_router(api_router, prefix='/api/rest')

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)