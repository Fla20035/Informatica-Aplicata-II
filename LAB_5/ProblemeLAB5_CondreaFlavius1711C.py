import sys
import time
import random
import os

'''
Scrieți un program care citește și salvează într-un fișier numere.txt o serie de numere întregi. 
Utilizați fișierul create pentru a scrieun program care calculează media arithmetică a tuturor  numerelor stocate în fișier.
'''

def problema_1():


    filename = input("Numele fisierului (nu uitati de formatul acestuia .txt):: ") #.txt la final!


    numbers = []
    while True:
        num = input("Introduceti un numar(sau 'q' ca sa iesiti):: ")
        if num == 'q':
            break
        numbers.append(int(num))

    with open(filename, 'w') as file:
        for num in numbers:
            file.write(f"{num}\n")

    def medie_lista(numbers):
        return sum(numbers) / len(numbers)
    
    average = medie_lista(numbers)
    print("Media aritmetica a numerelor din fisier este = ", round(average, 2))

    with open(filename, 'a') as file:
        file.write(f"Media aritmetica a numerelor de mai sus este ->> {average}\n\n\n")


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

    def problema_4(nr_cuvinte):
        print(nr_cuvinte)

    if choice == 'y':
        problema_4(nr_cuvinte)
    elif choice == 'n':
        sys.exit()
    else:
        print("INVALID")
        time.sleep(2)
        sys.exit()
    


problema_3()