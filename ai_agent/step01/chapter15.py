# step01/chapter15.py
from fastapi import FastAPI

app = FastAPI(title="메모 API")


@app.get("/")
def home():
    print("home 접속") # loging, 디버그용
    return {"message": "메모 API가 실행 중이다"}


@app.get("/hello/{name}")
def hello(name: str, times: int = 2):
    print("hello 접속") # loging, 디버그용
    return {"greeting": f"안녕, {name}! " * times}