from datetime import datetime
from typing import Literal

from sqlmodel import SQLModel, Field, Relationship


class Cliente(SQLModel):
    __tablename__ = "clientes"

    id: int = Field(primary_key=True)
    limite: int
    saldo_inicial: int

    transacoes: list["Transactions"] = Relationship(back_populates="cliente")


class Transacao(SQLModel):
    __tablename__ = "transacoes"

    id_client: int = Field(foreign_key="clientes.id")
    valor: int
    tipo: Literal["c", "d"]
    descricao: str
    realizada_em: datetime = Field(default_factory=datetime.now)

    cliente: Cliente = Relationship(back_populates="transacoes")
