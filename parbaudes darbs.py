
k = int(input('Enter k: '))
print(k)
r = input('Enter r: ')
print(r)
m = float(input('Enter m: '))
print(m)

try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
except ValueError:
    print('a or b = int')
x1 = a + b
x2 = a - b
x3 = a * b
x4 = a / b
x5 = a ** b

try:
    n = int(input('ievadi skaitli: '))
except ValueError:
    print('n = int')
if n == 1:
    print("skaitlis ir nepāra")
if (n % 2) == 0:
    print("skaitlis ir pāra ")
if n == 0:
    print("skaitlis - nulle")

    Atzime = int(input("Ievadiet Atzimi:"))
if 9 <= Atzime <= 10:
    print("Atzime: A")
if 7 <= Atzime < 8:
    print("Atzime: B")
if 6 <= Atzime < 7:
    print("Atzime: C")
if 5 <= Atzime < 6:
    print("Atzime: D")
if 4 <= Atzime < 5:
    print("Atzime: E")
if 0 <= Atzime < 4:
    print("Atzime: F")
if 0 < Atzime > 10:
    print("Nepareiza atzime! Ievadiet skaitli no 0 lidz 10")

