from datetime import datetime

from sqlmodel import Field, SQLModel


class Customer(SQLModel):
    """ Represents the customers (person or company) of the application with their
    attributes. """
    customer_id: int = Field(default=None, primary_key=True)
    name: str
    created_on: datetime = Field(default_factory=datetime.now)
    created_by: str
