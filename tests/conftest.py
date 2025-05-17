import os
import pytest
from engine import DataDrivenTestEngine
from factory import TestFactory

def pytest_generate_tests(metafunc):
    if 'case' in metafunc.fixturenames:
        csv_path = os.path.join(os.path.dirname(__file__),
                                'data', 'test_cases.csv')
        engine = DataDrivenTestEngine(csv_path, TestFactory())
        test_cases = engine.load_test_cases()
        ids = [f"case_{c.case_id}" for c in test_cases]
        metafunc.parametrize("case", test_cases, ids=ids)