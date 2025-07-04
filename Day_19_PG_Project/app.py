from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse

app = FastAPI()
import random

@app.get('/')
def home():
    return {'message' : 'Hello Welcome to Prometheus and grafana project intergated with kbs'}

total_requests = 0

@app.get("/metrics")
def metrics():
    global total_requests
    total_requests += 1

    # Simulated values
    request_processing_latency = round(random.uniform(0.1, 1.5), 3)  # Latency in seconds
    model_prediction_success_rate = round(random.uniform(80, 100), 2)  # Success rate in %

    metrics_json = {
        "total_api_requests_total": total_requests ,
        "request_processing_latency_seconds": request_processing_latency,
        "model_prediction_success_rate": model_prediction_success_rate
    }

    return JSONResponse(content=metrics_json, status_code=200)

if __name__ == '__main__':
    uvicorn.run(host='0.0.0.0',app=app,port=5000)
