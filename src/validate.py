"""
validate.py
Module for validating data quality and schema requirements.
"""

import pandas as pd


def validate_columns(df: pd.DataFrame, required_columns: list) -> None:
    """
    Ensure that the DataFrame contains the required columns.

    Args:
        df (pd.DataFrame): Input DataFrame.
        required_columns (list): List of column names expected in df.

    Raises:
        ValueError: If any required column is missing.
    """
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def check_missing_values(df: pd.DataFrame) -> pd.Series:
    """
    Compute the number of missing values per column in the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.Series: Series where the index is the column names and the values are counts of missing values.
    """
    return df.isna().sum()
