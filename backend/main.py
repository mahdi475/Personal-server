from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Mahdi's Personal Server API is running!"}
