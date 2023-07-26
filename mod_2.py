
# ex.10
# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num:
    # for i in range(1, num+1):
        # sum += i
    # num = int(input("Enter integer (0 for output): "))
# print(sum)


# Ex. 11
# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if not num:
#         break
#     for i in range(num + 1):
#         sum = sum + i
# print(sum)

# Ex. 12

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

# Ex. 13

message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    
