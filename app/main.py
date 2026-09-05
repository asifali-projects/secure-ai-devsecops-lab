from fastapi import FastAPI

app = FastAPI(
    title="Secure AI DevSecOps Lab",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "secure-ai-api",
    }


@app.get("/")
def root():
    return {
        "message": "Secure AI DevSecOps Lab"
    }