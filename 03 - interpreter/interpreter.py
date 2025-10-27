expression = input("Expression: ")
if "+" in expression:
    n1, n2 = expression.split("+")
    n1 = float(n1)
    n2 = float(n2)
    result = n1 + n2
elif "-" in expression:
    n1, n2 = expression.split("-")
    n1 = float(n1)
    n2 = float(n2)
    result = n1 - n2
elif "*" in expression:
    n1, n2 = expression.split("*")
    n1 = float(n1)
    n2 = float(n2)
    result = n1 * n2
elif "/" in expression:
    n1, n2 = expression.split("/")
    n1 = float(n1)
    n2 = float(n2)
    result = n1 / n2
    
print(result)  