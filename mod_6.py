from pathlib import Path
import re
import base64
import shutil

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
    with open(path, "r") as cat:
        cats = cat.readlines()
    for c in cats:
        cat_str = c.replace("\n", "").split(",")
        cat_info = {"id": cat_str[0], "name": cat_str[1], "age": cat_str[2]}
        cats_info.append(cat_info)
    return cats_info


# print(get_cats_info("cats.txt"))
# endregion


# region 06
print("Ex.06")


def get_recipe(path, search_id):
    result = {}
    with open(path, "r") as recipes:
        recipe = recipes.readlines()
    for r in recipe:
        rec = r.replace("\n", "").split(",")
        if search_id in rec:
            result["id"] = rec[0]
            result["name"] = rec[1]
            result["ingredients"] = rec[2:]
    if result:
        return result
    else:
        return None


# print(get_recipe("recipes.txt", "60b90c3b13067a15887e1ae4"))
assert get_recipe("recipes.txt", "60b90c3b13067a15887e1ae4") == {'id': '60b90c3b13067a15887e1ae4', 'name': 'Watermelon Cucumber Salad', 'ingredients': [
    '1 large seedless watermelon', '12 leaves fresh mint', '1 cup crumbled feta cheese']}
# endregion


# region 07
print("Ex.07")


def sanitize_file(source, output):
    with open(source, "r") as src:
        text = src.readlines()

    text = "".join(text)
    text = re.sub(r"[0-9]", "", text)

    with open(output, "w") as out:
        out.write(text)
# endregion


# region 08
print("Ex.08")


def save_applicant_data(source, output) -> None:
    result = []

    for i in source:
        app = []
        for v in i.values():
            app.append(str(v))
        app_str = ",".join(app) + "\n"
        result.append(app_str)
        # result.append("\n")

    # result = "\n".join(result)
    with open(output, "w") as out:
        out.writelines(result)


# endregion


# region 09
print("Ex.09")


def is_equal_string(utf8_string, utf16_string):
    return utf8_string.casefold().decode() == utf16_string.casefold().decode("utf-16")

# endregion


# region 10
print("Ex.10")


def save_credentials_users(path, users_info) -> None:
    with open(path, "wb") as us:
        for k, v in users_info.items():
            line = f"{k}:{v}\n"
            us.write(line.encode())


# endregion


# region 11
print("Ex.11")


def get_credentials_users(path):
    with open(path, "rb") as us:
        user_info = us.readlines()
    result = []
    for i in user_info:
        result.append(i.decode().replace("\n", ""))
    return result

# endregion


# region 12
print("Ex.12")


def encode_data_to_base64(data: list):
    encode_list = []
    for i in data:
        message_bytes = i.encode("utf-8")
        base64_bytes = base64.b64encode(message_bytes)
        encode_list.append(base64_bytes.decode("utf-8"))
    return encode_list
# endregion


# region 13
print("Ex.13")


def create_backup(path: Path, file_name: Path, employee_residence: dict):
    with open(path+'/'+file_name, "wb") as file:
        for i, k in employee_residence.items():
            line = f"{i} {k}\n".encode()
            file.write(line)
    return shutil.make_archive("backup_folder", "zip", path)

# endregion

# region 14
print("Ex.14")


def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)
# endregion
