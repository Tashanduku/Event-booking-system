import click
from models.db import SessionLocal, engine
from models.event import Event, Booking
from models.db import Base
from datetime import datetime


Base.metadata.create_all(bind=engine)

@click.group()
def cli():
    """Event Booking CLI"""
    pass

# Add Event
@click.command()
@click.option("--name", prompt="Event Name", help="Name of the event")
@click.option("--location", prompt="Location", help="Location of the event")
@click.option("--date", prompt="Date (YYYY-MM-DD)", help="Event date")
@click.option("--tickets", prompt="Available Tickets", type=int, help="Number of tickets")
def add_event(name, location, date, tickets):
    """Add a new event"""
    session = SessionLocal()
    try:
        event_date = datetime.strptime(date, "%Y-%m-%d").date()  
        event = Event(name=name, location=location, date=event_date, available_tickets=tickets)
        session.add(event)
        session.commit()
        click.echo(f" Event '{name}' added successfully!")
    except ValueError:
        click.echo(" Invalid date format! Use YYYY-MM-DD.")
    finally:
        session.close()

# List Events
@click.command()
def list_events():
    """List all events"""
    session = SessionLocal()
    events = session.query(Event).all()
    session.close()

    if not events:
        click.echo(" No events available.")
        return

    for event in events:
        click.echo(f" {event.id}: {event.name} - {event.location} on {event.date} ({event.available_tickets} tickets left)")

# Book a Ticket
@click.command()
@click.option("--event_id", prompt="Event ID", type=int, help="ID of the event to book")
@click.option("--user", prompt="Your Name", help="Your name for the booking")
def book_ticket(event_id, user):
    """Book a ticket for an event"""
    session = SessionLocal()
    event = session.query(Event).filter_by(id=event_id).first()

    if not event:
        click.echo(" Event not found.")
        session.close()
        return

    if event.available_tickets <= 0:
        click.echo(" No tickets available.")
        session.close()
        return

    booking = Booking(user_name=user, event_id=event.id)
    event.available_tickets -= 1
    session.add(booking)
    session.commit()
    click.echo(f" Ticket booked for {user} at '{event.name}'!")

    session.close()

# View Bookings
@click.command()
@click.option("--user", prompt="Your Name", help="Your name to view bookings")
def view_bookings(user):
    """View your bookings"""
    session = SessionLocal()
    bookings = session.query(Booking).filter_by(user_name=user).all()
    
    if not bookings:
        click.echo(f" No bookings found for {user}.")
    else:
        for booking in bookings:
            event = session.query(Event).filter_by(id=booking.event_id).first()
            click.echo(f" {event.name} - {event.location} on {event.date}")

    session.close()

# Cancelling Event
@click.command()
@click.option("--event_id", prompt="Event ID", type=int, help="ID of the event to cancel")
def cancel_event(event_id):
    """Cancel an event"""
    session = SessionLocal()
    event = session.query(Event).filter_by(id=event_id).first()

    if not event:
        click.echo(" Event not found.")
        session.close()
        return

   
    session.query(Booking).filter_by(event_id=event.id).delete()
    session.delete(event)
    session.commit()
    
    click.echo(f" Event ID {event_id} has been canceled.")
    session.close()


cli.add_command(add_event)
cli.add_command(list_events)
cli.add_command(book_ticket)
cli.add_command(view_bookings)
cli.add_command(cancel_event)

