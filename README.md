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
api-python-sql/
├── client.py          # WeatherApiClient with custom Session & Retry logic
├── models.py          # Pydantic data validation schemas
├── transformer.py     # Data transformation and parsing logic
├── main.py            # Main pipeline orchestration script
├── schema.sql         # Database table definitions and constraints
├── requirements.txt   # Project dependencies
├── docker-compose.yml # PostgreSQL container configuration
├── tests/
│   ├── test_models.py # Unit tests for Pydantic models & transformers
│   └── test_client.py # Unit tests with mocked API responses
└── .env.example       # Template for environment variables
```

---

## ⚙️ Getting Started

### Prerequisites
* **Python 3.10** or higher installed on your machine.
* **Docker** and **Docker Compose** installed and running.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/weather-etl-pipeline.git
cd weather-etl-pipeline
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory based on the provided example:
```bash
cp .env.example .env
```

Open the `.env` file and fill in your credentials and API key:
```env
API_KEY="apikey12345"
CONN_STR="postgresql://user:pass@localhost:5432/database_name"
POSTGRES_USER="myuser"
POSTGRES_PASSWORD="mypassword"
POSTGRES_DB="mydb"
CONN_STR="postgresql://myuser:mypassword@postgres_db:5432/mydb"
```

### 3. Spin Up the Database
Start the PostgreSQL container using Docker Compose:
```bash
docker compose up -d
```

### 4. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 5. Run the Tests
Verify that all unit tests pass successfully:
```bash
python -m pytest
```

### 6. Run the ETL Pipeline
Execute the main script to fetch, validate, and store the weather data:
```bash
python main.py
```

---

## 🔍 How to Inspect the Database

You can verify that the data has been successfully stored either via the command line or using a graphical database client (such as pgAdmin, DBeaver, or DataGrip).

### Option 1: Via Console (Docker Exec)
You can directly query the database inside the running Docker container:

```bash
docker exec -it <container_name_or_id> psql -U postgres -d mydb
```

Once inside the `psql` prompt, run the following query:
```sql
SELECT * FROM weather_forecasts;
```
To exit the console, simply type `\q`.

### Option 2: Via GUI Client (pgAdmin / DBeaver)
Connect to the database using your preferred graphical tool with the following connection details:

* **Host:** `localhost`
* **Port:** `5433` (as configured in `docker-compose.yml`)
* **Database:** `mydb`
* **User:** `myuser`
* **Password:** `mypassword`

---

## 💡 Engineering Highlights

### Fault Tolerance & Retry Strategy
Instead of relying on basic, unprotected HTTP requests, the pipeline wraps communication in a robust session using `urllib3` retries:

```python
retries = Retry(
    total=5,
    backoff_factor=2,
    status_forcelist=[500, 502, 503, 504],
    raise_on_status=False
)
adapter = HTTPAdapter(max_retries=retries)
session.mount('https://', adapter)
```

### Idempotency & Immutable Timestamps
The database schema and **UPSERT** logic ensure data integrity. Running the pipeline multiple times will update current metrics safely while preserving the exact moment a record was first discovered (`created_at` remains untouched on conflicts).

---

## 👤 Author
Created as part of a professional software engineering portfolio. Feel free to connect or reach out!