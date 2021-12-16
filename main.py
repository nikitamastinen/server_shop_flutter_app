import json
from fastapi import FastAPI

app = FastAPI()


@app.get('/search/')
async def search_products(query: str):
    query = query.lower()
    print(query)
    result = []
    with open('data.json') as products:
        response = json.load(products)
        for item in response:
            template: str = ''
            for i in item.keys():
                template += str(item[i])
            if template.__contains__(query):
                print(template)
                result.append(item)
        return result


@app.get(
    '/',
)
async def get_products(offset: int, count: int):
    with open('data.json') as products:
        response = json.load(products)
        return response[offset:min(offset + count, len(response))]
