"""
extract.py
Module for extracting data from sources.
"""

import pandas as pd
from typing import Optional

def extract_csv(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the extracted data.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        # Re-raise with context
        raise RuntimeError(f"Error reading CSV file {file_path}: {e}") from e
