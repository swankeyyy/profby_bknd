from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from api import router as api_router
from app.src.admin.config import create_admin

app = FastAPI(
    title="prof.by",
    description="backend for prof.by",
    version="0.0.1",
    contact={
        "name": "Ivan Levchuk",
        "email": "swankyyy1@gmail.com",
    },
)

# connect static
app.mount(
    "/images/",
    StaticFiles(directory="../images"),
    name="images"
)

# connect admin panel to app
admin = create_admin(app)

# include routers
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
