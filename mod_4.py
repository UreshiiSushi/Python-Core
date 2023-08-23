#region Ex. 1
# def amount_payment(payment):
#     sum_pay = 0
#     for i in payment:
#         if i > 0:
#             sum_pay += i
#     return sum_pay
#endregion

#region Ex. 2
# def prepare_data(data):
#     data.sort()
#     data.pop()
#     data.pop(0)
#     return data
    
# test_list = [1, -3, 4, 100, 0, -5, 10, 1, 1]
# print(prepare_data(test_list))
#endregion

#region Ex. 3
# def format_ingredients(items):
    
#     if len(items) == 0:
#         return "No ingridients"
#     else:
#         ingridients = items[0]
#     if len(items) == 1:
#         return ingridients
#     elif len(items) == 2:
#         ingridients = ingridients + " and "+ items[-1]
#     else:
#         for i in items[1:-1]:
#             ingridients = ingridients + ", " + i
#         ingridients = ingridients + " and "+ items[-1]
#     return ingridients
# print(format_ingredients([]))
#endregion

#region Ex. 4
# def get_grade(key):
#     grades = {"F": 1, "FX" : 2, "E" : 3, "D" : 3, "C" : 4, "B" : 5, "A" : 5}
#     return grades.get(key)


# def get_description(key):
#     grades = {"F": "Unsatisfactorily", "FX" : "Unsatisfactorily", "E" : "Enough", "D" : "Satisfactorily", "C" : "Good", "B" : "Very good", "A" : "Perfectly"}
#     return grades.get(key)
# print(get_description("A"))
# print(get_grade("C"))
#endregion

#region Ex. 5
# def lookup_key(data, value):
#     key_list = []
#     for k, v in data.items():
#         if v == value:
#             key_list.append(k)
#     return key_list
# lang = {"Python": 1991, "Java": 1995, "JS": 1995}
# print(lookup_key(lang, 1995))
#endregion

#region Ex. 6
# def split_list(grade = []):
#     if len(grade) > 0 :
#         Sum = sum(grade)
#         average = Sum / len(grade)
#         lesser = []
#         greater = []
#         for i in grade:
#             if i <= average:
#                 lesser.append(i)
#             else:
#                 greater.append(i)
#         return lesser, greater
#     else:
#         return ([], [])
    
# print(split_list([1, 12, 3, 24, 5]))
#endregion

#region Ex. 7
# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }

# def calculate_distance(coordinates) -> float:
#     distance = 0.0
#     for i in range(0, (len(coordinates)-1)):
#         coord = [coordinates[i], coordinates[i+1]]
#         distance += points[tuple(sorted(coord))]
#     return distance

# print(calculate_distance([0, 1, 3, 2, 0]))
#endregion

#region Ex. 8
# def game(terra, power):
#     res_power = power
#     for i in terra:
#         for j in i:
#             if j <= res_power:
#                 res_power += j
#             else:
#                 break
#     return res_power


# print(game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 2))
#endregion

#region Ex. 9
print('Ex. 09:')
def is_valid_pin_codes(pin_codes: list) -> bool:
    if not len(pin_codes):
        return False
    pin_set = set(pin_codes)
    if len(pin_codes) != len(pin_set):
        return False
    else:
        for i in pin_codes:
            if (len(i) == 4) and (type(i) == 'str') and (set(i) in set('1234567890')):
                continue
            else:
                return False
    return True
            
                
            
print(is_valid_pin_codes(['1101', '9034', '0011']), end='\n')

#endregion

#region Ex. 10

#endregion
#region Ex. 11

#endregion
#region Ex. 12

#endregion
#region Ex. 13

#endregion
#region Ex. 14

#endregion