from src.jobs import read


def get_unique_job_types(path):
    table = read(path)
    job_types = [row["job_type"] for row in table]

    return list(set(job_types))


def filter_by_job_type(jobs, job_type):
    filtered_jobs = list()
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    table = read(path)
    industries = list()
    for row in table:
        if row["industry"]:
            industries.append(row["industry"])

    return set(industries)


def filter_by_industry(jobs, industry):
    filtered_industry = list()
    for job in jobs:
        if job["industry"] == industry:
            filtered_industry.append(job)

    return filtered_industry


def get_max_salary(path):
    table = read(path)
    salaries = set()
    for row in table:
        if row["max_salary"] and row["max_salary"] != "invalid":
            salaries.add(int(row["max_salary"]))

    return max(salaries)


def get_min_salary(path):
    table = read(path)
    salaries = set()
    for row in table:
        if row["min_salary"] and row["min_salary"] != "invalid":
            salaries.add(int(row["min_salary"]))

    return min(salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Salary doesn't exists")

    if (
        type(salary) != int
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
    ):
        raise ValueError("Salary is not an integer")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError('"min_salary" is greather than "max_salary"')

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True

    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
