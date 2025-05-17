class TestCase:
    def __init__(self, case_id, input_expr, expected):
        self.case_id    = case_id
        self.input_expr = input_expr
        self.expected   = expected

    def execute(self):
        return eval(self.input_expr)

    def __repr__(self):
        return (f"<TestCase id={self.case_id!r} "
                f"input={self.input_expr!r} expected={self.expected!r}>")
