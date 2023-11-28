import pandas as pd

def excel_to_csv(input_file, output_file, column1, column2):
    # Load the Excel file
    df = pd.read_excel(input_file)

    # Select the desired columns and ignore the first row
    df = df[[column1, column2]].iloc[1:]

    # Drop rows where either of the selected columns is blank
    df = df.dropna(subset=[column1, column2])

    # Save to CSV
    df.to_csv(output_file, index=False)

# Usage
excel_to_csv('input_file.xlsx', 'output_file.csv', 'Column1', 'Column2')
