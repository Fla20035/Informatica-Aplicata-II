def problema_1():
    
    
    '''
    1.O companie a stabilit că profitul său anual este de obicei 23 la sută din vânzările totale. 
    Scrieți un program care solicită utilizatorului să introducă suma prevăzută din vânzările totale.
    Afișează profitul care va fi obținut din acea sumă.
    ''' 
    sumaVanzariTotale = int(input("Introduceti suma vanzarilor totale: "))
    profit23_1 = 23/100 * sumaVanzariTotale
    profit23_2 = sumaVanzariTotale - profit23_1
    print(profit23_2)
def problema_2():
    
    
    '''
    2.Presupunând că nu există accidente sau întârzieri:
    O mașină circulă cu 130 de km pe oră. 
    Scrieți un program care afișează următoarele:
        • Distanța pe care o va parcurge mașina în 6 ore
        • Distanța pe care o va parcurge mașina în 10 ore
        • Distanța pe care o va parcurge mașina în 15 ore.
    '''
    
    
    speed = 130
    d6 = str(speed * 6)
    d10 = str(speed * 10)
    d15 = str(speed * 15)
    print("Distanta pe care o va parcurge masina in 6 ore este ->", d6 + " km")
    print("Distanta pe care o va parcurge masina in 10 ore este ->", d10 + " km")
    print("Distanta pe care o va parcurge masina in 15 ore este ->", d15 + " km")    
def problema_3():
    
    
    '''
    O rețetă de prăjituri necesită următoarele ingrediente: 
        •300 gzahăr 
        •230 g unt 
        •360 gfăină
    Rețeta produce 48 de fursecuri cu această cantitate de ingrediente.
    Scrieți un program care întreabă utilizatorul câte fursecuri dorește să faca
    Afișează cantitatea din fiecare ingredient necesar pentru numărul specificat de fursecuri.
    '''
    
    
    fursecuriINPUT = int(input("Cate fursecuri doriti sa faceti ->> "))
    #6,25g zahar/fursec
    #4,79166g unt/fursec
    #7,5g faina/fursec
    zaharFINAL = 6.25 * fursecuriINPUT
    untFINAL = 4.79166 * fursecuriINPUT
    fainaFINAL = 7.5 * fursecuriINPUT
    s = "Ingredientele necesare pentru a face " + repr(fursecuriINPUT) + " fursecuri" +  ": " + repr(zaharFINAL) + "g zahar "  + repr(untFINAL) + "g unt " + repr(fainaFINAL) + "g faina."
    print(s)
def problema_4():
    
 
    '''
    
    
    4.Luna trecută, Joe a achiziționat unele acțiuni în Acme Software, Inc. 
    Iată detaliile achiziției:
        •Numărul de acțiuni cumpăratede Joe a fost de 2.000.
        •Când Joe a achiziționat acțiunile, a plătit 40.00 USD pe acțiune.
        •Joe i-a plătit agentului său un comision care a însumat 3% din suma pe care a plătit-o pentru acțiuni.
    Două săptămâni mai târziu, Joe a vândut acțiunile.
    Iată detaliile vânzării:
        •Numărul de acțiuni pe care Joe le-a vândut a fost de 2.000.
        •A vândut acțiunea cu prețul de 42.75 USD.
        •El a plătit agentului de bursă un comision care s-a ridicat la 3 la sută din suma pe care a primit-o pentru acțiuni.
    Scrieți un program careafișează următoarele informații:
        •Suma de bani pe care Joe a plătit-o pentru acțiuni.
        •Suma comisionului pe care Joe l-a plătitbrokerului când a cumpărat acțiunile.
        •Suma pentru care Joe a vândut acțiunile.
        •Suma comisionului pe care Joe l-a plătit brokerului când a vândut acțiunile.
        •Afișați suma de bani cucare Joe a rămas după vânzareaacțiunilorși și-a plătit brokerul (de ambele ori). 
    !!Dacă această sumă este pozitivă, atunci Joe a făcut un profit. Dacă suma este negativă, atunci Joe a pierdut bani.
    
    
    
    '''
    
    
    actiuniCumparate = 2000
    pretPerActiune_laCumparare = 40
    actiuniVandute = 2000
    pretPerActiune_laVanzare = 42.75
    
    sumaInitiala = actiuniCumparate * pretPerActiune_laCumparare
    sumaFinala = actiuniVandute * pretPerActiune_laVanzare
    
    comisionInitial = 3/100 * sumaInitiala #3% comision
    comisionFinal = 3/100 * sumaFinala #3% comision
    comisionTotal = comisionFinal + comisionInitial
    
    profitJoe = (sumaFinala - comisionTotal) - sumaInitiala
    
    bulletPoint1 = "Suma de bani pe care a platit-o Joe pentru actiuni este -> " + repr(sumaInitiala)
    print(bulletPoint1)
    bulletPoint2 = "Suma comisionului pe care Joe a platit-o brokerului cand a cumparat acitunile este -> " + repr(comisionInitial)
    print(bulletPoint2)
    bulletPoint3 = "Suma pentru care Joe a vandut actiunile este -> " + repr(sumaFinala)
    print(bulletPoint3)
    bulletPoint4 = "Suma comisionului pe care Joe a platit-o brokerului cand a vandut actiunile este -> " + repr(comisionFinal)
    print(bulletPoint4)
    bulletPoint5 = "Profitul lui Joe dupa vanzarea actiunilor este -> " + repr(profitJoe)
    print(bulletPoint5)
    
    if profitJoe > 0 :
        print("Joe a obtinut un profit pozitiv")
    elif profitJoe == 0 :
        print("Joe a stagnat")
    else : 
        print("Joe a iesit pe minus")
def problema_5(): 
    
    '''
    5.Un proprietar de viță de vie plantează mai multe rânduri noi de viță de vie și 
    trebuie să știe câte mladițe de viță de vie să planteze pefiecare rând.
    Ea a stabilit că după măsurarea lungimii unui rând viitor, poate utiliza următoarea formulă pentru a calcula numărul de vițe care se vor potrivi în rând, 
    împreună cu ansamblurile din capetele unui rând care vor trebui construite la fiecare capăt al rândului:
        𝑉=𝑅−2𝐸𝑆
    Termenii din formulă sunt:
        V este numărul de vițede vie care se vorplantape fiecarerând. 
        R este lungimea rândului. E este cantitatea de spațiu folosită de un ansambludin capătului rândului. 
        S este spațiul dintre vița de vie.Scrieți un program care face calculul pentru proprietarul viței de vie. 
    Programul trebuie să solicite utilizatorului să introducă următoarele:
        •Lungimea rândului•Spațiul folosit de un ansamblu
        •Cantitatea de spațiu dintre vița de vieOdată introduse datele de intrare, programul ar trebui să calculeze și să afișeze numărul de vițe de vie 
        care se vor putea planta într-un rând
    '''
    R = int(input("Introduceti lungimea randului ->> "))
    S = int(input("Introduceti vantitatea de spatiu dintre vita de vie ->> "))
    E = int(input("Spatiul folosit de un ansamblu ->> "))
    V = (R - 2*E) / S
    print("Cantitatea este -> " + repr(V))



choice = 3 #just a random number pentru ca python != c++ si nu are swtich case -_-

while choice !=0:
    choice = int(input('''      1.Problema nr1
      2.Problmea nr2
      3.Problmea nr3
      4.Problema nr4
      5.Problema nr5
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
    else:
        print("Please provide a valid option")
        
        





























