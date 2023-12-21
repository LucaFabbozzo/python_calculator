print("Welcome to the calculator", "\N{winking face}")
print("To exit, type Exit")
print("The operations are addition, multi, div and subtraction")

resultado = ""
while True:
    if not resultado:
        resultado = input("Enter number: ")
        if resultado.lower() == "exit":
            break
        resultado = int(resultado)
    op = input("Enter operation ")
    if op.lower() == "exit":
        break
    n2 = input("Enter following number: ")
    if n2.lower() == "exit":
        break
    n2 = int(n2)

    if op.lower() == "addition":
        resultado += n2
    elif op.lower() == "subtraction":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Invalid operation")
        break

    print(f"The result is {resultado}")