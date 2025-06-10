import pandas as pd

#Data from string to dict
def load_excel(file_path: str) -> dict:
    #xlrd library serves as an engine for reading data and formatting info from older Excel files with .xls extension:
    xl = pd.read_excel(file_path, sheet_name=None, engine="xlrd")
    return xl

#Get table names (keys) from dict to list:
def get_table_names(data: dict) -> list:
    return list(data.keys())

#Get row names using dict.get()
def get_row_names(data: dict, table_name: str) -> list:
    df = data.get(table_name)
    if df is not None:
        #Selects first column, drops null, converts val to str, converts col to list:
        return df.iloc[:, 0].dropna().astype(str).tolist()
    return []

#Get sum of row numeric values as float:
def get_row_sum(data: dict, table_name: str, row_name: str) -> float:
    df = data.get(table_name)
    if df is not None:
        #Row where first col matches row name:
        row = df[df.iloc[:, 0].astype(str) == row_name]
        if not row.empty:
            #Selects first row, exclude first column, convert value to number else NaN:
            numeric_values = pd.to_numeric(row.iloc[0, 1:], errors='coerce')
            #Drop NaN and give sum of numeric values:
            return numeric_values.dropna().sum()
    return 0.0