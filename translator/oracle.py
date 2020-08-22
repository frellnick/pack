# oracle.py


import datetime

from translator.tbase import Translator

from translator.utils import check_datetime, utf8len

### Oracle Spec
# [
#     {
#         "tableName":"USHE_GRADUATION_DEMO_08102020", 
#         "entityType":"TABLE",
#         "columns":[
#             {"columnName":"COL1NAME", "columnType":"VARCHAR2", "size":"26", "mantissa":null, "hashed":false},
#             {"columnName":"COL2NAME", "columnType":"VARCHAR2", "size":"26", "mantissa":null, "hashed":false}
#         ]
#     },
# ]

OracleColSpec = {
    'columnName': None,
    'columnType': None,
    'size': None,
    'mantissa': None,
    'hashed': False
}


def _translate_text(profile, colspec=OracleColSpec):

    def _infer_text_types(varoptions):
        if check_datetime(varoptions):
            return 'datetime'
        else:
            if _get_max_text_size(varoptions) < 3500:
                return 'VARCHAR2'
            else:
                return 'CLOB'

    def _get_max_text_size(varoptions):
        smax = 0
        for val in varoptions:
            vlen = utf8len(val)
            if vlen > smax:
                smax = vlen
        return smax

    spec = colspec.copy()
    spec['columnName'] = profile['name']
    spec['columnType'] = _infer_text_types(profile['varoptions'])
    spec['size'] = _get_max_text_size(profile['varoptions'])
    spec['mantissa'] = None

    return spec


def _translate_numeric(profile, colspec=OracleColSpec):
    
    def _infer_num_types(varoptions):
        return 'NUMBER'

    def _get_max_num_size(varoptions):
        precisions = [len(str(option).split('.')[0]) for option in varoptions]
        return max(precisions)

    def _est_mantissa(varoptions):
        decimals = [len(str(option).split('.')) > 1 for option in varoptions]
        if sum(decimals) >= 1:
            mantissa = [len(str(option).split('.')[-1]) for option in varoptions]
            return max(mantissa)
        else:
            return 0

    spec = colspec.copy()
    spec['columnName'] = profile['name']
    spec['columnType'] = _infer_num_types(profile['varoptions'])
    spec['size'] = _get_max_num_size(profile['varoptions'])
    spec['mantissa'] = _est_mantissa(profile['varoptions'])

    return spec




OracleInstructions = {
    'text': _translate_text,
    'numeric': _translate_numeric,
}



class OracleTranslator(Translator):
    def __init__(self, tablename, instructionset=OracleInstructions):
        super().__init__(instructionset)
        self.tablename = tablename


    def translate(self, profile):
        date = datetime.datetime.now()
        fdate = '-'.join([str(x) for x in [date.year, date.month, date.day]])
        return {
            'tableName': self.tablename.split('.')[0],
            'entityType': 'Table',
            'columns': super().translate(profile),
        }

    def __call__(self, profile):
        return self.translate(profile)