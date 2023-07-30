#region Ex.1
# 
# def greeting():
    # print("Hello world!")
# 
# greeting()
#endregion

#region Ex. 2
# def invite_to_event(username):
#     return f"Dear {username}, we have the honour to invite you to our event."

# name = input("Enter your name: ")
# print(invite_to_event(name))
#endregion

#region Ex. 3
# base_rate = 40
# price_per_km = 10
# total_trip = 0
# 
# 
# def calculate_trip_price(distance_km):
    # global total_trip 
    # total_trip += 1
    # return base_rate + price_per_km*distance_km
# 
# distance = float(input("Enter a distance in km: "))
# print(calculate_trip_price(distance))
# print(total_trip)
    # 
#endregion

#region Ex. 4
# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price = price*(1 - discount)
#     apply_discount()
#     return price
#endregion

#region Ex. 5
# def get_fullname(first_name, last_name, middle_name = ''):
#     if middle_name:
#         return f"{first_name} {middle_name} {last_name}"
#     else:
#         return f"{first_name} {last_name}"
#endregion

#region Ex. 6
# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         string = " "*((length - len(string))//2) + string
#         return string
    
# in_string = input("String: ")
# in_len = int(input("Length: "))
# print(format_string(in_string, in_len))
#endregion

#region Ex. 7
# def first(size, *position):
#     return size + len(position)
# def second(size, **keys):
#     return size + len(keys)
# print(first(5, "first", "second", "third"))
# print(first(1, "Alex", "Boris"))
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))
# print(second(10, comment_one="Alex", comment_two="Boris"))
#endregion

#region Ex. 8
# def cost_delivery(quantity, *_, discount = 0):
#     if not discount:
#         return 5 + 2*(quantity-1)
#     else:
#         return (5 + 2*(quantity - 1))*(1 - discount)

# print(cost_delivery(2, 1, 2, 3))
# print(cost_delivery(3, 3))
# print(cost_delivery(1))
# print(cost_delivery(2, 1, 2, 3, discount=0.5))
#endregion

#region Ex. 9
# def cost_delivery(quantity, *_, discount=0):
#     """Функція повертає суму за доставлення замовлення.

#      Перший параметр &mdash; кількість товарів в замовленні.
#      Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""
#     result = (5 + 2 * (quantity - 1)) * (1 - discount)
#     return result

# print(cost_delivery.__doc__)
#endregion

#region Ex. 10
# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n*factorial(n-1)

# def number_of_groups(n, k):
#     return int(factorial(n)/(factorial(n-k)*factorial(k)))

# print(number_of_groups(50, 7))
#endregion

#region Ex. 11
def fibonacci(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

print(fibonacci(10))
#endregion 
