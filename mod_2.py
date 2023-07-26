
#region ex.10
# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num:
    # for i in range(1, num+1):
        # sum += i
    # num = int(input("Enter integer (0 for output): "))
# print(sum)
#endregion


#region Ex. 11
# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if not num:
#         break
#     for i in range(num + 1):
#         sum = sum + i
# print(sum)
#endregion

#region Ex. 12
# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     for i in range(num + 1):
#         if i%2 == 1:
#             continue
#         sum += i
# print(sum)
#endregion

#region Ex. 13

# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# for ch in message:
#     num = ord(ch)
#     if num in (range(32, 65) or range(91, 97) or range(123, 127)) :
#         encoded_message += chr(num)
#     elif num in range(65, 91):
#         pos = ord(ch) - ord('A')
#         pos = (pos + offset)%26
#         encoded_message += chr(pos + ord('A'))
#     else:
#         pos = ord(ch) - ord('a')
#         pos = (pos + offset)%26
#         encoded_message += chr(pos + ord('a'))
# print(encoded_message)
#endregion

#region Ex. 14

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity
# except ZeroDivisionError:
#     print('Divide by zero completed!')
# else:
#     print(chunk)
#endregion

#region Ex. 15

result = None
operand = None
operator = None # + - * /
wait_for_number = True

while True:
    user_input = input()
    if user_input == '=':
        print('Result: '+ str(result))
        break
    if wait_for_number: #waiting for operand
        try:
            operand = int(user_input)
        except ValueError:
            print(user_input + ' not a number. Try again')
            continue
        if not result:
            result = operand
        else:
            match operator:
                case '+':
                    result = result + operand
                case '-':
                    result = result - operand
                case '*':
                    result = result * operand
                case '/':
                    try:
                        result = result / operand
                    except ZeroDivisionError:
                        print('Division by zero is restricted. Try again')
                        continue
        wait_for_number = False
    else: #waiting for operator
        if user_input in ['+', '-', '*', '/']:
            operator = user_input
            wait_for_number = True
        else:
            print(user_input + " not + or - or * or /. Try again")
            continue

#endregion
