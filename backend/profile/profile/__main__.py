import os
import uvicorn

from .api import app

uvicorn.run(
    "profile.api:app",
    host="0.0.0.0",
    port=int(os.environ.get("API_PORT", 8002)),
    reload=True,
)
