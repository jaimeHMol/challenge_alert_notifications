from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from alert_notifications_api.models.customer import Customer


class NotificationPreference(SQLModel, table=True):
    """ Represents the notification preferences defined per each customer (1 to 1) """
    notification_preference_id: int = Field(primary_key=True)
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.customer_id")
    email: bool
    sms: bool
    app_push: Optional[bool] = None
    dummy: Optional[bool] = False
    created_on: datetime = Field(default_factory=datetime.now)
    created_by: str

    # customer: "Customer" = Relationship(back_populates="notification_property")
