from fastapi import FastAPI
from database import Base, engine
from routers import favorites

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bakery Backend with Favorites")


app.include_router(favorites.router)


