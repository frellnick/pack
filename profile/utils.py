# utils.py (profile utilities)


def clean_column_name(n:str) -> str:
    n = n.replace(':', '_')
    n = n.strip()
    n = n.replace (' ', '')
    return n


def prepare_data(data, filepath, save=False):
    def _mod_path(filepath, suffix):
        cp = filepath.split('.')
        cp[-2] = cp[-2] + suffix
        return '.'.join(cp)

    def _save_file(data, filepath, suffix='_clean'):
        spath = _mod_path(filepath, suffix)
        data.to_csv(spath, index=False)
        return spath

    
    data.columns = [clean_column_name(column) for column in data.columns]
    data = data.dropna(how='all')

    spath = filepath

    if save:
        spath = _save_file(data, filepath)
    return spath