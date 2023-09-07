# CLI interface for hugohu_pandas_package project.

import pandas as pd


def filter_data(input_file):
    """
    Read a CSV file and filter rows based on a condition.

    Args:
        input_file (str): The path to the input CSV file.

    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    df = pd.read_csv(input_file)
    filtered_df = df[df["Age"] > 30]
    return filtered_df


def main():
    """
    The main function executes on commands:
    `python -m hugohu_pandas_package`
        and `$ hugohu_pandas_package `.
    """
    filtered_df = filter_data("data/data.csv")
    print(filtered_df)
