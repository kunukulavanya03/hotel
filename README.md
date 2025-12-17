# hotel

Backend API for hotel

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign.git))

## Project Structure

```
hotel/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User registration and login
- Hotel management
- Room management
- Booking management

## API Endpoints

- `POST /api/register` - Register a new user
- `POST /api/login` - Login a user
- `GET /api/hotels` - Get all hotels
- `POST /api/hotels` - Create a new hotel
- `GET /api/hotels/{hotel_id}/rooms` - Get all rooms for a hotel
- `POST /api/hotels/{hotel_id}/rooms` - Create a new room for a hotel
- `GET /api/rooms/{room_id}/bookings` - Get all bookings for a room
- `POST /api/rooms/{room_id}/bookings` - Create a new booking for a room

## License

MIT
