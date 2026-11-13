from fastapi import FastAPI
app = FastAPI()

@app.get("/welcome")
def welcome():
    return {
        "message": "Hello World!"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
