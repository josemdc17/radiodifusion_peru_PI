import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
excel_file_path = 'muestra.xlsx'

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path, dtype=str).iloc[:, 0]

arraynew = df.values

arraynewnew = map(lambda x: [x[i:i + 2]
                  for i in range(0, len(x), 2)], arraynew)


# Display basic information about the DataFrame
print(arraynew)
print('-----------------------------------')
print('-----------------------------------')
print(list(arraynewnew))
