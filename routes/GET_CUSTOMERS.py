from fastapi import HTTPException
from pydantic import BaseModel
from typing import List
from app import app

class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str
    company: str
    position: str

@app.get("/GET_CUSTOMERS", response_model=List[Customer])
def get_customers():
    try:
        customers = [
            {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com",
                "phone": "555-1234",
                "address": "123 Main St, Anytown, USA",
                "company": "Doe Enterprises",
                "position": "CEO"
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "email": "jane.smith@example.com",
                "phone": "555-5678",
                "address": "456 Oak St, Anytown, USA",
                "company": "Smith Consulting",
                "position": "Consultant"
            }
        ]
        return customers
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving customers")