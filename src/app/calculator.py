def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def mul(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b