#!/usr/bin/env python3

"""Simple pagination"""


import csv

# Assume that the CSV file is named 'your_dataset.csv'
# Replace 'your_dataset.csv' with the actual name of your CSV file.

def index_range(page, page_size):
    # Assume index_range function is defined as provided in the previous example

def get_page(page=1, page_size=10):
    """
    Get the specified page of the dataset.

    Parameters:
    - page (int, optional): Page number (1-indexed). Default is 1.
    - page_size (int, optional): Number of items per page. Default is 10.

    Returns:
    List: The appropriate page of the dataset.
    """
    assert isinstance(page, int) and page > 0, "Page must be an integer greater than 0."
    assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0."

    # Assuming the CSV file is named 'your_dataset.csv'
    with open('your_dataset.csv', 'r') as csvfile:
        # Read the CSV file into a list of dictionaries
        dataset = list(csv.DictReader(csvfile))

        # Calculate start and end indexes using the index_range function
        start_index, end_index = index_range(page, page_size)

        # Return the appropriate page of the dataset
        return dataset[start_index:end_index]

# Example usage:
# Replace 'your_dataset.csv' with the actual name of your CSV file.
result = get_page(page=2, page_size=5)
print(result)
