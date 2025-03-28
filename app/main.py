from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api import router as api_router
from src.admin.config import create_admin

# create FastAPI app
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
    StaticFiles(directory="./images"),
    name="images"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены (для разработки)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

# connect admin panel to app
admin = create_admin(app)

# include routers
app.include_router(api_router)

#redirect to docs from main page
@app.get("/")
def read_root():
    """main page redirect to docs"""
    return RedirectResponse(url="/docs")

# run the app with uvicorn server
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
