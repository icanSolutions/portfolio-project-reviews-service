# Reviews Service

The **Reviews Service** is a microservice responsible for managing user reviews associated with products.  
It is part of a larger system of services designed to demonstrate a full CI/CD pipeline for a containerized application.

---

## Overview

This service provides:
- CRUD operations for product reviews.
- RESTful API endpoints for integration with other services (e.g., Products Service).
- Persistence in a dedicated PostgreSQL database.
- Containerized deployment with Docker.

---

## Architecture

- **Language/Framework**: Python (Flask)
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Orchestration**: Docker Compose (multi-service setup with other components)

Each service runs in its own container and communicates over a dedicated Docker network.

---

## Endpoints (examples)

| Method | Endpoint                | Description                  |
|--------|--------------------------|------------------------------|
| GET    | `/reviews`              | Fetch all reviews            |
| GET    | `/reviews/{id}`         | Fetch a single review        |
| POST   | `/reviews`              | Create a new review          |
| PUT    | `/reviews/{id}`         | Update an existing review    |
| DELETE | `/reviews/{id}`         | Delete a review              |

---

## Deployment

This service is deployed via CI/CD pipelines that:
1. Run automated tests.
2. Build and tag a Docker image.
3. Push the image to a container registry.
4. Deploy it to the target environment (staging/production).

---

## Related Services

- **Products Service** – manages product information consumed by this service.
- **Gateway/API Layer** – aggregates and exposes endpoints to external clients.
- **Database Service** – PostgreSQL container for persistence.

---

## Status

This repository is part of a **CI/CD learning exercise** showcasing:
- Multi-service architecture
- Automated pipelines
- Isolated service development
