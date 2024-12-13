#6. uzdevums

import random

min_skaitlis = 1

max_skaitlis = 100

iedomata_skaitlis = random.randint(min_skaitlis,

max_skaitlis)

print(f"Ludzu uzminet skaitli intervalà no {min_skaitlis}")

minesanas_reizes = 0

while True:

    lietotaja_ievade = int(input("levadi savu minējumu: "))

minesanas_reizes += 1

if lietotaja_ievade < iedomata_skaitlis:

    print("Lielaks!")

elif lietotaja_ievade < iedomata_skaitlis:

    print( "Mazāks!")

else:

        print(f"Uzminēts! Skaitlis ir {iedomata_skaitlis}.")
        break

print(f"Skatijãt minesanu (minesanas_reizes) reizes.")

#2. uzdevums

n = int(input(" ievadi skaitli:"))

summa = 0

    for i in range(1, 1 + n):

    summa += i

    print("skaitļu summa no 1 lidz n ir:", summa)


#3.uzdevums

n = int(input(" ievadi skaitli:"))

faktorials = 1

for i in range(1, 1 + n):

    faktorials *= i

print("skaitļu faktorials no 1 lidz n ir:", faktorials)

#3.uzdevums

n = int(input(" ievadi skaitli:"))

for i in range(n, -1, -1):

    print(i)

