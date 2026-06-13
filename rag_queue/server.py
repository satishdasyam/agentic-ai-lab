from fastapi import FastAPI, Query
from langchain_text_splitters import python
from .client.rq_client import queue
from .queues.worker import process_query


app = FastAPI()

# http://0.0.0.0:8000/docs
# python -m rag_queue.main
# run rq worker


@app.get("/")
def read_root():
    return {"status": "Server is running"}


@app.post("/chat")
def chat(
    query: str = Query(..., description="The chat query of user")
    
):
    job = queue.enqueue(process_query, user_query=query)

    return { "status": "queued", "job_id": job.id }

# {
#   "status": "queued",
#   "job_id": "0a3f3faa-217d-40f4-a60f-9eb2ff257ea2"
# }


@app.get("/job-status")
def get_result(
    job_id: str = Query(..., description="Job ID")
):
    job = queue.fetch_job(job_id=job_id)
    result = job.return_value()
    
    return { "result":  result}

    