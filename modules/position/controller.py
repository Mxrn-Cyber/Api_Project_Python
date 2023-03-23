from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from core.authentication import JWTBearer

from core.database import get_db
from modules.Position.entity import Position
from modules.Position.model import PositionInsertRequest, PositionUpdateRequest

router = APIRouter(
    prefix='/Position',
    tags=['Position']
)


@router.get('')
def gets(db: Session = Depends(get_db), auth_id: str = Depends(JWTBearer())):
    return db.query(Position).all()


@router.get('/{item_id}')
def get(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Position).filter(Position.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return item


@router.post('')
def create(item: PositionInsertRequest, db: Session = Depends(get_db), auth_id: str = Depends(JWTBearer())):
    db_item = Position(name=item.name)
    db.add(db_item)
    db.commit()
    return db_item


@router.put('/{item_id}')
def update(item_id: int, item: PositionUpdateRequest, db: Session = Depends(get_db)):
    old = db.query(Position).filter(Position.id == item_id).first()
    if old is None:
        raise HTTPException(status_code=404, detail='Item not found')
    old.name = item.name
    db.commit()
    return old


@router.delete('/{item_id}')
def delete(item_id: int, db: Session = Depends(get_db)):
    old = db.query(Position).filter(Position.id == item_id).first()
    if old is None:
        raise HTTPException(status_code=404, detail='Item not found')
    db.delete(item)
    db.commit()
    return item
