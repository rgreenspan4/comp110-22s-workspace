"""Some helpful utility fns for working with CSV files."""

from csv import DictReader


def read_cvs_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a cvs into a table."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the datafile as a csv rather than jsut strings
    csv_reader = DictReader(file_handle)

    # read each row of CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close the file when we are done, to free its resources
    file_handle.close()
    return result


def column_value(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str[ of all values in a single comlumn."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table into a column oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_value(row_table, column)
    return result