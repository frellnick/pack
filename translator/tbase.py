# base.py


class Translator():
    def __init__(self, instructionset):
        self.instructionsset = instructionset


    def _process(self, column):
        tfn = self.instructions[column['vartype']]
        return tfn(column)


    def __call__(self, profile):
        translation = []
        for column in profile:
            translation.append(self._process(column))
        return translation