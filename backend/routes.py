from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from backend.database import get_db, engine, wait_for_db
from backend.models import Item, Base

router = APIRouter()

# Pydantic model for requests
class ItemRequest(BaseModel):
    name: str
    description: str

@router.on_event("startup")
async def startup():
    await wait_for_db()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@router.get("/")
def home():
    return {"message": "Welcome to the CRUD API!"}

@router.post("/items/")
async def create_item(item: ItemRequest, db: AsyncSession = Depends(get_db)):
    new_item = Item(name=item.name, description=item.description)
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item

@router.get("/items/")
async def read_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item))
    return result.scalars().all()

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).where(Item.id == item_id))
    item_obj = result.scalars().first()
    
    if not item_obj:
        raise HTTPException(status_code=404, detail="Item not found")

    item_obj.name = item.name
    item_obj.description = item.description
    await db.commit()
    return item_obj

@router.delete("/items/{item_id}")
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).where(Item.id == item_id))
    item_obj = result.scalars().first()

    if not item_obj:
        raise HTTPException(status_code=404, detail="Item not found")

    await db.delete(item_obj)
    await db.commit()
    return {"message": "Item deleted successfully"}
