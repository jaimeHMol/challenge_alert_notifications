from datetime import datetime

from pydantic import BaseModel, Field


class Offer(BaseModel):
    """ Represents the offers that will be send to all the customers. """
    offer_id: int
    message: str
    sended: bool
    created_on: datetime = Field(default_factory=datetime.now)
    created_by: str