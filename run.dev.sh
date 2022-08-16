cp .env.dev .env
nohup python3 -m uvicorn src.main:app > catalina.out  2>&1 &