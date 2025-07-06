from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "¡Hola mundo desde FastAPI con Docker y Nginx!"}