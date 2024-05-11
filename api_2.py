from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class ID(BaseModel):
    id: int


organization = {
    1: "Colllance",
    2: "CCMG"
}


@app.post("/getOrganization")
async def get_company_name(id: ID) -> Dict:
    organization_name = organization.get(id.id, "Organization not found")
    return {"data": organization_name}


if __name__ == "__main__":
    uvicorn.run(app)
