from .server import app
import uvicorn

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

main()

# Command to run server     python -m rag_queue.main  http://0.0.0.0:8000/docs