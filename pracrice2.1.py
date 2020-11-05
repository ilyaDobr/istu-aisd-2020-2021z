x = float(input("Первое число: "))
oper = (input("Операция: "))
y = float(input("Второе число: "))
def calc(a,  b, op):
    if op == "+":
        print("Результат:", end = " ")
        print (a+b)
    if op == "-":
        print("Результат:", end = " ")
        print (a-b)
    if op == "*":
        print("Результат:", end = " ")
        print (a*b)
    if op == "/" and b == 0:
        print("Деление на ноль!")
    elif op == "/":
        print("Результат:", end = " ")
        print (a/b)
calc(x, y, oper)
input()
