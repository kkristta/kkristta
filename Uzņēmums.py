from darbinieks import Darbinieks



class Uznemums:

    def __init__(self, nosaukums):

        self.nosaukums = nosaukums

self.darbinieki = []



def pievienot_darbinieku(self, darbinieks):

    self.darbinieki.append(darbinieks)



def paradit_visus_darbiniekus(self):

    for darbinieks in self.darbinieki:

        print(darbinieks)



    def augstaka_alga(self):

if not self.darbinieki:

        return None

    return max(self.darbinieki, key=lambda d: d.salary)




uznemums = Uznemums("Mana Firma")





darbinieks1 = Darbinieks("Krists", "Kalniņ", 1200)

darbinieks2 = Darbinieks("Jānis", "Bērziņš", 1500)

darbinieks3 = Darbinieks("Elīna", "Liepa", 1000)





uznemums.pievienot_darbinieku(darbinieks1)

uznemums.pievienot_darbinieku(darbinieks2)

uznemums.pievienot_darbinieku(darbinieks3)





print("Darbinieki uzņēmumā:")

for darbinieks in uznemums.darbinieki:

print(darbinieks)





print("\nAlgu izmaiņas:")





darbinieks1.increase_salary(10)

print(f"Pēc algas palielināšanas: {darbinieks1}")





darbinieks2.decrease_salary(5)

print(f"Pēc algas samazināšanas: {darbinieks2}")




augstakais = uznemums.augstaka_alga()

print(f"\nDarbinieks ar augstāko algu: {augstakais.name} {augstakais.surname} ar algu {augstakais.salary:.2f} EUR")