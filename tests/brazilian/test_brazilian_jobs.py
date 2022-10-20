from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    table = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for row in table:
        assert ("title" in row) and ("salary" in row) and ("type" in row)
