# -*- coding: utf-8 -*-
"""
Created on Thu Apr  13 2:15:30 2023

@author: student
"""

import sys
import time

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

  def suma_generata(**locuri_pret):
    suma_A = locuri_pret["A"] * 20
    suma_B = locuri_pret["B"] * 15
    suma_C = locuri_pret["C"] * 10
    return suma_A, suma_B, suma_C

  suma_A, suma_B, suma_C = suma_generata(A=locuri_A, B=locuri_B, C=locuri_C)
  print_dict = {"A": suma_A, "B": suma_B, "C": suma_C}
  

  print_slots(A=locuri_A, B=locuri_B, C=locuri_C)
  print(print_dict)




'''
O firmă de zugrăvit a stabilit că pentru fiecare 112 metri pătrați de perete, este nevoie de un galon de vopsea și opt ore de muncă. 
Compania percepe o taxă de $35.00 pe oră pentru forța de muncă. 
Scrieți un program care solicită utilizatorului să introducă metri pătrați de perete care urmează să fie zugrăvți și prețul vopselei pe galon. 
Programul trebuie să afișeze următoarele date:
  •Numărul de galoane de vopsea necesare
  •Orele de muncă necesare 
  •Costul vopselei
  •Costurile cu forța de muncă!!!!!!!!
  •Costul total al lucrărilor de zugrăvit
'''

#122m^2~perete/3,78541178L(un galon)/8h_munca
#1h/35$

def problema_2():
  metri_patrati = int(input("Cati m^2 de perete sunt :: "))
  pret_vopsea = int(input("Cat costa un galon de vopsea :: "))

  def vopsea__timp(metri_patrati):
    vopsea_necesara = metri_patrati * 3.78541178 / 122          #calculeaza numarul de L necesar de vopsea
    ore_necesare = metri_patrati * 8 / 122                      #calculeaza numarul de ORE necesar pentru x(m^2) 
    return vopsea_necesara, ore_necesare

  vopsea, timp = vopsea__timp(metri_patrati)
  
  def calculeaza_preturi(pret_vopsea, metri_patrati, timp):
    cost_vopsea = metri_patrati * pret_vopsea / 122             #calculeaza pretul vopselei pentru x(m^2) si y(pret/galon)
    cost_forta_munca_H = timp * 35                              #calculeaza costul fortei de munca pentru x(m^2)
    cost_total = cost_vopsea + cost_forta_munca_H
    return cost_vopsea, cost_forta_munca_H, cost_total
  

  cost_vopsea, cost_forta_munca_H, cost_total = calculeaza_preturi(pret_vopsea, metri_patrati, timp)

  print(f"Numarul de litri de vopsea necesari ->> {vopsea:.2f}")
  print(f"Numarul de ore necesare ->> {timp:.2f}")
  print(f"Costul vopselei ->> {cost_vopsea:.2f}")
  print(f"Costurile fortei de munca ->> {cost_forta_munca_H:.2f}")
  print(f"Costul total al lucrarilor ->> {cost_total:.2f}")


'''
Scrieți un program care solicită utilizatorului să introducă cinci punctaje pentru un test. 
Programul trebuie să afișeze o notă pentru fiecare punctaj și nota medie de testare. 
Creați următoarele funcții în program:
  •calc_average. Această funcție trebuie să accepte cinci punctaje de testare ca argumente și să returneze media scorurilor.
  •determine_grade. Această funcție trebuie să accepte un punctaj de testare ca argument și să returneze o literă notă pentru punctaj
'''

def problema_3():
  punctaj_1 = int(input("Introduceti primul punctaj"))
  punctaj_2 = int(input("Introduceti al doilea punctaj"))
  punctaj_3 = int(input("Introduceti al treilea punctaj"))
  punctaj_4 = int(input("Introduceti al patrulea punctaj"))
  punctaj_5 = int(input("Introduceti al cincilea punctaj"))

  def calc_average(punctaj_1, punctaj_2, punctaj_3, punctaj_4, punctaj_5):
    media = (punctaj_1 + punctaj_2 + punctaj_3 + punctaj_4 + punctaj_5) / 5
    return media
  
  medie_clasa = calc_average(punctaj_1, punctaj_2, punctaj_3, punctaj_4, punctaj_5)
  print(f"Media punctajelor de testare este ->> {medie_clasa:.2f}")
  punctaj_testare_grade = int(input("Introduceti un punctaj :: "))

  def determine_grade(punctaj_testare_grade):
    if 90 <= punctaj_testare_grade <= 100: 
      return print(f"---A---")
    elif 80<=punctaj_testare_grade<=89:
      return print(f"---B---")
    elif 70<=punctaj_testare_grade<=79:
      return print(f"---C---")
    elif 60<=punctaj_testare_grade<=69:
      return print(f"---D---")
    elif punctaj_testare_grade < 60:
      return print(f"F")
    else:
      return print("INVALID!")

  determine_grade(punctaj_testare_grade)

'''
Scrieți un program care generează un număr aleatoriu în intervalul de la 1 la 100 și cere utilizatorului să ghicească care este numărul.
Dacă numărul introdus de utilizator  este mai mare decât numărul aleatoriu, programul ar trebui să afișeze “Too high, try again.”.
Dacă numărul introdus de utilizator este mai mic decât numărul aleatoriu, programul ar trebui să afișeze “Too low, try again.”. 
Dacă utilizatorul ghicește numărul, programular trebui să felicite utilizatorul și să genereze un nou număr aleatoriu, astfel încât jocul să poată reîncepe. 
'''

def problema_4():
  import random
  k = 0
  

  def joc_ghicit():
    numar_rand = random.randint(1,10)
    #print(f"Numarul dvs este {numar_rand}")                  ~~~testing
    nr_ghicit = int(input("Introduceti numarul :: "))
    return numar_rand, nr_ghicit

  numar_rand, numar_ghicit = joc_ghicit()

  while True:
    
    if numar_ghicit < numar_rand:
      print("Too low, try again.")
      numar_ghicit = int(input("Introduceti numarul :: "))
      k+=1
    elif numar_ghicit > numar_rand:
       print("Too high, try again.")
       numar_ghicit = int(input("Introduceti numarul :: "))
       k+=1
    else:
      print(f"Congrats! Incercarile dvs ->> {k}.")
      numar_rand, numar_ghicit = joc_ghicit()

'''
Scrieți un program modularizat care permite utilizatorului să joace jocul Rock, Paper, Scissors împotriva computerului.
Programul ar trebui să funcționeze după cum urmează: 
#.Când începe programul, este generat un număr aleatoriu în intervalul de la 1 la 3.
Dacă numărul este 1, atunci computerul a ales Rock. Dacă numărul este 2, computerul a ales Paper.
Dacă numărul este 3, atunci computerul a ales Scissors. (Nu afișați încă alegerea computerului.)
##.Utilizatorul introduce alegerea sa „rock”, „paper” sau „scissors” de la tastatură. 
###.Opțiunea computerului este afișată. 
####.Un câștigător este selectat conform următoarelor reguli: 
  •Dacă un jucător alege rock și celălalt alege scissors, atunci rock câștigă.(Rock smashes scissors.)
  •Dacă un jucător alege scissors, iar celălalt alege paper, scissors câștigă. (Scissors cuts paper.)
  •Dacă un jucător alege paper, iar celălalt alege rock, atunci paper câștigă. (Paper wraps rock.) 
  •Dacă ambii jucători fac aceeași alegere, jocul trebuie jucat din nou pentru a determina câștigătorul
'''

def problema_5():
  import random
  import time

  

  def game():
    alegere_calculator = random.randint(1,3)
    print("Loading...")
    time.sleep(1.3)
    print("1.rock")
    time.sleep(0.3)
    print("2.paper")
    time.sleep(0.3)
    print("3.scissors")
    time.sleep(0.3)

    alegere_jucator = int(input("Alegeti urmatoarea miscare (1,2,3) :: "))
    
    if alegere_calculator == 1:
     print("computer's choice - rock!")
    elif alegere_calculator == 2:
     print("computer's choice - paper!")
    else:
     print("computer's choice - scissors!")
    return alegere_calculator, alegere_jucator

  alegere_calculator, alegere_jucator = game()

  while True:
    if alegere_jucator == alegere_calculator:
      time.sleep(1.5)
      print("---DRAW---")
      time.sleep(1)
      print("3...")
      time.sleep(1)
      print("2...")
      time.sleep(1)
      print("1...")
      time.sleep(1)
      alegere_calculator, alegere_jucator = game()
    elif alegere_jucator == 1 and alegere_calculator == 3:
      time.sleep(1.5)
      print("---YOU WIN---")
      break 
    elif alegere_jucator == 2 and alegere_calculator == 1:
      time.sleep(1.5)
      print("---YOU WIN---")
      break
    elif alegere_jucator == 3 and alegere_calculator == 2:
      time.sleep(1.5)
      print("---YOU WIN---")
      break
    else:
      time.sleep(1.5)
      print("---YOU LOST---")
      break


'''
Scrieți o funcție recursivă care acceptă un argument întreg, n.
Funcția trebuie să afișeze n linii de steluțe pe ecran, cu prima linie care arată 1 steluță, a doua linie care prezintă 2 steluțe, până la a n linie care arată n steluțe.
'''

def problema_6():

  def afisare_stelute(n):
    if n == 0:
        return
    afisare_stelute(n-1)
    print("*" * n)

  afisare_stelute(3)

'''
Implementați o funcție recursivă care acceptă un argument întreg n, și tipărește fiecare al doilea număr de la n până la minimum 0. 
Presupunem că n este întotdeauna un număr întreg pozitiv.
'''

def problema_7():
  def din_doi_in_doi(n):
    if n < 0:
        return
    if n % 2 == 0:
        print(n)
    din_doi_in_doi(n-2)

  din_doi_in_doi(10)


choice = 3 #just a random number pentru ca python != c++ si nu are swtich case -_-

while choice !=0:
    choice = int(input('''      1.Problema nr1
      2.Problmea nr2
      3.Problmea nr3
      4.Problema nr4
      5.Problema nr5
      6.Problema nr6
      7.Problema nr7
      0.EXIT
      '''))
    
    if choice == 1:
        problema_1()
    elif choice == 2:
        problema_2()
    elif choice == 3:
        problema_3()
    elif choice == 4:
        problema_4()
    elif choice == 5:
        problema_5()
    elif choice == 6:
        problema_6()
    elif choice == 7:
        problema_7()
    elif choice == 0:
        sys.exit("      Exiting...")
        time.sleep(1.5)
    else:
        print("Please provide a valid option")
        