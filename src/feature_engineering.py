from __future__ import annotations

import pandas as pd


def add_column_flag(df: pd.DataFrame, column_name: str, new_column_name: str, value: object) -> pd.DataFrame:
    """Create a new flag column based on an existing column."""
    df = df.copy()
    df[new_column_name] = df[column_name].apply(lambda x: value if x else 0)
    return df
