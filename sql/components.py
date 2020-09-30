# components.py

## Base Class ##

class Query():
    def __init__(self, name=None) -> None:
        self.query_comp = []
        self.cursor = 0
        self.name = name

    def __repr__(self) -> str:
        return self._assemble()

    def __str__(self) -> str:
        return self._assemble()

    def _assemble(self) -> str:
        body = '\n'.join(self.query_comp)
        if self.name is None:
            return body
        else:
            return f'{self.name} AS (\n{body}\n)'


    def _get_len(self) -> int:
        return sum([len(item) for item in self.query_comp])

    def _cursor_to_end(self) -> None:
        self.cursor = self._get_len()

    def Select(self, *args, **kwargs):
        s = Select()
        self.query_comp.insert(self.cursor, s(*args))
        self._cursor_to_end()
        return self

    def From(self, *args):
        f = From()
        self.query_comp.insert(self.cursor, f(*args))
        self._cursor_to_end()
        return self

        

## Individual Components ##

class Component():
    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs

    def __repr__(self) -> str:
        return self.assemble()

    def __call__(self, *args):
        if len(args) > 0:
            self.args = args
        return self.assemble()

    def assemble(self):
        pass



class Select(Component):
    def __init__(self, *args) -> None:
        super().__init__(*args)

    def assemble(self):
        rstr = ',\n\t'.join(self.args)
        return f'SELECT\n\t{rstr}'


class From(Component):
    def __init__(self, *args) -> None:
        super().__init__(*args)

    def _to_str(self, items):
        str_list = []
        for item in items:
            if hasattr(item, 'name'):
                str_list.append(item.name)
            else:
                str_list.append(item)
        return str_list

    def assemble(self):
        rstr = ',\n\t'.join(self._to_str(self.args))
        return f'FROM\n\t{rstr}'