#!/usr/bin/python

import sys
import pandas as pd

def excel_to_csv(excel_file, csv_file):
    # Load spreadsheet
    xl = pd.ExcelFile(excel_file)

    # Load a sheet into a DataFrame by its name
    df = xl.parse(xl.sheet_names[0])

    # Write the dataframe object into CSV file
    df.to_csv(csv_file, index=None, header=True)

def main():
    # sys.argv[0] is the script name itself, so we skip that
    excel_file = sys.argv[1]
    csv_file = sys.argv[2]
    excel_to_csv(excel_file, csv_file)

if __name__ == '__main__':
    main()
