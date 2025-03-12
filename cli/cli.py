import click
from models.db import SessionLocal, engine
from models.event import Event, Booking

from models.db import Base
Base.metadata.create_all(bind=engine)


@click.group()
def cli():
    """Event Booking CLI"""
    pass

@click.command()
@click.option("--name", prompt="Event Name", help="Name of the event")
@click.option("--location", prompt="Location", help="Location of the event")
@click.option("--date", prompt="Date (YYYY-MM-DD)", help="Event date")
@click.option("--tickets", prompt="Available Tickets", type=int, help="Number of tickets")
def add_event(name, location, date, tickets):
    """Add a new event"""
    session = SessionLocal()
    event = Event(name=name, location=location, date=date, available_tickets=tickets)
    session.add(event)
    session.commit()
    session.close()
    click.echo(f"Event '{name}' added successfully!")
