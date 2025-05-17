from .test_case import TestCase # type: ignore

class TestFactory:
    def create(self, data: dict) -> TestCase:
        case_id    = data.get('id') or data.get('test_id')
        input_expr = data['input']
        expected   = self._cast_expected(data['expected'])
        return TestCase(case_id, input_expr, expected)

    def _cast_expected(self, value: str):
        for caster in (int, float):
            try:
                return caster(value)
            except (ValueError, TypeError):
                continue
        return value