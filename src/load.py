"""
load.py
Module for loading processed data into various storage systems.
"""

import pandas as pd
from sqlalchemy import create_engine


def load_to_csv(df: pd.DataFrame, file_path: str, index: bool = False) -> None:
    """
    Save a pandas DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame to save.
        file_path (str): Destination file path.
        index (bool, optional): Whether to write row names (index). Defaults to False.
    """
    df.to_csv(file_path, index=index)


def load_to_sql(
    df: pd.DataFrame,
    table_name: str,
    connection_string: str,
    if_exists: str = "replace",
) -> None:
    """
    Load a pandas DataFrame into a SQL table using SQLAlchemy.

    Args:
        df (pd.DataFrame): DataFrame to load.
        table_name (str): Name of the target table.
        connection_string (str): SQLAlchemy connection string.
        if_exists (str, optional): Behavior if the table already exists ("replace", "append"). Defaults to "replace".
    """
    engine = create_engine(connection_string)
    with engine.begin() as connection:
        df.to_sql(name=table_name, con=connection, if_exists=if_exists, index=False)
