def process_data(input_data):
    data = []
    # Read data from input list of dictionaries
    for row in input_data:
        if 'value' in row:
            row['value'] = row['value'] * 2  # Example transformation
            data.append(row)

    # Write transformed data to output list
    output_data = []
    for row in data:
        if 'value' in row:
            output_data.append(row['value'])

    return output_data


# Example usage
input_data = [
    {'id': 1, 'value': 10},
    {'id': 2, 'value': 20},
    {'id': 3, 'value': 30},
]

output_data = process_data(input_data)
print(output_data)
