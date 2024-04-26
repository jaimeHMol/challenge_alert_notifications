from datetime import datetime

from pydantic import BaseModel, Field


class Customer(BaseModel):
    """ Represents the customers (person or company) of the application with their
    attributes. """
    customer_id: int
    name: str
    created_on: datetime = Field(default_factory=datetime.now)
    created_by: str