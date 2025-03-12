from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from models.db import Base, SessionLocal

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    available_tickets = Column(Integer, default=0)

    bookings = relationship("Booking", back_populates="event", cascade="all, delete-orphan")

   
    def save(self):
        session = SessionLocal()
        session.add(self)
        session.commit()
        session.close()

    @classmethod
    def get_by_id(cls, event_id):
        session = SessionLocal()
        event = session.query(cls).filter_by(id=event_id).first()
        session.close()
        return event

    @classmethod
    def get_all(cls):
        session = SessionLocal()
        events = session.query(cls).all()
        session.close()
        return events

    def delete(self):
        session = SessionLocal()
        session.delete(self)
        session.commit()
        session.close()

    
    @property
    def has_tickets(self):
        return self.available_tickets > 0


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    event_id = Column(Integer, ForeignKey("events.id", ondelete="CASCADE"))

    event = relationship("Event", back_populates="bookings")

    def save(self):
        session = SessionLocal()
        session.add(self)
        session.commit()
        session.close()

    @classmethod
    def get_by_id(cls, booking_id):
        session = SessionLocal()
        booking = session.query(cls).filter_by(id=booking_id).first()
        session.close()
        return booking

    @classmethod
    def get_all(cls):
        session = SessionLocal()
        bookings = session.query(cls).all()
        session.close()
        return bookings

    def delete(self):
        session = SessionLocal()
        session.delete(self)
        session.commit()
        session.close()
