import pandas as pd


def create_array():

    data_source_file_path = "./files/muestra.xlsx"

    # Read the Excel file into a Pandas DataFrame
    df = pd.read_excel(data_source_file_path, dtype=str).iloc[:, 0]

    get_df_values = df.values

    formated_array = map(lambda x: [x[i:i + 2]
                                    for i in range(0, len(x), 2)], get_df_values)

    return list(formated_array)


if __name__ == '__main__':
    create_array()
