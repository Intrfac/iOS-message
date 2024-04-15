from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
async def function(request: Request):
    print(await request.json())
