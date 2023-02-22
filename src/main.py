from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas

app = _fastapi.FastAPI()

_services.create_database()

@app.post("/category/",response_model=_schemas.Category)
def create_category(
    category: _schemas.CategoryCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    db_category = _services.get_category_by_name(db=db, name=category.name)
    if db_category:
        raise _fastapi.HTTPException(
            status_code=400, detail="Category already exists in database!"
        )
    return _services.create_category(db=db, category=category)

@app.get("/category/", response_model=List[_schemas.Category])
def read_categories(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    categories = _services.get_categories(db=db)
    return categories

@app.post("/products/",response_model=_schemas.Product)
def create_product(
    product: _schemas.ProductCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    db_product = _services.get_product_by_name(db=db, name=product.name)
    if db_product:
        raise _fastapi.HTTPException(
            status_code=400, detail="Product already exists in database!"
        )

    db_category = _services.get_category_by_name(db=db, name=product.category)
    if db_category is None:
        raise _fastapi.HTTPException(
            status_code=400, detail="Category does not exist in database!"
        )
    return _services.create_product(db=db, product=product)

@app.get("/product/", response_model=List[_schemas.Product])
def read_product(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    products = _services.get_products(db=db)
    return products

@app.get("/product/{id}", response_model=_schemas.Product)
def read_product(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    product = _services.get_product(db=db, product_id=id)
    if product is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="Sorry no product exists for this id"
        )

    return product


@app.delete("/product/{id}")
def delete_product(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_product(db=db, product_id=id)
    return {"message": f"Successfully deleted product with id: {id}!"}


@app.patch("/product/{id}")
def patch_product(
    id: int,
    product: _schemas.ProductUpdate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    _services.update_product(db=db, product=product, product_id=id)
    return  {"message": f"Successfully updated product with id: {id}!"}
