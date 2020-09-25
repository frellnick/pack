# utils.py (profile utilities)


import numpy as np
import pandas as pd

import logging 

ulog = logging.getLogger(__name__)

def clean_column_name(n:str) -> str:
    n = n.replace(':', '_')
    n = n.strip()
    n = n.replace (' ', '')
    return n


def prepare_data(data, filepath, **kwargs):
    def _mod_path(filepath, suffix):
        cp = filepath.split('.')
        cp[-2] = cp[-2] + suffix
        return '.'.join(cp)

    def _save_file(data, filepath, suffix='_clean'):
        spath = _mod_path(filepath, suffix)
        data.to_csv(spath, index=False)
        return spath

    def _downcast(data:pd.DataFrame):
        temp = data.copy(deep=True)
        for col in temp.columns:
            if np.issubdtype(temp[col], np.number):
                try:
                    temp[col] = pd.to_numeric(temp[col], downcast='integer')
                except:
                    pass
            else:
                pass
        return temp
    
    ulog.info(f'Checking Columns: {data.columns}')
    data.columns = [clean_column_name(column) for column in data.columns]
    ulog.info(f'Output Columns: {data.columns}')
    
    ulog.info(f'Checking for null records.')
    ulog.info(f'Raw Records: {len(data)}')
    data = data.dropna(how='all')
    ulog.info(f'Cleaned Records: {len(data)}')


    ulog.info(f"Checking DTypes for Downcasting. \
        {[f'{col}:{data[col].dtype}' for col in data.columns]}")
    data = _downcast(data)
    ulog.info(f"Final DTypes. \
        {[f'{col}:{data[col].dtype}' for col in data.columns]}")


    spath = filepath

    save = False
    if 'save_copy' in kwargs:
        if kwargs['save_copy']:
            spath = _save_file(data, filepath)
    return spath