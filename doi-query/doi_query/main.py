
import uvicorn
from fastapi import FastAPI, Depends

app = FastAPI()


@app.get("/")
async def hello_world( name: str ) -> str:
    """
    Image CDN Address: https://assets.clubing.stick.us
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
