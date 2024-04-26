from datetime import datetime

from sqlmodel import Field, SQLModel


class NotificationPreference(SQLModel):
    """ Represents the notification preferences defined per each customer (1 to 1) """
    notification_preference_id: int = Field(default=None, primary_key=True)
    customer_id: int
    mail: bool
    sms: bool
    app_push: bool
    created_on: datetime = Field(default_factory=datetime.now)
    created_by: str
