from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic import EmailStr
from sqlmodel import AutoString, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from alert_notifications_api.models.notification_preference import \
        NotificationPreference


class Customer(SQLModel, table=True):
    """ Represents the customers (person or company) of the application with their
    attributes. """
    customer_id: int = Field(primary_key=True)
    name: str
    email: Optional[EmailStr] = Field(sa_type=AutoString)
    cellphone: Optional[int]
    created_on: datetime = Field(default_factory=datetime.now)
    created_by: str
    
    # notification_property: "NotificationPreference" = Relationship(back_populates="customer")
