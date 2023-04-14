# -*- coding: utf-8 -*-
"""
Created on Thu Apr  13 2:15:30 2023

@author: student
"""

'''
Pe un stadion există trei categorii de locuri.
Locurile din clasa A costă 20 dolari, locurile din clasa B costă 15 dolari, iar locurile din clasa C costă 10 dolari.
Scrieți un program modularizat care  solicităutilizatorului  introducerea  numărului  de  bilete  vândute  din  fiecare  clasă
apoi  afișează  suma veniturilor generate din vânzarea biletelor.Utilizati funcții pentru a rezolva problema.
'''

def problema_1():

  def print_slots(**locuri_ocupate):
    print(f"Locurile ocupate sunt ::  {locuri_ocupate}")

  locuri_A = int(input("Cate locuri de tip \"A\" au fost vandute ->> "))  
  locuri_B = int(input("Cate locuri de tip \"B\" au fost vandute ->> "))
  locuri_C = int(input("Cate locuri de tip \"C\" au fost vandute ->> "))

  suma_A, suma_B, suma_C = suma_generata(A=locuri_A, B=locuri_B, C=locuri_C)
  print_dict = {"A": suma_A, "B": suma_B, "C": suma_C}
  

  print_slots(A=locuri_A, B=locuri_B, C=locuri_C)
  print(print_dict)

def suma_generata(**locuri_pret):
  suma_A = locuri_pret["A"] * 20
  suma_B = locuri_pret["B"] * 15
  suma_C = locuri_pret["C"] * 10
  return suma_A, suma_B, suma_C

problema_1()
