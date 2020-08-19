# base.py


class Translator():
    def __init__(self, instructionset):
        self.instructionset = instructionset


    def _process(self, column):
        tfn = self.instructionset[column['vartype']]
        return tfn(column)


    def translate(self, profile):
        col_translations = []
        for column in profile:
            col_translations.append(self._process(column))
        return col_translations