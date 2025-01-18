# chatbot-admin-api

### Start Virtual Environment:

source venv/bin/activate

### Start App:

uvicorn app.main:app --reload

### Test App:

PYTHONPATH=$(pwd) pytest

### Migrate Database

• alembic revision --autogenerate -m "message"
• alembic upgrade head
