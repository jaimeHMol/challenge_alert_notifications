from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import ConfigDict, EmailStr
from sqlmodel import AutoString, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from alert_notifications_api.models.notification_preference import \
        NotificationPreference


class Customer(SQLModel, table=True):
    """ Represents the customers (person or company) of the application with their
    attributes. """
    # class Config:
    #     validate_assignment = True
    model_config = ConfigDict(validate_assignment=True) # type: ignore

    customer_id: int = Field(primary_key=True)
    name: str
    email: EmailStr = Field(sa_type=AutoString)
    cellphone: int
    created_on: datetime = Field(default_factory=datetime.now)
    created_by: str
    
    # notification_property: "NotificationPreference" = Relationship(back_populates="customer")
