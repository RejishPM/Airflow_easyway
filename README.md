# Airflow + dbt + MLflow Pipeline

A containerized ELT pipeline powered by **Apache Airflow**, **dbt**, and **MLflow**, orchestrated via Docker.  
This project automates dbt model execution using Airflow and logs tracking information using MLflow. Designed for modularity, it supports future extension with machine learning experiments and model versioning.

---

## 📦 Tech Stack

- **Apache Airflow** – Workflow orchestration
- **dbt (Data Build Tool)** – SQL-based data transformation
- **MLflow** – Model tracking and experiment logging
- **Docker Compose** – Local container orchestration
- **Operators Used**: `PythonOperator`, `BashOperator`

---

## 🧭 Project Structure

```
airflow_easyway/
├── dags/
│   └── dbt_dag.py              # DAG triggering dbt transformations
├── dbt/
│   └── my_dbt_project/         # Your dbt project directory
├── mlflow/
│   └── mlruns/                 # MLflow tracking logs
├── Dockerfile
├── docker-compose.yaml
├── docker-compose.mlflow.yaml
└── README.md
```

---

## 🚀 Pipeline Overview

1. **Airflow** triggers the `dbt_dag` which:
   - Uses `BashOperator` to run dbt models.
   - Uses `PythonOperator` to log artifacts to MLflow.
2. **MLflow** runs in a separate container, ready to track future machine learning experiments.
3. Containers communicate through custom Docker networks for isolation and flexibility.

---

## ⚙️ Prerequisites

- Docker and Docker Compose installed
- Recommended: Docker Compose v2+

---

## 🛠️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/RejishPM/airflow_easyway.git
cd airflow_easyway
```

### 2. Create Required Docker Networks

This is **mandatory** to allow Airflow and MLflow containers to communicate.

```bash
docker network create mlflow_network && docker network create elt_network
```

> These networks are required if not defined inside `docker-compose.yaml`.

### 3. Start the Containers

```bash
docker-compose -f docker-compose.yaml -f docker-compose.mlflow.yaml up -d
```

- Airflow UI → [http://localhost:8080](http://localhost:8080)  
- MLflow UI → [http://localhost:5000](http://localhost:5000)

### 4. Trigger the DAG

- Visit the Airflow UI
- Enable and manually trigger the DAG named `dbt_dag`

---

## 🔍 Why Separate MLflow?

MLflow is run in its own container to:
- Isolate experiment tracking logic from orchestration
- Allow seamless scaling when ML components are added
- Track metadata and model artifacts (to be integrated soon)

---

## 📤 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

[MIT License](LICENSE)

---

## 🙌 Author

Made with 💻 and ☕ by **[Rejish P M](https://github.com/RejishPM)**