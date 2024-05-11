import uvicorn
from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()


@app.get("/getOrganizations")
def get_companies() -> Dict[str, List[str]]:
    return {"data": ["Collance", "CCMG"]}


if __name__ == "__main__":
    uvicorn.run(app)
