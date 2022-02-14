n1 = int(input("enter  1st number: "))
n2 = int(input("enter 2nd number: "))


def num_check(n1, n2):
    if n1 == 20 or n2 == 20 or (n1 + n2) == 20:
        print(True)
    else:
        print(False)

num_check(n1, n2)


