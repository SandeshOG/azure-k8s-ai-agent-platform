"""
Azure Kubernetes AI Agent Platform
Author: Sandesh Lanjewar
"""
from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(
    title="AI Agent Platform",
    description="Kubernetes-native AI agent service by Sandesh Lanjewar",
    version="1.0.0"
)

class AgentRequest(BaseModel):
    query: str
    context: str | None = None

class AgentResponse(BaseModel):
    response: str
    agent: str = "platform-agent"
    author: str = "Sandesh Lanjewar"
    latency_ms: float

@app.get("/health")
def health():
    return {"status": "healthy", "service": "ai-agent-platform", "author": "Sandesh Lanjewar"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.post("/agent", response_model=AgentResponse)
def run_agent(request: AgentRequest):
    start = time.time()
    
    # Simulated AI agent reasoning (extend with Azure OpenAI / Semantic Kernel)
    simulated_response = f"Processed query: '{request.query}'. This is a Kubernetes-hosted AI agent."
    if request.context:
        simulated_response += f" Context considered: {request.context[:50]}..."
    
    latency = (time.time() - start) * 1000
    return AgentResponse(
        response=simulated_response,
        latency_ms=round(latency, 2)
    )

@app.get("/")
def root():
    return {
        "message": "Azure Kubernetes AI Agent Platform",
        "author": "Sandesh Lanjewar",
        "docs": "/docs",
        "agent_endpoint": "/agent"
    }