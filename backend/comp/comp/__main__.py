import os
import uvicorn

from .api import app

uvicorn.run(
    "comp.api:app",
    host="0.0.0.0",
    port=int(os.environ.get("API_PORT", 8004)),
    reload=True,
)
