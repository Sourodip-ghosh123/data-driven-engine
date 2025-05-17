# Data-Driven Test Engine

A Python & CSV-driven test engine with dynamic test generation and parameterization.  
Leveraged pytest fixtures & factory pattern; coverage via pytest-cov; parallel runs via pytest-xdist.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

data-driven-engine/
├── .gitignore
├── README.md
├── requirements.txt
├── pytest.ini
├── .vscode/
│   └── settings.json
├── data_driven_engine/
│   ├── __init__.py
│   ├── engine.py
│   ├── factory.py
│   └── test_case.py
└── tests/
    ├── data/
    │   └── test_cases.csv
    ├── conftest.py
    └── test_engine.py

## Run tests

```bash
pytest
```

HTML coverage reports will land in `htmlcov/` and `reports/`.