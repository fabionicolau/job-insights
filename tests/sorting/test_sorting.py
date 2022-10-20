from src.sorting import sort_by

mock = [
    {
        "min_salary": 1000,
        "max_salary": 6000,
        "date_posted": "2021-05-05",
    },
    {
        "min_salary": 300,
        "max_salary": 10000,
        "date_posted": "2022-05-05",
    },
    {
        "min_salary": 600,
        "max_salary": 3000,
        "date_posted": "2020-05-05",
    },
]


def test_sort_by_criteria():
    sort_by(mock, "min_salary")
    assert mock[0]["min_salary"] == 300

    sort_by(mock, "max_salary")
    assert mock[0]["max_salary"] == 10000

    sort_by(mock, "date_posted")
    assert mock[0]["date_posted"] == "2022-05-05"
