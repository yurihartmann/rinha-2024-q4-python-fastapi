from datetime import datetime
from http import HTTPStatus
from typing import Literal

from pydantic import BaseModel, Field, NonNegativeInt
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select, desc

from app.database import get_session
from app.models import Transacao, Cliente, TipoTransacao

app_routes = APIRouter()


@app_routes.get(
    path="/clientes/{id_cliente}/extrato"
)
async def get_extract(
    id_cliente: int,
    session: Session = Depends(get_session)
):
    cliente: Cliente | None = session.exec(select(Cliente).where(Cliente.id == id_cliente)).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não existe")

    ultimas_transacoes = session.exec(
        select(Transacao)
        .where(Transacao.id_client == id_cliente)
        .order_by(desc(Transacao.realizada_em))
        .limit(10)
    ).all()

    return ORJSONResponse(
        content={
          "saldo": {
            "total": cliente.saldo,
            "data_extrato": datetime.now().isoformat(),
            "limite": cliente.limite
          },
          "ultimas_transacoes": [
            transacao.model_dump(include={'valor', 'tipo', 'descricao', 'realizada_em'})
            for transacao in ultimas_transacoes
          ]
        },
        status_code=HTTPStatus.OK
    )


class AddTransaction(BaseModel):
    valor: NonNegativeInt
    tipo: Literal["c", "d"]
    descricao: str = Field(min_length=1, max_length=10)


@app_routes.post(
    path="/clientes/{id_cliente}/transacoes"
)
async def create_transaction(
    id_cliente: int,
    add_transaction: AddTransaction,
    session: Session = Depends(get_session)
):
    cliente: Cliente | None = session.exec(select(Cliente).where(Cliente.id == id_cliente).with_for_update()).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não existe")

    nova_transacao = Transacao(
        id_client=id_cliente,
        valor=add_transaction.valor,
        tipo=add_transaction.tipo,
        descricao=add_transaction.descricao,
    )

    if add_transaction.tipo == TipoTransacao.DEBITO.value:
        cliente.saldo -= add_transaction.valor

        if cliente.saldo < -cliente.limite:
            raise HTTPException(status_code=422, detail="Saldo insuficiente")

    elif add_transaction.tipo == TipoTransacao.CREDITO.value:
        cliente.saldo += add_transaction.valor

    session.add(nova_transacao)
    session.add(cliente)
    session.commit()

    return ORJSONResponse(
        content={
            "limite": cliente.limite,
            "saldo": cliente.saldo,
        },
        status_code=HTTPStatus.OK
    )
