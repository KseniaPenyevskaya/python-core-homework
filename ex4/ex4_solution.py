from typing import Iterator, List, Tuple


def cross_join(
    employees: List[str], departments: List[str]
) -> Iterator[Tuple[str, str]]:
    """
    Реализует декартово произведение списков employees и departments

    :param employees: Список LastName сотрудников таблицы Employee
    :param departments: Список DepartmentName таблицы Department
    :return: Генератор пар (LastName, DepartmentName)
    """
    # put your code here
    return (
        (employee, department) for employee in employees for department in departments
    )
