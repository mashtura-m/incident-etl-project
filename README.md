# Incident Management ETL Pipeline

## Project Overview

This repository implements a scalable Extract ‑ Transform ‑ Load (ETL) pipeline for the **Incident Management Process Enriched Event Log** dataset from the UCI Machine Learning Repository. The dataset contains event logs from incident management processes with timestamps, incident IDs, severities, categories and other attributes. The goal of this project is to build a data pipeline that ingests the raw event log, cleans and enriches the data, and loads the results into a structured data store where analysts can compute metrics such as average resolution times, trend analysis and resource utilization.

The code is organized into modular components under the `src/` directory:

- **extract.py** – Functions to read raw CSV logs or download data from remote sources.
- **transform.py** – Cleaning and feature‑engineering functions such as handling missing values, calculating durations between events, encoding categorical variables and normalizing numeric fields.
- **load.py** – Utilities to persist the processed data to flat files (CSV), relational databases using SQLAlchemy, or cloud storage.
- **validate.py** – Data quality checks to ensure required columns exist and to detect missing values.
- **utils.py** – Helper functions for logging and timestamp generation.

A set of unit tests is provided in `tests/` to verify that extraction, transformation and validation work as expected.

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/mashtura-m/incident-etl-project.git
   cd incident-etl-project
   ```

2. **Create a Python environment** (optional but recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # on Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**

   All required packages are listed in `requirements.txt`. Install them with pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare data**

   Place the raw dataset files (CSV or JSON) into the `data/raw/` directory. For example, download the **Incident Management Process Enriched Event Log** CSV from UCI and store it in that folder.

5. **Configure database (optional)**

   If you intend to load data into a relational database, set up a database (e.g. PostgreSQL) and adjust the SQLAlchemy connection string in `src/load.py`.

## Usage

Run each stage of the pipeline from the command line or integrate them into a script:

```bash
# Extract raw CSV into a DataFrame
python3 -c "from src.extract import extract_csv; df = extract_csv('data/raw/incident_log.csv'); print(df.head())"

# Clean and engineer features
python3 -c "from src.transform import clean_data, engineer_features; import pandas as pd; df = pd.read_csv('data/raw/incident_log.csv'); df_clean = clean_data(df); df_feat = engineer_features(df_clean); print(df_feat.head())"

# Load processed data to a CSV file
python3 -c "import pandas as pd; from src.load import load_to_csv; df = pd.read_csv('data/processed/processed_incident_log.csv'); load_to_csv(df, 'data/processed/final_incident_log.csv')"
```

Alternatively, write a driver script that calls these functions in sequence. See `tests/test_pipeline.py` for example usage and test cases.

To run the test suite:

```bash
pytest
```

If you prefer containerization, build and run the Docker image:

```bash
docker build -t incident-etl .
docker run --rm incident-etl
```

## Business Insights

After loading the processed data into a database or analytical environment, you can derive valuable metrics to improve incident management:

- **Resolution time analysis** – calculate average and median resolution times by severity, category or department to identify bottlenecks.
- **Incident trends** – plot incidents over time to detect peaks, recurring issues and seasonal patterns.
- **Resource allocation** – examine which teams handle the most incidents and adjust staffing accordingly.
- **Process compliance** – measure the time between event stages to ensure incidents follow defined SLAs.

You can visualize these findings using Jupyter notebooks in the `notebooks/` directory or with BI tools such as Tableau or Power BI.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
