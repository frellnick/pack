from .templates import TemplateTest
from pack.sql.components import Query

class TableStats(TemplateTest):

    def __init__(self, tablename=None, data=None):
        self.tablename = tablename
        self.data = self._validate_data(data)

    def _validate_data(self, data:dict):
        req_data = [
            'tablenames',
            'schema',
        ]
        if data is not None:
            for rd in req_data:
                assert rd in data, f'{rd} not found in data.'
        return data

    def __repr__(self) -> str:
        return f'<Query: SingleTableTest> Table: {self.tablename}'

    def _organize(self, base, report, use_report):
        ctes = base
        if use_report:
            ctes.extend(report)
        return ctes

    def assemble(self):

        assert self.data is not None, 'Must provide data to generate statement.'
        queries = []

        if self.data is not None:
            tablenames = self.data['tablenames']
        else:
            tablenames = [self.tablename]

        t_suffix = '_STATS'
        for name in tablenames:
            q = Query(name+t_suffix)
            q.Select(f'COUNT(*) AS {name}').From(name)
            queries.append(q)

        qf = Query()
        
        base = queries
        report = []
        use_report = True
        ctes = self._organize(base, report, use_report)

        consolidation = Query(name='consolidation')
        consolidation.Select('*').From(*ctes)

        qnames = ',\n'.join([f'"{name}"' for name in tablenames])
        qf.Select('*').From(f'{consolidation.name} unpivot(\nrowcount for tablename in (\n{qnames})\n)')

        return self._stack(
            '', 'WITH',
            self._stack(',', *ctes, consolidation),
            qf,
            ';'
            )