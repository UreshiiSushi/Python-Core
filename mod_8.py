# region import
from datetime import datetime, date
# endregion


# region Ex.01
print("Ex.01")


def get_days_from_today(date: str):
    date_today = datetime.today()
    date = date.split("-")
    date_int = []
    for i in date:
        date_int.append(int(i))
    date_start = datetime(*date_int)
    result = date_today.date() - date_start.date()
    return result.days

# print(get_days_from_today("2020-10-09"))
# endregion


# region Ex.02
print("Ex.02")


def get_days_in_month(month, year):
    first_month = date(year, month, 1)
    if month == 12:
        next_month = date(year+1, 1, 1)
    else:
        next_month = date(year, month+1, 1)
    result = next_month-first_month
    return result.days

# print(get_days_in_month(2, 2000))
# endregion


# region Ex.03
print("Ex.03")

#'Thursday 27 May 2021'
def get_str_date(date:str):
    date = date.split(" ")
    result = []
    for i in date[0].split("-"):
        result.append(int(i))
    result = datetime(*result)
    return result.strftime("%A %d %B %Y")
print(get_str_date("2021-05-27 17:08:34.149Z"))
# endregion


# region Ex.04

# endregion


# region Ex.05

# endregion


# region Ex.06

# endregion


# region Ex.07

# endregion


# region Ex.08

# endregion


# region Ex.09

# endregion


# region Ex.10

# endregion
