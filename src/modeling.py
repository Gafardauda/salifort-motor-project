from __future__ import annotations

import pandas as pd


def show_data_shape(df: pd.DataFrame) -> tuple[int, int]:
    """Return the number of rows and columns in the dataset."""
    return df.shape
