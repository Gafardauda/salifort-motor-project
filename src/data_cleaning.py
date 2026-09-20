from __future__ import annotations

import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(file_path)


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    return df.drop_duplicates().reset_index(drop=True)


def summarize_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Return a DataFrame of missing values per column."""
    return df.isna().sum().to_frame(name='missing_values')
