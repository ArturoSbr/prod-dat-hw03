# Imports
import numpy as np
import pandas as pd
from my_functions import fill_all_missing_values

# Input dataframe
df = pd.DataFrame(
    {
        'col_num': [1, 2, np.nan, 3],
        'col_str': ['a', 'a', np.nan, 'b']
    }
)

# Fill all missing values
fill_all_missing_values(df)

# Assert if col_num filled correctly
def test_fill_num():
    assert df.loc[2, 'col_num'] == 2.0

# Assert if col_str filled correctly
def test_fill_str():
    assert df.loc[2, 'col_str'] == 'a'
