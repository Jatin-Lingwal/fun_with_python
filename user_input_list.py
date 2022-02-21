""" Fun to write a list """


user = int(input("Enter a number which will be length of the list: "))
empty = []
# As length is given above, now user will ask to give
try:
    for i in range(user):
        empty.append(int(input("value/element will be appended to the list:")))
    print(empty)
except ValueError:
    print("you skipped a value")