# Import pandas
import logging
import pandas as pd

# Log config
logging.basicConfig(
    filename='../logs/my_functions.log',
    filemode='w',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

# Fill all missing values with either mean or mode
def fill_all_missing_values(data):
    try:
        
        # Assert type
        assert(type(data) == pd.core.frame.DataFrame)

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
    except:
        
        True
