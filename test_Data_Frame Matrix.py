
import numpy as np
import pandas as pd

# Pandas: Generate matrix [4x6] of random integers

matrix_rows = 4
matrix_columns = 6

#       col_1  col_2  col_3  col_4  col_5  col_6
# rw_1    500      7    119    228    633    140
# rw_2    712    527    482    419    599    605
# rw_3     60    464    382    258    978    423
# rw_4    284    721     47    324    410    166

def Random_Matrix(rows : int, columns: int) ->  pd.DataFrame:

    # Generate an array of random float numbers: [0.123, -0.345,...]
    random_values = np.random.random(rows * columns ).reshape(rows, columns)

    # Array of floats: transform each number to the positive integer
    random_pos_values = abs(random_values * 1000)

    # Rows: generate the list of the names like: ['rw_1', 'rw_2' ..
    rows_list = list(map(lambda x: f"rw_{x}", np.arange(1,rows + 1)))
    rows_arr = pd.Index(rows_list)

    # Columns: generate the list of the names like: ['col_1', 'col_2' ..
    columns_list = list(map(lambda x: f"col_{x}", np.arange(1,columns + 1)))    

    # Matrix:
    df1 = pd.DataFrame(random_pos_values, index=rows_arr, copy=False, columns=columns_list, dtype=np.int32 )
    return df1


if __name__ == "__main__":
    df_matrix = Random_Matrix(matrix_rows,matrix_columns)
    print (df_matrix)
