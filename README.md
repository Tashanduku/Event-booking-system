# Event Booking System

A command-line interface (CLI) application for managing events and bookings using Python, SQLAlchemy, and Click.

## Features

- Event Management: Create, list and delete events
- Booking Management: Book tickets for events, view bookings
- Interactive menu system for easy navigation
- Database migrations with Alembic

## Requirements

- Python
- SQLAlchemy
- Click
- Alembic

## Installation

1. Clone the repository:
```
git clone <repository-url>
cd event-booking-system
```

2. Create a virtual environment:
```
python -m venv env
```

3. Activate the virtual environment:
```
# On macOS/Linux
source env/bin/activate
```

4. Install the dependencies:
```
pip install -r requirements.txt
```

5. Apply database migrations:
```
alembic upgrade head
```

## Usage

### Interactive Mode

To start the application in interactive mode:

```
python main.py 
```

This will display a menu-driven interface for managing events and bookingd

#### Event Management

```
# Create a new event
python main.py add-event


# List all events
python main.py events-list

# cancel an event
python main.py cancel-event --id 1
```

#### Booking Management

```
# Create a new booking
python main.py book-ticket

# List all bookings
python main.py view-bookings

## Database

The application uses SQLite as the database, which is stored in the `database.db` file. The database is automatically created when you run the application for the first time.
```

## File struvture

event_booking_cli

|-- models\
|   |-- db.py      
|   |-- event.py   
|-- cli\
|   |-- cli.py      
|-- migrations  
|-- main.py         
|-- requirements.txt\
|-- README.md