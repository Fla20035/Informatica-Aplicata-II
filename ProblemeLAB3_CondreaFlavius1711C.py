# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 11:55:16 2023

@author: student
"""
'''
Scrieți un program care solicită utilizatorului să introducă o lună, ca număr întreg între 1 și 12. 
Programul  trebuie să afișeze un mesaj care să indice dacă luna este în primul trimestru, al doilea trimestru, al treilea trimestru
sau al patrulea trimestru al anului. 
Urmează indicațiile:
  •Dacă utilizatorul introduce 1, 2, sau 3, luna este în primul trimestru. 
  •Dacă utilizatorul introduce un număr între 4 și 6, luna este în al doilea trimestru. 
  •Dacă numărul este 7, 8, sau 9, luna este în trimestrul al treilea. 
  •Dacă luna este cuprinsă între 10 și 12, luna este în al patrulea trimestru. 
  •Dacă numărul nu este între 1 și 12, programul ar trebui să afișeze o eroare.
'''


def problema_1():
  month = int(input("Introduceti luna ->> "))
  if 1 <= month <=3:
    print("Esti in primul semestru.")
  elif 4 <= month <=6:
    print("Esti in al doilea semestru.")
  elif 7 <= month <=9:
    print("Esti in al treilea semestru.")
  elif 10 <= month <=12:
    print("Esti in al patrulea semestru")
  else:
    print("Nu ai introdus luna corecta!")


'''
Figura1 prezintă o diagramă de flux simplificată pentru depanarea unei conexiuni Wi-Fi  defecte. 
Folosiți organigrama pentru a crea un program care să conducă o persoană prin etapele de remediere a unei conexiuni Wi-Fi proaste.
'''


def problema_2():
    while True:
        print("Reboot the computer and try to connect.")
        try:
            answer = input("Did that fix the problem? (Y/N)").upper()
        except ValueError:
            print("Invalid input. Please enter 'Y' or 'N'.")
            continue
        
        if answer == 'Y':
            return
        
        print("Reboot the router and try to connect...")
        try:
            answer = input("Did that fix the problem? (Y/N)").upper()
        except ValueError:
            print("Invalid input. Please enter 'Y' or 'N'.")
            continue
        
        if answer == 'Y':
            return
        
        print("Make sure the cables between the router & modem are plugged in firmly...")
        try:
            answer = input("Did that fix the problem? (Y/N)").upper()
        except ValueError:
            print("Invalid input. Please enter 'Y' or 'N'.")
            continue
        
        if answer == 'Y':
            return 
        
        print("Move the router to a new location and try to connect...")
        try:
            answer = input("Did that fix the problem? (Y/N)").upper()
        except ValueError:
            print("Invalid input. Please enter 'Y' or 'N'.")
            continue
        
        if answer == 'Y':
            return
        
        print("Get a new router.")
        return


'''
Presupunând că nivelul oceanului crește în prezent cu aproximativ 1,6 milimetri pe an.
Creați o aplicație care afișează numărul de milimetri cucare oceanul va crește în fiecare an în următorii 25 de ani.
'''


def problema_3():
   
   crestereNivelPerAn = 1.6
   totalPerAn = 0

   for i in range(25):
      totalPerAn+=crestereNivelPerAn
      print(f"{i}. {totalPerAn:0,.1f} mm")


'''
La  un  colegiu, taxa  de școlarizare  pentru  un  student cu normă întreagă este de 8.000 de dolari pe semestru.
S-a anunțat că taxa de școlarizare va crește cu 3% în fiecare an pentru următorii 5 ani.
Scrieți un program cu o instrucțiune repetitivă care afișează suma semestrială pentru următorii 5 ani.
'''


def problema_4():
   
  taxa_scolarizare_an = 8000
  for i in range(5):
    total_per_semestru = taxa_scolarizare_an + (0.03*taxa_scolarizare_an)
    taxa_scolarizare_an = total_per_semestru
    print(f"Anul {i+1} - >> {total_per_semestru:0,.2f}")


'''
Planul de credit de la TidBit Computer Store specifică o plată în avans de 10% și o rată anuală a dobânzii de 12%. 
Plățile lunare reprezintă 5% din prețul de cumpărare listat, minus avansul. Scrieți un program  care primește la intrare prețul de achiziție. 
Programul  trebuiesă afișeze un tabel, cu anteturile corespunzătoare, a unui program de plată pe durata de viață a împrumutului. 
Fiecare rând al tabelului trebuie să conțină următoarele elemente:
    •numărul lunii (începând cu 1) 
    •soldul total curent datorat 
    •dobânda datorată pentru luna respectivă 
    •sumade capitaldatoratăpentru luna respectivă 
    •plata pentru luna respectivă 
    •sold rămas după platăSuma dobânzii pentru o lună este egală cu soldul * rata/ 12.
Suma de capital pentru o lună este egală cu plata lunară minus dobânda datorată.
'''

def problema_5():
    pret_achizitie = int(input("Care este pretul produsului? ")) 
    plata_avans10 = 0.1 * pret_achizitie 
    pret_fara_avans = pret_achizitie - plata_avans10
    pret_fara_avans_cu_dobanda = 1.12 * pret_fara_avans #pretul cu dobanda
    rata_lunara = 0.05 * pret_fara_avans
    dob_lunara = pret_fara_avans_cu_dobanda * 0.01 / 12
    sold_datorat = pret_fara_avans_cu_dobanda
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Luna", "Sold Datorat", "Dobanda Lunara", "Suma de Capital", "Plata Lunara", "Sold Ramas"))
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "-"*10, "-"*20, "-"*20, "-"*20, "-"*20, "-"*20))
    for luna in range(1, 13):
        dob_lunara = sold_datorat * 0.01 / 12
        capital_lunar = rata_lunara - dob_lunara
        plata_lunară = rata_lunara + capital_lunar
        sold_datorat -= capital_lunar
        print("{:<10} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f}".format(
            luna, sold_datorat, dob_lunara, capital_lunar, plata_lunară, sold_datorat))

while True:
    print("Selectati o optiune:")
    print("1. Problema 1")
    print("2. Problema 2")
    print("3. Problema 3")
    print("4. Problema 4")
    print("5. Problema 5")
    print("0. Exit")
    option = input("Introduceti numarul optiunii: ")
    
    if option == "1":
        problema_1()
    elif option == "2":
        problema_2()
    elif option == "3":
        problema_3()
    elif option == "4":
        problema_4()
    elif option == "0":
        break
    else:
        print("Va rog introduceti o optiune valida.")
