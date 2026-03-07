from __future__ import annotations
from enum import Enum as PyEnum
from pydantic import BaseModel, Field


class PrintType(str, PyEnum):
    bw = "bw"
    color = "color"
    photo_paper = "photo_paper"


class OrderBase(BaseModel):
    student_name: str
    document_name: str
    pages: int = Field(..., gt=0)
    print_type: PrintType


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    student_name: str | None = None
    document_name: str | None = None
    pages: int | None = Field(None, gt=0)
    print_type: PrintType | None = None


class Order(OrderBase):
    order_id: int
    total_cost: float

    class Config:
        orm_mode = True
