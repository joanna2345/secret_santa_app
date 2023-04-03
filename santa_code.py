from sys import exit
from os import system
from random import shuffle
from time import sleep

lista_imion = []
lista_losujacych = []

while True:
    czy_dodac = input('Czy chcesz dodać imię do listy? (t/n)')
    if czy_dodac == 't':
        do_dodania = str.capitalize(str.strip(input('Podaj imię: ')))
        if do_dodania in lista_imion:
            print('Podane imie znajduje się już na liście. Podaj wartość unikatową.')
        elif len(do_dodania) == 0:
            print('Należy podać imię.')
        else:
            lista_imion.append(do_dodania)
    elif czy_dodac == 'n':
        #jesli długość listy jest mniejsza niz 3 osoby
        if len(lista_imion) <3: 
            while True:
                print('Lista jest za krótka, aby móc losować osoby.')
                czy_zakonczyc = input('Czy chcesz zakończyć działanie programu? (t/n): ')
                if czy_zakonczyc == 't':
                    exit(0) #zamknij program
                elif czy_zakonczyc == 'n':
                    break
                else:
                    system('cls')
                    print('Podano nieprawidłową wartość.')
        else:
            break
    else:
        system('cls')
        print('Podano nieprawidłową odpowiedź.')
# print(lista_imion) #spr
shuffle(lista_imion) #miesza kolejnosc na liscie
# print(lista_imion) #spr

for i in range(len(lista_imion)):
    if i != len(lista_imion) -1: #jeżeli jest różne od ostatniego elementu
        lista_losujacych.append(lista_imion[i+1]) #dodaje to co na indeksie drugim
    else:
        lista_losujacych.append(lista_imion[0])
# print(lista_imion) spr
# print(lista_losujacych) z tym spr

mikolaj = {} #slownik mikolaj

# parujemy elementy w slowniku
for i in range(len(lista_imion)):
    mikolaj[lista_imion[i]] = lista_losujacych[i] 
    
lista_do_wyswietlenia = list(mikolaj.items())

shuffle(lista_do_wyswietlenia)
# print(lista_do_wyswietlenia) #spr z tym

for i in range(len(lista_do_wyswietlenia)):
    system('cls')
    input('Naciśnij Enter, aby kontynuować.') #
    system('cls')
    print('Teraz losować będzie', lista_do_wyswietlenia[i][0])
    input('Nacisnij Enter, aby kontynuować. Upewnij się, że osoby nielosujące nie patrzą na ekran. ')
    print(lista_do_wyswietlenia[i][0], 'kupujesz prezent dla', lista_do_wyswietlenia[i][1])
    input('Naciśnij Enter, aby kontynuować.')
system('cls')
print('To już wszyscy ;)')
sleep(5) #5sek komunikat
