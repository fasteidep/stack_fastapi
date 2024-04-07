from fastapi import FastAPI

app = FastAPI()
stack = []

# Обработчик для добавления элемента в стек
@app.post("/push/{item}")
def push_item(item: str):
    stack.append(item)
    return {"message": f"Item '{item}' has been pushed to the stack"}

# Обработчик для извлечения элемента из стека
@app.get("/pop")
def pop_item():
    if not stack:
        return {"message": "Stack is empty"}
    item = stack.pop()
    return {"popped_item": item}

# Обработчик для просмотра текущего состояния стека
@app.get("/stack")
def view_stack():
    return {"stack": stack}

