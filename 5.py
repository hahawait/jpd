from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class WebhookData(BaseModel):
    """Модель для вебхука"""
    function: str
    data: dict


def function_one(data):
    return {"message": "Function One executed", "data": data}


def function_two(data):
    return {"message": "Function Two executed", "data": data}


# Словарь для маршрутизации функций
function_map = {
    "function_one": function_one,
    "function_two": function_two,
}


@app.post("/Datalore")
async def handle_webhook(webhook_data: WebhookData):
    function_name = webhook_data.function
    data = webhook_data.data

    # Проверяем, существует ли функция в словаре
    if function_name in function_map:
        # Вызываем соответствующую функцию
        result = function_map[function_name](data)
        return result
    else:
        raise HTTPException(status_code=404, detail="Function not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app)
