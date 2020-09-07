# utils.py (profile utilities)


def clean_column_name(n:str) -> str:
    n = n.replace(':', '_')
    n = n.strip()
    n = n.replace (' ', '')
    return n


def prepare_data(data, filepath):
    pass