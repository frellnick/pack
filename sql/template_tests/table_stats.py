from .templates import TemplateTest
from sql.components import Query

class TableStats(TemplateTest):

    def __init__(self, tablename, data=None):
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
        queries = [Query(name=table) for table in self.data['tablenames']]
        q1 = Query(name='total_count')
        q2 = Query(name='distinct_mpi')
        q3 = Query(name='distinct_id')
        loss = Query(name='loss')
        dropped=Query(name='dropped')
        errors = Query(name='errors')
        q4 = Query()

        base = [q1, q2, q3]
        report = [loss, dropped]
        use_report = False

        ctes = self._organize(base, report, use_report)
        q4.Select('*').From(*ctes)

        return self._stack(
            '', 'WITH',
            self._stack(',', *ctes),
            q4,
            ';'
            )