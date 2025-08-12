"""
transform.py
Module for transforming data extracted from the incident management dataset.
"""

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic data cleaning, such as dropping duplicates and handling missing values.

    Args:
        df (pd.DataFrame): Raw DataFrame to clean.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Drop duplicate rows
    df_clean = df.drop_duplicates().copy()

    # Handle missing values: numeric columns -> median, categorical -> mode
    for col in df_clean.columns:
        if pd.api.types.is_numeric_dtype(df_clean[col]):
            median_value = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(median_value)
        else:
            mode_value = df_clean[col].mode().iloc[0] if not df_clean[col].mode().empty else None
            df_clean[col] = df_clean[col].fillna(mode_value)

    return df_clean


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform feature engineering on the dataset.

    Example operations include:
      - Converting timestamp columns to datetime objects.
      - Creating duration features between events.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with engineered features.
    """
    df_feat = df.copy()

    # Convert 'Timestamp' or 'timestamp' column to datetime if exists
    for col in ['Timestamp', 'timestamp', 'EventTime', 'event_time']:
        if col in df_feat.columns:
            df_feat[col] = pd.to_datetime(df_feat[col], errors='coerce')

    # Example: compute duration between 'StartTime' and 'EndTime' if both exist
    if 'StartTime' in df_feat.columns and 'EndTime' in df_feat.columns:
        df_feat['duration_seconds'] = (pd.to_datetime(df_feat['EndTime']) - pd.to_datetime(df_feat['StartTime'])).dt.total_seconds()

    return df_feat
