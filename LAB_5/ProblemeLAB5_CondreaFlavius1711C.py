import sys
import time
import random
import os

'''
Scrieți un program care citește și salvează într-un fișier numere.txt o serie de numere întregi. 
Utilizați fișierul create pentru a scrieun program care calculează media arithmetică a tuturor  numerelor stocate în fișier.
'''

def problema_1():
    while True:
        try:
            filename = input("Numele fisierului (nu uitati de formatul acestuia .txt):: ") #.txt la final!
            with open(filename, 'w') as file:
                break
        except IOError:
            print("Eroare la deschiderea fisierului! Verificati daca numele fisierului este corect sau daca aveti permisiunea necesara.")
    
    numbers = []
    while True:
        try:
            num = input("Introduceti un numar(sau 'q' ca sa iesiti):: ")
            if num == 'q':
                break
            numbers.append(int(num))
        except ValueError:
            print("Valoarea introdusa nu este un numar intreg!")
    
    try:
        with open(filename, 'w') as file:
            for num in numbers:
                file.write(f"{num}\n")
    except IOError:
        print("Eroare la scrierea in fisier!")
    
    def medie_lista(numbers):
        return sum(numbers) / len(numbers)
    
    try:
        average = medie_lista(numbers)
        print("Media aritmetica a numerelor din fisier este = ", round(average, 2))
        with open(filename, 'a') as file:
            file.write(f"Media aritmetica a numerelor de mai sus este ->> {average}\n\n\n")
    except (ValueError, ZeroDivisionError, IOError):
        print("Eroare la prelucrarea datelor!")

'''
Scrieți un program care citește și salvează într-un fișier numit score.txt, o serie de înregistrări, fiecare cu două câmpuri: 
un nume, urmat de un punctaj (un număr întreg între 1 și 100). 
Utilizați fișierul create pentru a scrieun program care afișează numele și punctajul înregistrării cu cel mai mare scor, precum și numărul de înregistrări din fișier.
'''

def problema_2():

    inregistrari = int(input("Cate inregistrari sunt :: "))
    with open("score.txt", "w")as f:
        for count in range(inregistrari):
           nume = str(input("nume ::\t\t--\t\t"))
           punctaj = int(input("punctaj ::\t\t--\t\t"))
           f.write(f"{nume}\t--\t{punctaj}\n")

    with open("score.txt", "r") as f:
        records = [tuple(line.strip().split("\t--\t")) for line in f.readlines()]
        max_record = max(records, key=lambda record: int(record[1]))
        print("Cel mai mare punctaj este:", max_record[1])
        print("Obtinut de:", max_record[0])


'''

'''

def problema_3():

    nr_cuvinte = int(input("Cate cuvinte doresti sa scrii in fisier? "))
    cuvinte = []
    for i in range(nr_cuvinte):
        cuvant = input(f"Introdu cuvantul {i+1}: ")
        cuvinte.append(cuvant)
    with open("words.txt", "w") as f:
        for cuvant in cuvinte:
            f.write(cuvant + "\n")
    choice = str(input("Doriti sa continuati si cu problema 4 (Y/N) ? :: ").lower())

    def problema_4(nr_cuvinte, cuvinte, cuvant):
        print(f"Numarul de cuvinte ->> {nr_cuvinte}")
        cuvant_lung = max(cuvinte, key=len)
        print(f"Cel mai lung cuvant din lista este ->> {cuvant_lung}")
        average = sum(len(cuvant) for cuvant in cuvinte) / nr_cuvinte
        print(f"Media lungimii cuvintelor este ->> {average}")

    if choice == 'y':
        problema_4(nr_cuvinte, cuvinte, cuvant)
    elif choice == 'n':
        sys.exit()
    else:
        print("INVALID")
        time.sleep(2)
        sys.exit()

choice = 3 #?

while choice !=0:
    choice = int(input('''      1.Problema nr1
      2.Problmea nr2
      3.Problmea nr3
      0.EXIT
      '''))
    
    if choice == 1:
        problema_1()
    elif choice == 2:
        problema_2()
    elif choice == 3:
        problema_3()
    elif choice == 0:
        sys.exit("      Exiting...")
        time.sleep(1.5)
    else:
        print("Please provide a valid option")
