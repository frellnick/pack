from .templates import TemplateTest
from sql.components import Query

class SingleTableTest(TemplateTest):

    def __init__(self, tablename, data=None):
        self.tablename = tablename
        self.data = self._validate_data(data)

    def _validate_data(self, data:dict):
        req_data = [
            'expected_mpi',
            'expected_id',
            'record_count'
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

        q1.Select('COUNT(*) AS total').From(self.tablename)
        q2.Select('COUNT(DISTINCT(master_person_index)) AS count_mpi').From(self.tablename)
        q3.Select('COUNT(DISTINCT(id)) AS count_id').From(self.tablename)
        if self.data is not None:
            loss.Select(
                f"{q2.name}.count_mpi - {self.data['expected_mpi']} AS loss",
                f"({q2.name}.count_mpi - {self.data['expected_mpi']})/{self.data['expected_mpi']} AS loss_perc")\
                    .From(q2)
            dropped.Select(
                f"{q3.name}.count_id - {self.data['expected_id']} AS dropped",
                f"({q3.name}.count_id - {self.data['expected_id']})/{self.data['expected_id']} AS dropped_perc")\
                    .From(q3)
            errors.Select('')
            use_report=True

        ctes = self._organize(base, report, use_report)
        q4.Select('*').From(*ctes)

        return self._stack(
            '', 'WITH',
            self._stack(',', *ctes),
            q4,
            ';'
            )