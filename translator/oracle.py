# oracle.py


from translator.tbase import Translator 

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



def _translate_text(profile):
    pass 



def _translate_numeric(profile):
    pass



OracleInstructions = {
    'text': _translate_text,
    'numeric': _translate_numeric,
}

class OracleTranslator(Translator):
    def __init__(self, instructionset=OracleInstructions):
        super().__init__(instructionset)