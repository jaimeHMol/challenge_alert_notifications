from typing import Optional

from pydantic import EmailStr
from sqlmodel import SQLModel


class NotificationDTO(SQLModel):
    """ Data Transfer Object with the attributes required to be used on the notification
    queue. """
    email: bool
    customer_email: EmailStr
    sms: bool
    customer_cellphone: int
    app_push: Optional[bool] = False
    dummy: Optional[bool] = False
    offer_message: str
