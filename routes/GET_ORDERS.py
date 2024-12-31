from app import app

@app.get("/GET_ORDERS")
def get_orders():
    orders = [
        {
            "id": 1,
            "customer_id": 1,
            "product_id": 1,
            "quantity": 1,
            "total_price": 999.99,
            "status": "Shipped"
        },
        {
            "id": 2,
            "customer_id": 2,
            "product_id": 2,
            "quantity": 2,
            "total_price": 1399.98,
            "status": "Processing"
        }
    ]
    return orders