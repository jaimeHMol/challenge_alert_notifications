from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select

from alert_notifications_api.database import engine
from alert_notifications_api.models.customer import Customer
from alert_notifications_api.models.notification_dto import NotificationDTO
from alert_notifications_api.models.notification_preference import \
    NotificationPreference
from alert_notifications_api.models.offer import Offer
from queue_tasks.main import queue_notification_task

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "Hello, this is a custom alert notification API. Go to the /docs address to see the full documentation."}


@app.get("/health")
async def status() -> dict:
    return {"message": "The service is up and running :)"}


@app.post("/customer", response_model=Customer)
async def create_customer(customer: Customer) -> Customer:
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)
    return customer


@app.post("/offer", response_model=Offer)
async def create_offer(offer: Offer) -> Offer:
    with Session(engine) as session:
        session.add(offer)
        session.commit()
        session.refresh(offer)
    return offer


@app.post("/preferences/{customer_id}", response_model=NotificationPreference)
async def create_notification_preference(
    customer_id: int,
    notification_preference: NotificationPreference
) -> NotificationPreference:
    notification_preference.customer_id = customer_id
    with Session(engine) as session:
        session.add(notification_preference)
        session.commit()
        session.refresh(notification_preference)
    return notification_preference


@app.get("/preferences/{customer_id}", response_model=NotificationPreference)
async def get_notification_preference(customer_id: int) -> NotificationPreference:
    with Session(engine) as session:
        statement = select(NotificationPreference).where(NotificationPreference.customer_id == customer_id)
        results = session.exec(statement)
        notification_preference = results.first()
        if not notification_preference:
            raise HTTPException(status_code=404, detail="Preferences for customer {customer_id} not found")
    return notification_preference


@app.post("/notifications")
async def schedule_notifications() -> dict:
    notification_queue = []

    with Session(engine) as session:
        statement = select(Offer).where(Offer.sended == False)
        offers = session.exec(statement)

        for offer in offers:
            statement = select(Customer, NotificationPreference).where(
                Customer.customer_id == NotificationPreference.customer_id
            )
            results = session.exec(statement)
            for customer, notification_preference in results:
                notification = NotificationDTO(
                    offer_message=offer.message,
                    email=notification_preference.email,
                    customer_email=customer.email,
                    sms=notification_preference.sms,
                    customer_cellphone=customer.cellphone,
                    )
                notification_queue.append(notification)
        
        response = queue_notification_task(notification_queue)

    return response



def queue_notification(result: Offer) -> None:
    return
