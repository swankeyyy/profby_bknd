from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title="prof.by",
    description="backend for prof.by",
    version="0.0.1",
    contact={
        "name": "Ivan Levchuk",
        "email": "swankyyy1@gmail.com",
    },
)




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)