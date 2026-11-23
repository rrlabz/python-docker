from fastapi import FastAPI


app = FastAPI(title="Demo API")


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Welcome to the Demo API"}


@app.get("/healthcheck")
def healthcheck() -> dict[str, str]:
    return {"status": "healthy"}
