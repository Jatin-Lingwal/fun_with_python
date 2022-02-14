n1 = int(float(input("Enter first digit: ")))
n2 = int(float(input("Enter second digit: ")))
operator = input("+, *, -, / :")
def calculator(n1, n2):

    if operator == "+":
        result = (n1 + n2)
        return result

    elif operator == "-":
        result = (n1 - n2)
        return result

    elif operator == "/":
        result = (n1 / n2)
        return result

    elif operator == "*":
        result = (n1 * n2)
        return result
    else:
        print("Invalid")


result = calculator(n1, n2)
print(result)
