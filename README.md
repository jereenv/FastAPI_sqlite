# FastAPI_sqlite
To get a hands on experience of using Fast Api and SQLite, I implemented the below database table and created endpoints to interact with it

Database tables 
        - Products
            id  (Primary Key)
            category (Foreign Key)
            name (String)
            sku (String)
            date_created (Datetime)
            date_updated (Datetime)
            status (String)
        
        - Category
            id (Primary Key)
            name (string)
            date_created
            date_updated



 Endpoints -- 
        POST - /products/
        GET - /products/
        GET - /products/{id}
        PATCH - /products/{id}
        DELETE - /products/{id}


_________________________

To run:
On command line, Run uvicorn main:app –reload



