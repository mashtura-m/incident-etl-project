import pandas as pd
import pytest

from src.extract import extract_csv
from src.transform import clean_data, engineer_features
from src.load import load_to_csv
from src.validate import validate_columns


def test_extract_csv(tmp_path):
    """Test extracting a CSV file into a DataFrame."""
    # Create a temporary CSV file
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    csv_path = tmp_path / "sample.csv"
    df.to_csv(csv_path, index=False)

    # Use the extract_csv function to read the file
    extracted = extract_csv(str(csv_path))

    # Ensure the returned DataFrame matches the original
    assert not extracted.empty
    assert list(extracted.columns) == ["A", "B"]


def test_validate_columns():
    """Test the validate_columns function with required columns."""
    df = pd.DataFrame({"incident_id": [1], "timestamp": ["2021-01-01T00:00:00"]})
    required = ["incident_id", "timestamp"]
    assert validate_columns(df, required)
