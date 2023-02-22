import sqlalchemy.orm as _orm

import models as _models, schemas as _schemas, database as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_category_by_name(db: _orm.Session, name: str):
    return db.query(_models.Category).filter(_models.Category.name == name).first()


def create_category(db: _orm.Session, category: _schemas.CategoryCreate):

    db_category = _models.Category(name = category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: _orm.Session):
    return db.query(_models.Category).all()



def get_product_by_name(db: _orm.Session, name: str):
    return db.query(_models.Product).filter(_models.Product.name == name).first()


def create_product(db: _orm.Session, product: _schemas.ProductCreate):

    db_product = _models.Product(category = product.category, name = product.name, sku = product.sku, status = product.status)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: _orm.Session):
    return db.query(_models.Product).all()

def get_product(db: _orm.Session, product_id: int):
    return db.query(_models.Product).filter(_models.Product.id == product_id).first()

def delete_product(db: _orm.Session, product_id: int):
    db.query(_models.Product).filter(_models.Product.id == product_id).delete()
    db.commit()



def update_product(db: _orm.Session, product_id: int, product: _schemas.ProductUpdate):
    db_product = get_product(db=db, product_id=product_id)
    product_data = product.dict(exclude_unset=True)
    for key, value in product_data.items():
        setattr(db_product,key,value)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
