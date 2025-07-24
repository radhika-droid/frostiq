# Frostiq BakeryBackend

## Overview
Frostiq's BakeryBackend is a FastAPI-based backend service for managing user favorites in a bakery application. It supports adding, listing, and deleting favorite items for users, with robust validation and access control.

## Features
- Add, list, and delete user favorites
- Duplicate detection to prevent redundant entries
- Input validation for item names
- Resource-level authorization for deletion
- SQLite database (file always stored in `BakeryBackend/`)
- Ready for unit/integration testing with pytest

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd frostiq
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   uvicorn BakeryBackend.main:app --reload
   ```
   The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Running Tests
1. **Ensure pytest is installed:**
   ```bash
   pip install pytest
   ```
2. **Run the tests:**
   ```bash
   pytest BakeryBackend/routers/test_favorites.py
   ```

## Project Structure
```
frostiq/
├── BakeryBackend/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routers/
│   │   ├── favorites.py
│   │   └── test_favorites.py
│   ├── schemas.py
│   └── favorites.db
├── requirements.txt
└── README.md
```

## API Endpoints
- `POST /favorites/` — Add a favorite
- `GET /favorites/{user_id}` — List favorites for a user
- `DELETE /favorites/{favorite_id}?user_id=...` — Delete a favorite (only by owner)

## Notes
- The database file is always created in the `BakeryBackend` directory for consistency.
- The codebase is structured for easy extension and testing.

---

Made with ❤️ 