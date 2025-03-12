from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.db import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    date = Column(String, nullable=False)
    available_tickets = Column(Integer, default=0)

    bookings = relationship("Booking", back_populates="event")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"))

    event = relationship("Event", back_populates="bookings")
