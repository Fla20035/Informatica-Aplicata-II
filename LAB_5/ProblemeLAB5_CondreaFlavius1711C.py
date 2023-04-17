import sys
import time
import random

'''
Scrieți un program care citește și salvează într-un fișier numere.txt o serie de numere întregi. 
Utilizați fișierul create pentru a scrieun program care calculează media arithmetică a tuturor  numerelor stocate în fișier.
'''

def problema_1():
    with open ('numere.txt', 'r') as f :
        lista_numere = [line.strip() for line in f] 
        print(lista_numere)
    
 
problema_1()