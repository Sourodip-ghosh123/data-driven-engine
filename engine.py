import csv
from pathlib import Path

class DataDrivenTestEngine:
    def __init__(self, csv_path, factory):
        self.csv_path = Path(csv_path)
        self.factory = factory

    def load_test_cases(self):
        with self.csv_path.open(newline='') as f:
            reader = csv.DictReader(f)
            return [self.factory.create(row) for row in reader]