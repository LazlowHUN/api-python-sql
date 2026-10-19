# 🌦️ Robust Weather ETL Pipeline

A production-grade, fault-tolerant ETL (Extract, Transform, Load) pipeline built in Python that fetches live weather data from the OpenWeather API, validates it using Pydantic, and securely loads it into a containerized PostgreSQL database with strict idempotency guarantees.

Designed with a strong focus on software engineering best practices, network resilience, and testability.

---

## 🚀 Key Features

* **Resilient Network Layer**: Implements a custom `requests.Session` with a tailored `HTTPAdapter` and exponential backoff `Retry` strategy to gracefully handle transient network failures, rate limits, and server errors (5xx).
* **Data Validation & Integrity**: Leverages **Pydantic** models to strictly validate incoming JSON payloads, ensuring type safety and catching malformed API responses early.
* **Idempotent Database Logic**: Utilizes PostgreSQL `ON CONFLICT (city_id, dt) DO UPDATE` constraints. Designed to protect the immutable `created_at` timestamp while updating latest telemetry data.
* **Containerized Infrastructure**: Runs PostgreSQL in a Docker container via Docker Compose, ensuring a reproducible development and execution environment.
* **Comprehensive Testing**: Includes unit tests built with **pytest** covering data validation models and mocked API interactions (`unittest.mock`), ensuring high code reliability without hitting live external APIs.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Database**: PostgreSQL 15-alpine
* **Containerization**: Docker & Docker Compose
* **Libraries**: `requests`, `pydantic`, `pytest`, `psycopg2` / `sqlalchemy` (or your DB driver)

---

## 📁 Project Structure

```text
weather-etl-pipeline/
├── api_client.py      # WeatherApiClient with custom Session & Retry logic
├── models.py          # Pydantic data validation schemas
├── main.py            # Main pipeline orchestration script
├── requirements.txt   # Project dependencies
├── docker-compose.yml # PostgreSQL container configuration
├── tests/
│   ├── test_models.py # Unit tests for Pydantic models
│   └── test_api.py    # Unit tests with mocked API responses
└── .env.example       # Template for environment variables