# templates.py

class TemplateTest():
    def __repr__(self) -> str:
        return f'<TestTemplate: Undefined>'

    def _stack(self, delim, *args):
        return f'{delim}\n'.join([str(a) for a in args])

    def assemble(self):
        pass

    def export(self, path):
        with open(path, 'w+') as file:
            file.write(self.assemble())


