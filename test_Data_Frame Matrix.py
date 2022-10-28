
import numpy as np
import pandas as pd


# Pandas: Generate matrix [21x43] of random integers - use "Reshape()"

matrix_rows = 21
matrix_columns = 43


#       col_0  col_1  col_2  col_3  col_4  col_5  col_6  col_7  col_8  col_9  col_10  col_11  col_12
# rw_0    119    959    831    181    401    374    978    903    126    623     432     819     637
# rw_1    119     12    336    137      6    741    964    651    752     55     774     246     715
# rw_2    191    143     15    876    161    391    558    784    857    207     317     581       6
# rw_3    428    478    957    260    723    744    838    937    567    890     134     180     894
# rw_4    976    871    642     99    466    911    837    250    772     80     836     379     717
# rw_5    421    711    802    737    379    159    800     76    552    813      18     873      49
# rw_6    858    943     25    675    890    788    751    291    677    726     378     677     430
# rw_7    598    877    983    885    149    824     71    675    599    199     122     749     188
# rw_8    752    578    839    235    471    689    801    696    291    815     792     543     308
# rw_9    428     98    580    771    168    808    263    654     23    318     774     443     758
def Random_Matrix(rows : int, columns: int) ->  pd.DataFrame:

    # array of random float numbers: [0.123, -0.345,...]
    random_values = np.random.random(rows * columns ).reshape(rows, columns)

    # transform floats to tositive integers 
    random_pos_values = abs(random_values * 1000)

    # Rows: generate the list of the names like: ['rw_0', 'rw_1' ..
    rows_list = []
    for i in range(rows):
        rows_list.append(f"rw_{i}")
    rows_arr = pd.Index(rows_list)

    # Columsn: generate the list of the names like: ['col_0', 'col_1' ..
    columns_list = []
    for i in range(columns):
        columns_list.append(f"col_{i}")

    # Matrix:
    df1 = pd.DataFrame(random_pos_values, index=rows_arr, copy=True, columns=columns_list, dtype=np.int32 )
    return df1


if __name__ == "__main__":
    df_matrix = Random_Matrix(matrix_rows,matrix_columns)
    print (df_matrix)