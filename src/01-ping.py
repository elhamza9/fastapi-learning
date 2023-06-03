from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping_pong():
    return {'message': 'pong'}
