from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open("requirements.txt") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="incident_etl_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    description="ETL pipeline for the Incident Management Process Enriched Event Log dataset",
)
