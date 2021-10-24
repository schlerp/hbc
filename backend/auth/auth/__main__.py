import os
import uvicorn

from .api import app

uvicorn.run(
    "auth.api:app",
    host="0.0.0.0",
    port=int(os.environ.get("API_PORT", 8001)),
    reload=True,
)
