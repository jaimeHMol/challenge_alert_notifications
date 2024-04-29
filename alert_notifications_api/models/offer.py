from datetime import datetime

from sqlmodel import Field, SQLModel


class Offer(SQLModel, table=True):
    """ Represents the offers that will be send to all the customers. """
    offer_id: int = Field(primary_key=True)
    message: str
    sended: bool
    created_on: datetime = Field(default_factory=datetime.now)
    created_by: str
