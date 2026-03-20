from sqlalchemy.orm import Session
from . import models, schemas


RATES = {
    models.PrintType.bw: 2.00,
    models.PrintType.color: 5.00,
    models.PrintType.photo_paper: 20.00,
}


def calculate_cost(pages: int, print_type: models.PrintType) -> float:
    """Simple cost calculator based on print type and page count."""
    return pages * RATES.get(print_type, 0.0)


def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        student_name=order.student_name,
        document_name=order.document_name,
        pages=order.pages,
        print_type=order.print_type,
        total_cost=calculate_cost(order.pages, order.print_type),
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def update_order(db: Session, order_id: int, order: schemas.OrderUpdate):
    db_order = get_order(db, order_id)
    if not db_order:
        return None
    if order.student_name is not None:
        db_order.student_name = order.student_name
    if order.document_name is not None:
        db_order.document_name = order.document_name
    if order.pages is not None:
        db_order.pages = order.pages
    if order.print_type is not None:
        db_order.print_type = order.print_type
    db_order.total_cost = calculate_cost(db_order.pages, db_order.print_type)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int):
    db_order = get_order(db, order_id)
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order
