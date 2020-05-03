PORT=${1:-5000}
cd ../
uvicorn main:app --host 0.0.0.0 --reload --port $PORT 
cd getting-started/