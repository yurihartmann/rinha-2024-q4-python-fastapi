from typing import Literal

from pydantic import BaseModel, Field


class AddTransaction(BaseModel):
    valor: int
    tipo: Literal["c", "d"]
    descricao: str = Field(min_length=1, max_length=10)


class AddTransactionResponse(BaseModel):
    limite: int
    saldo: int
