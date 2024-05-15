from datetime import datetime

from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class Offer(SQLModel, table=True):
    """ Represents the offers that will be send to all the customers. """
    # class Config:
    #     validate_assignment = True
    model_config = ConfigDict(validate_assignment=True) # type: ignore

    offer_id: int = Field(primary_key=True)
    message: str
    sended: bool
    created_on: datetime = Field(default_factory=datetime.now)
    created_by: str
