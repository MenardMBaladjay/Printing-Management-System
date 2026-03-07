import enum
from sqlalchemy import Column, Integer, String, Float, Enum
from .database import Base


class PrintType(str, enum.Enum):
    bw = "bw"
    color = "color"
    photo_paper = "photo_paper"


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String, index=True)
    document_name = Column(String)
    pages = Column(Integer)
    print_type = Column(Enum(PrintType))
    total_cost = Column(Float)
