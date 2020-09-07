"""
Profiler

Create metadata from raw columnar information
"""

import pandas as pd
from .utils import *


class Profiler():
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    def load_csv(self, filepath, **kwargs):
        self.data = pd.read_csv(filepath, low_memory=False)
        clean_path = prepare_data(self.data, filepath, **kwargs)  # Changes data in place   
        return clean_path

    def load_frame(self, dataframe, **kwargs):
        self.data = dataframe
        return self.data.head()

    def _det_size(self, data: pd.DataFrame, **kwargs):
        if 'num_items' in kwargs:
            return kwargs['num_items']
        return len(data)

    def run_profile(self, data: pd.DataFrame, **kwargs) -> pd.DataFrame:
        descriptions = _get_descriptions(data)
        return _build_metadata_from_profiles(
            descriptions=descriptions,
            data=data,
            num_items=self._det_size(data, **kwargs)
        )

    @property
    def profile(self):
        return self.run_profile(self.data, **self.kwargs)



def _get_description(series: pd.Series) -> pd.Series:
    return series.describe()


def _get_descriptions(dataframe: pd.DataFrame) -> list:
    return list(map(
        _get_description,
        [dataframe[col] for col in dataframe.columns]))


def _get_type(profile: pd.Series) -> str:
    if profile._is_numeric_mixed_type:
        return 'numeric'
    else:
        return 'text'


def _get_text_options(series: pd.Series) -> list:
    return series.unique()


def _get_numeric_options(series: pd.Series) -> list:
    def _check_int_replacement(x, y):
        if (x % 1 == 0) and (y % 1 == 0):
            return int(x), int(y)
        else:
            return x, y

    return _check_int_replacement(series.min(), series.max())


def _get_varoptions(vartype, series) -> list:
    option_generators = {
        'text': _get_text_options,
        'numeric': _get_numeric_options,
    }
    return option_generators[vartype](series)


def _build_metadata_from_profile(profile: pd.Series, data: pd.DataFrame, num_items: int):
    return _compile_dict(
        name = profile.name,
        varsize = 1,
        num_items = num_items,
        vartype = _get_type(profile), 
        varoptions = _get_varoptions(_get_type(profile), data[profile.name])
    )

def _build_metadata_from_profiles(descriptions, data, num_items):
    return [_build_metadata_from_profile(profile, data, num_items) for profile in descriptions]


def _compile_dict(*args, **kwargs) -> dict:
    return kwargs