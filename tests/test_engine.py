def test_case_execution(case):
    assert case.execute() == case.expected