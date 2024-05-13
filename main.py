from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()


class CreateUser(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    password: str


class Calculation(BaseModel):
    a: int
    b: int
    calc: str


@app.post('/calc/add/')
def calc_add(calculation: Calculation):
    a = calculation.a
    b = calculation.b
    calc = calculation.calc

    if calc == '+':
        result = a + b
    elif calc == '-':
        result = a - b
    elif calc == '*':
        result = a * b
    elif calc == '/':
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {
        "message": "Calculation performed successfully",
        'a': a,
        'b': b,
        'result': result
    }


@app.get("/")
def hello_index():
    return {
        "message": "Hello World!",
    }


@app.get('/hello/')
def say_hello(name: str):
    name = name.strip().title()
    return {"message": f"Hello Dear {name} "}


@app.post('/users/')
def create_user(user: CreateUser):
    return {
        "message": "User Created",
        "username": user.username,
        "full_name": user.full_name,
        "email": user.email,
        "password": user.password
    }


@app.get("/items/")
def items():
    return [
        'item1',
        'item2',
        'item3',
        'item4',
        'item5',
    ]


@app.get('/items/latest/')
def get_latest():
    return {'items': {'id': 0, 'name': 'latest'}}


@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {
        "item": {
            'id': item_id,
        }
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
