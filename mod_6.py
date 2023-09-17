from pathlib import Path

# region 01
print("Ex.01")


def total_salary(path: Path) -> float:
    salary = 0.0
    lines = []
    fh = open(path)
    while True:
        line = fh.readline()
        if not line:
            break
        lines.append(line)
    fh.close()
    for l in lines:
        new_line = l.split(",")
        salary += float(new_line[1])
    return salary


salary = Path("salary.txt")
# print(total_salary(salary))
# endregion

# region 02
print("Ex.02")


def write_employees_to_file(employee_list, path):
    employee = ""
    for e in employee_list:
        for i in e:
            employee = employee + str(i) + "\n"
    fh = open(path, "w")
    fh.write(employee)
    fh.close()

# employee_list = [["Robert Stivenson,28", "Alex Denver,30"], ["Drake Mikelsson,19"]]
# path = Path("employee_list.txt")
# write_employees_to_file(employee_list, path)

# endregion


# region 03
print("Ex.03")


def read_employees_from_file(path):
    fh = open(path, "r")
    employees = fh.read()
    fh.close()
    employees_list = employees.split("\n")
    if not employees_list[-1]:
        employees_list.pop()
    return employees_list

# print(read_employees_from_file("employee_list.txt"))
# endregion


# region 04
print("Ex.04")


def add_employee_to_file(record, path):
    record = record + "\n"
    fh = open(path, "a")
    fh.write(record)
    fh.close()

# add_employee_to_file("Drake Mikelsson, 19", "employee_list.txt")

# endregion


# region 05
print("Ex.05")


def get_cats_info(path):
    cats_info = []
    return cats_info

# endregion

# region 06

# endregion

# region 07

# endregion

# region 08

# endregion

# region 09

# endregion

# region 10

# endregion

# region 11

# endregion

# region 12

# endregion

# region 13

# endregion

# region 14

# endregion
