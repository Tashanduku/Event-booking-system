import click
from models.db import SessionLocal, engine
from models.event import Event, Booking

from models.db import Base
Base.metadata.create_all(bind=engine)


@click.group()
def cli():
    """Event Booking CLI"""
    pass

if __name__ == "__main__":
    cli()
