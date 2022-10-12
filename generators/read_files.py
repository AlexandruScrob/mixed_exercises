from pathlib import Path
from typing import NamedTuple


current_path = Path.cwd() / "generators"


class MyDataPoint(NamedTuple):
    x: float
    y: float
    z: float


def mydata_reader(file):
    for row in file:
        cols = row.rstrip().split(",")
        cols_list = [float(c) for c in cols]
        yield MyDataPoint._make(cols_list)


def example_reader():
    with open(f"{current_path}\mydata.txt") as file:
        for row in mydata_reader(file):
            print(row)


example_reader()
