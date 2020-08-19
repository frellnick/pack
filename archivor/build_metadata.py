# build_metadata.py

import json

def agg_translations(translations: list, filepath=None):
    if filepath is None:
        return json.dumps(translations)
    else:
        with open(filepath, 'w+') as f:
            json.dump(translations, f)
