import uuid
from datetime import datetime
from enum import Enum
from sqlmodel import SQLModel, Field


class TipoTransacao(Enum):
    CREDITO = "c"
    DEBITO = "d"


class Cliente(SQLModel, table=True):
    __tablename__ = "clientes"

    id: int = Field(primary_key=True)
    nome: str
    limite: int
    saldo: int


class Transacao(SQLModel, table=True):
    __tablename__ = "transacoes"

    uuid: str = Field(primary_key=True, default_factory=uuid.uuid4)
    id_client: int = Field()
    valor: int
    tipo: str
    descricao: str
    realizada_em: datetime = Field(default_factory=datetime.now)
