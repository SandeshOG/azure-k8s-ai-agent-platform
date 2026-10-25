# Azure Kubernetes AI Agent Platform

**Author:** Sandesh Lanjewar  
**GitHub:** https://github.com/SandeshOG

A production-oriented platform that deploys and orchestrates AI agents on Kubernetes with Azure integration, automation, and observability.

## What this project demonstrates
- **Kubernetes** — Deployments, Services, ConfigMaps, probes, resource limits
- **Python** — FastAPI-based AI agent service
- **Azure** — Ready for AKS, Azure Monitor, Azure OpenAI / AI Foundry patterns
- **AI Agents** — Simple agent endpoint that can be extended with Semantic Kernel / LangChain
- **Automation** — Deployment scripts and operational best practices
- **Observability** — Health checks + Prometheus-style metrics

## Architecture
```
Client → Service → AI Agent Pod (FastAPI)
                     ↓
               Azure OpenAI / Monitor (extensible)
```

## Quick Start

### Local
```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```

### Kubernetes
```bash
kubectl apply -f k8s/
```

## Why this fits Cloud / Platform Engineer roles
- Hands-on Kubernetes + container orchestration
- AI agent systems (preferred qualification at Cisco)
- Azure cloud patterns
- Automation and operational readiness
- Clean, documented, interview-ready project

---
Built by **Sandesh Lanjewar** as a portfolio project for cloud platform and AI engineering roles.