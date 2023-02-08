# Import pandas
import logging
import pandas as pd

# Log config
logging.basicConfig(
    filename='../../logs/my_functions.log',
    filemode='a',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

# Fill all missing values with either mean or mode
def fill_all_missing_values(data):
    '''
    Fill missing values of a DataFrame.

    This function receives a pandas DataFrame, fills the missing
    values of each column and overwrites the original input with
    the result.

    Parameters
    ----------
    data : pd.core.frame.DataFrame
        A pandas DataFrame with at least one column.
    
    Returns
    -------
    This function does not return anything. It simply overwrites
    `data` with the transformed result.

    Examples
    --------
    >>> df = pd.DataFrame({'column': [1, 2, np.nan, 3]})

    >>> fill_all_missing_values(data=df)

    >>> print(df)

        column
    0        1
    1        2
    2        2
    3        3
    '''

    # Try with correct workflow
    try:
        
        # Assert type
        assert type(data) == pd.core.frame.DataFrame, 'Input `data` is not a pandas DataFrame.'

        # Assert number of columns
        assert data.shape[1] > 0, 'Input `data` has no columns.'

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
            
            # Debug log
            logging.info(f'{col} successfully transformed.')

    # Handle errors
    except:

        # Raise TypeError
        raise TypeError('Please pass a pandas DataFrame with one or more columns.')

        # Log error
        logging.error(f'Unable to transform input of type {type(data)}.')
