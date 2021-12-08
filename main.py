import json
from typing import Optional

import uvicorn as uvicorn
from fastapi import FastAPI, Response, Request, APIRouter
from pydantic import BaseModel
from settings import settings

app = FastAPI()


@app.get(
    '/',
)
async def get_products(offset: int, count: int):
    with open('data.json') as products:
        response = json.load(products)
        print(response)
        return response


if __name__ == '__main__':
    uvicorn.run(
        '__main__:app',
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=True,
    )
