import asyncio
import fastapi


# Create fastapi application
app = fastapi.FastAPI()

@app.get("/")
async def root():
    await asyncio.sleep(0.1)
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
