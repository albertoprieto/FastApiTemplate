from app import app

@app.get("/GET_PRODUCTS")
def get_products():
    products = [
        {
            "id": 1,
            "name": "Laptop",
            "description": "A high performance laptop",
            "price": 999.99,
            "stock": 10
        },
        {
            "id": 2,
            "name": "Smartphone",
            "description": "A latest model smartphone",
            "price": 699.99,
            "stock": 25
        }
    ]
    return products