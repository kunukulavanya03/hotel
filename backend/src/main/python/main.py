from fastapi import FastAPI
from sqlalchemy import create_engine
from src.main.python.models import User, Hotel, Room, Booking

app = FastAPI()

engine = create_engine('postgresql://postgres:postgres@localhost:5432/hotel_booking')

@app.get('/users')
def get_users():
    # Retrieve a list of all users
    users = session.query(User).all()
    return users

@app.post('/users')
def create_user(user: User):
    # Create a new user
    session.add(user)
    session.commit()
    return user

@app.get('/hotels')
def get_hotels():
    # Retrieve a list of all hotels
    hotels = session.query(Hotel).all()
    return hotels

@app.post('/hotels')
def create_hotel(hotel: Hotel):
    # Create a new hotel
    session.add(hotel)
    session.commit()
    return hotel

@app.get('/hotels/{hotel_id}/rooms')
def get_rooms(hotel_id: int):
    # Retrieve a list of all rooms for a hotel
    rooms = session.query(Room).filter(Room.hotel_id == hotel_id).all()
    return rooms

@app.post('/hotels/{hotel_id}/rooms')
def create_room(hotel_id: int, room: Room):
    # Create a new room for a hotel
    room.hotel_id = hotel_id
    session.add(room)
    session.commit()
    return room

@app.get('/rooms/{room_id}/bookings')
def get_bookings(room_id: int):
    # Retrieve a list of all bookings for a room
    bookings = session.query(Booking).filter(Booking.room_id == room_id).all()
    return bookings

@app.post('/rooms/{room_id}/bookings')
def create_booking(room_id: int, booking: Booking):
    # Create a new booking for a room
    booking.room_id = room_id
    session.add(booking)
    session.commit()
    return booking
