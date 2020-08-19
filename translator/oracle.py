# oracle.py


from translator.tbase import Translator 


class OracleTranslator(Translator):
    def __init__(self, instructionset=OracleInstructions):
        super().__init__(instructionset)