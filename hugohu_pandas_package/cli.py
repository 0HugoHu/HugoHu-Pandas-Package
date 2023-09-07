"""CLI interface for hugohu_pandas_package project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

from hugohu_pandas_package.base import pd


def filter_data(input_file):
    """
    Read a CSV file and filter rows based on a condition.

    Args:
        input_file (str): The path to the input CSV file.

    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    df = pd.read_csv(input_file)
    filtered_df = df[df['Age'] > 30]
    return filtered_df


def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m hugohu_pandas_package` and `$ hugohu_pandas_package `.
    """

    filtered_df = filter_data('data/data.csv')
    print(filtered_df)

