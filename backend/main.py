"""Backend API entry point."""

from fastapi import FastAPI


app = FastAPI(title="Forest Inventory API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
