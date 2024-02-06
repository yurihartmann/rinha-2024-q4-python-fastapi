from http import HTTPStatus

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from app.schemas.add_transaction import AddTransaction

app_routes = APIRouter()

@app_routes.get(
    path="/clientes/{id}/extrato"
)
async def get_extract(
    id: int
):
    return id

@app_routes.post(
    path="/clientes/{id}/transacoes"
)
async def create_transaction(
    id: int,
    add_transaction: AddTransaction
):
    return ORJSONResponse(content=add_transaction.model_dump(), status_code=HTTPStatus.OK)
