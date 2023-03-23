from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from core.authentication import JWTBearer

from core.database import get_db
from modules.User.entity import User
from modules.User.model import UserInsertRequest, UserUpdateRequest

router = APIRouter(
    prefix='/User',
    tags=['User']
)


@router.get('')
def gets(db: Session = Depends(get_db), auth_id: str = Depends(JWTBearer())):
    return db.query(User).all()


@router.get('/{item_id}')
def get(item_id: int, db: Session = Depends(get_db)):
    item = db.query(User).filter(User.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return item


@router.post('')
def create(item: UserInsertRequest, db: Session = Depends(get_db), auth_id: str = Depends(JWTBearer())):
    db_item = User(name=item.name)
    db.add(db_item)
    db.commit()
    return db_item


@router.put('/{item_id}')
def update(item_id: int, item: UserUpdateRequest, db: Session = Depends(get_db)):
    old = db.query(User).filter(User.id == item_id).first()
    if old is None:
        raise HTTPException(status_code=404, detail='Item not found')
    old.name = item.name
    db.commit()
    return old


@router.delete('/{item_id}')
def delete(item_id: int, db: Session = Depends(get_db)):
    old = db.query(User).filter(User.id == item_id).first()
    if old is None:
        raise HTTPException(status_code=404, detail='Item not found')
    db.delete(item)
    db.commit()
    return item
