from src.main.python.models import User, Hotel, Room, Booking

# Create some seed data
user = User(username='john', password='password', email='john@example.com')
session.add(user)
session.commit()

hotel = Hotel(name='Hotel Example', address='123 Main St')
session.add(hotel)
session.commit()

room = Room(hotel_id=hotel.id, room_number='101', room_type='Single')
session.add(room)
session.commit()

booking = Booking(room_id=room.id, user_id=user.id, checkin_date=datetime.now(), checkout_date=datetime.now())
session.add(booking)
session.commit()
