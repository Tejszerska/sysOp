
def kalkulator():
    print("Prosty Kalkulator")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wprowadź numer operacji (1/2/3/4): ")

    if wybor in ['1', '2', '3', '4']:
        try:
            liczba1 = float(input("Wprowadź pierwszą liczbę: "))
            liczba2 = float(input("Wprowadź drugą liczbę: "))

            if wybor == '1':
                wynik = liczba1 + liczba2
                print(f"Wynik dodawania: {wynik}")
            elif wybor == '2':
                wynik = liczba1 - liczba2
                print(f"Wynik odejmowania: {wynik}")
            elif wybor == '3':
                wynik = liczba1 * liczba2
                print(f"Wynik mnożenia: {wynik}")
            elif wybor == '4':
                if liczba2 != 0:
                    wynik = liczba1 / liczba2
                    print(f"Wynik dzielenia: {wynik}")
                else:
                    print("Błąd: Dzielenie przez zero jest niedozwolone.")
        except ValueError:
            print("Błąd: Wprowadzono nieprawidłową liczbę.")
    else:
        print("Błąd: Wybrano nieprawidłową operację.")

# Uruchomienie kalkulatora
kalkulator()
