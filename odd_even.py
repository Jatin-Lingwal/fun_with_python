"""Creating a function to know whether a number is even or odd. If both the numbers are even then
=>(smaller number) but any number is odd then => (larger number)"""

n1 = int(input("Enter any number: "))
n2 = int(input("Enter any number: "))


def num_to_know(n1, n2):
    if n1 %2 == 0 and n2 % 2 == 0:
        print(f'min value: {min(n1,n2)}')
    else:
        print(f'max value: {max(n1, n2)}')

num_to_know(n1, n2)









