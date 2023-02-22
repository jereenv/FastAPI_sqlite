from typing import List, Optional
import datetime as _dt
import pydantic as _pydantic


class _ProductBase(_pydantic.BaseModel):
    category: str
    name: str
    sku: str
    status: str

class ProductCreate(_ProductBase):
    pass

class ProductUpdate(_ProductBase):
    category: Optional[str] = None
    name: Optional[str]
    sku: Optional[str]
    status: Optional[str]

class Product(_ProductBase):
    id :int
    date_created: _dt.datetime
    date_updated: _dt.datetime
    

    class Config:
        orm_mode = True

class _CategoryBase(_pydantic.BaseModel):
    name: str

class CategoryCreate(_CategoryBase):
    pass

class Category(_CategoryBase):
    id : int
    date_created: _dt.datetime
    date_updated: _dt.datetime

    class Config:
        orm_mode = True