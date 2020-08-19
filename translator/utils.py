# utils.py
import numpy as np

def check_datetime(values):
    return False


def utf8len(s):
    try:
        return len(s.encode('utf-8'))
    except Exception as e:
        if np.isnan(s):
            return 0
        else:
            return len(str(s).encode('utf-8'))