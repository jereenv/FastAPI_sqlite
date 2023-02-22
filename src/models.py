import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import database as _database



class Category(_database.Base):
    __tablename__ = "categories"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, unique=True, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)


class Product(_database.Base):
    __tablename__ = "products"
    id = _sql.Column(_sql.Integer, primary_key = True,index = True)
    category = _sql.Column(_sql.String, _sql.ForeignKey("categories.name"))
    name = _sql.Column(_sql.String, unique=True, index=True)
    sku = _sql.Column(_sql.String, unique=True, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    status = _sql.Column(_sql.String, index=True)
