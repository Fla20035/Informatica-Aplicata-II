'''
Proiectați un program care solicită utilizatorului să introducă o serie de 20 de numere. 
Programul trebuie să stocheze numerele dintr-o listă, apoi să afișeze următoarele date:
  •Cel mai mic număr din listă
  •Cel mai mare număr din listă
  •Totalul numerelor din listă
  •Media aritmetică anumerelor din listă
'''
import sys
import random

def problema_1():
    
  lista_numere = []
  counter = 1
  while counter <=5:
    nume = str(input("--> "))
    lista_numere.append(nume)
    counter +=1
  for index in range(0,5):
    print(f"{index+1}. {lista_numere[index]}")


'''
Într-un program, scrieți o funcție numită roll care acceptă un argument number_of_throws. 
Funcția trebuie să genereze și să returneze o listă sortată de numere aleatorii între 1 și 6, care are un număr de elemente  egal  cu number_of_throws.  
Programul  trebuiesă solicite utilizatorului să introducă un număr întreg pozitiv care este transmis la funcție, apoi să afișeze lista returnată.
'''

def problema_2():


  def roll(number_of_throws):
      rolls = [random.randint(1, 6) for _ in range(number_of_throws)]
      return sorted(rolls)

  try:
      number_of_throws = int(input("Introduceti numarul de aruncari: "))
      rolls = roll(number_of_throws)
      print("Lista sortata de aruncari: ", rolls)
  except ValueError:
      print("Introduceti un numar intreg pozitiv.")


'''
Biroul local de licență a șoferului v-a solicitat să creați o aplicație care să noteze examenulscris  din examenul pentru  permisul  de  conducere. 
Examenul are 20 de întrebări tip test grilă. Iată răspunsurile corecte
'''

def problema_3():

  raspunsuri_corecte = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'A', 'D']
  raspunsuri_student = []
  with open ("LAB_6\\raspunsuri_student.txt", "r") as f:
     for line in f:
      print(line.strip())
      raspuns_student = str(input("R:")).upper()
      raspunsuri_student.append(raspuns_student)

  numar_raspunsuri_corecte = 0
  numar_raspunsuri_incorecte = []

  for i in range(20):
    if raspunsuri_student[i] == raspunsuri_corecte[i]:
      numar_raspunsuri_corecte +=1
    else : 
      numar_raspunsuri_incorecte.append(i+1)
  if numar_raspunsuri_corecte >= 15:
    print("Student a trecut cu brio!")
  else:
    print("Ai fost nepregatit!")


  print("Numărul total de întrebări răspuns corect: ", numar_raspunsuri_corecte)
  print("Numărul total de întrebări răspuns incorect: ", 20 - numar_raspunsuri_corecte)
  print("Lista întrebărilor la care s-a răspuns incorect: ", numar_raspunsuri_incorecte)


'''
Se dau următoarele două fișiere:
 •GirlNames.txt: Acest fișier conține o listă cu cele mai populare 200 de nume date fetelor născute în Statele Unite din anii 2000 până în 2009.
 •BoyNames.txt: Acest fișier conține o listă cu cele mai populare 200 de nume date băieților născuți în Statele Unite ale Americii din anul 2000 până în 2009.
Scrieți un program care citește conținutul celor două fișiere în două liste separate. 
Utilizatorul trebuie să poată introduce numele unui băiat, numele unei fete sau ambele, 
iar aplicația va afișa mesaje care indică dacă numele sunt printre cele mai populare.
'''

def problema_4():

  girl_names = []
  boy_names = []

  with open("LAB_6\GirlNames.txt", "r") as fG:
    for line in fG:
      girl_names.append(line.strip())
      
  with open("LAB_6\BoyNames.txt", "r") as fB:
    for line in fB:
      boy_names.append(line.strip())
      

  while True:

    choice = str(input("What do you want to search?(B/G) -- \"Q\" ~to exit or \"BO\" ~ for both genders :: ").upper())

    if choice == "B":
      user_input_boy = str(input("Boy's name to search -> ").upper())
      if user_input_boy in boy_names:
        indexB = boy_names.index(user_input_boy)
        print(f"FOUND IT! ~ {user_input_boy}\n Position - ..{indexB+1}.. ")
      else:
        print("NO MATCHES!")
    elif choice == "G":
      user_input_girl = str(input("Girl's name to search - > ").upper())
      if user_input_girl in girl_names:
        indexG = girl_names.index(user_input_girl)
        print(f"FOUND IT! ~ {user_input_girl}\n Position - ..{indexG+1}..")
      else:
        print("NO MATCHES!")
    elif choice == "BO":
      user_input_both = str(input("Name to search -> ").upper())
      if user_input_both in boy_names:
        indexBO = boy_names.index(user_input_both)
        print(f"FOUND IT! ~ {user_input_both}\n Position - ..{indexBO+1}..")
      elif user_input_both in girl_names:
        indexBO = girl_names.index(user_input_both)
        print(f"FOUND IT! ~ {user_input_both}\n Position - ..{indexBO+1}..")
      else:
        print("NO MATCHES IN BOTH LIST!")
    elif choice == "Q":
      sys.exit()
    else:
      print("Invalid option!")
