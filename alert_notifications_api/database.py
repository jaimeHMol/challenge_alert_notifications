from sqlmodel import SQLModel, create_engine

# Required to make sur that the create_all method includes the desired models
from alert_notifications_api.models import (customer, notification_preference,
                                            offer)

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def drop_db() -> None:
    engine.dispose()
    SQLModel.metadata.drop_all(engine)