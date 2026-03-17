# Enterprise Utility Data Pipeline Orchestration using Apache Airflow

## Project Overview
This project shows how I can orchestrate enterprise utility data pipelines from start to end using Apache Airflow concepts.

It is based on a utility-style workflow where multiple datasets and dependent steps must run in the correct order. The project includes raw data validation, Bronze loading, Silver transformation, Gold publishing, KPI generation, and execution logging.

The notebook is built in Google Colab for easy execution, and a separate Airflow DAG file is included in the repository to show real workflow structure and task dependency design.

---

## Business Goal
The goal of this project is to show how pipeline orchestration improves:
- workflow sequencing
- dependency handling
- retries
- failure logging
- operational stability
- consistent data delivery

---

## Tools Used
- Python
- Pandas
- NumPy
- Apache Airflow concepts
- Google Colab

---

## Pipeline Stages
1. Validate raw input data
2. Load Bronze layer
3. Transform Silver layer
4. Publish Gold layer
5. Generate KPI output
6. Write pipeline summary
7. Save execution log
