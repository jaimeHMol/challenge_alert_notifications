from datetime import datetime

from pydantic import BaseModel, Field


class NotificationPreference(BaseModel):
    """ Represents the notification preferences defined per each customer (1 to 1) """
    notification_preference_id: int
    customer_id: int
    mail: bool
    sms: bool
    app_push: bool
    created_on: datetime = Field(default_factory=datetime.now)
    created_by: str