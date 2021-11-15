from pydantic import BaseModel
from tracardi.domain.entity import Entity


class JupyterAuth(BaseModel):
    token: str
    url: str


class JupyterPayload(BaseModel):
    source: Entity
    notebook_path: str
    notebook_name: str
