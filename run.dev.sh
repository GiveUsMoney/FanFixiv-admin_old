cp .env.dev .env
nohup python3 -m uvicorn src.main:app --host 0.0.0.0 > catalina.out  2>&1 &