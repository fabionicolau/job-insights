from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode="r", encoding="utf-8") as file:
        table = csv.DictReader(file)
        return list(table)
