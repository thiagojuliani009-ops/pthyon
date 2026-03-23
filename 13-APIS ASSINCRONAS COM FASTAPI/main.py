from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World", "status": "Rodando!"}

@app.get("/foobar")
def foobar():
    return {"foo": "bar", "hello": "world"}

