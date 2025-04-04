from fastapi import FastAPI
from routers.details import router as detail_router

from fastapi.middleware.cors import CORSMiddleware

import uvicorn


app = FastAPI()


app.include_router(detail_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)