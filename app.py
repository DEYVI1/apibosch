import pandas as pd
import fastapi
from fastapi.responses import StreamingResponse  # Add to Top

app = fastapi.FastAPI()

@app.get("/csv")
async def get_csv():
    df = pd.read_csv("data/data.csv")
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=data.csv"},
    )