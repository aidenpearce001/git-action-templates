from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from routers import sql_injection

app = FastAPI(title="Dashboard API", version="0.1.0", description="Dashboard API")

origins = [
    "http://localhost",
    "http://localhost:9000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")


app.include_router(sql_injection.app, prefix="/sql_injection", tags=["SQL Injection"])

def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# def calculate_factorial(n):
#     if n < 0:
#         raise ValueError("Input must be non-negative")
#     result = 1
#     for i in range(1, n + 1):
#         old_result = result
#         result *= i
#         if result // i != old_result:
#             raise OverflowError("Integer overflow")
#     return result

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    

# def fibonacci(n):
#     if n <= 0:
#         raise ValueError("Input must be positive")
#     fib = [0, 1]
#     for i in range(2, n):
#         fib.append(fib[i-1] + fib[i-2])
#     return fib[:n]
