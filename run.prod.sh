cp .env.prod .env
python3 -m uvicorn src.main:app --host 0.0.0.0