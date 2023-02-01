# Import pandas
import pandas as pd

# Fill all missing values with either mean or mode
def fill_all_missing_values(data):

    # Iterate over columns
    for col in data.columns:

        # Fill numeric columns with mean
        if data[col].dtype in ['float64', 'int64']:
            data[col].fillna(
                data[col].mean(),
                inplace=True
            )
        
        # Fill all other types with mode
        else:
             data[col].fillna(
                data[col].mode().item(),
                inplace=True
            )