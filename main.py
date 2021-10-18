def menu():
    print("1. Citirea unei liste de numere intregi")
    print("2. Afisarea listei dupa eliminarea duplicatelor")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. Iesire")
    print("0. Afisare lista")


def citire_lista():
    l = []
    given_string = input("Dati lista de numere, cu numerele separate printr-o virgula: ")
    numbers_as_string = given_string.split(',')
    for x in numbers_as_string:
        l.append(int(x))
    return l


def eliminare_duplicate(l):
    '''
    Elimina duplicatele dintr-o lista
    :param l: o lista de intregi
    :return: lista l, dupa ce a eliminat duplicatele
    '''
    rezultat = []
    for x in l:
        ok = 0
        for y in rezultat:
            if x==y:
                ok = 1
        if ok == 0:
            rezultat.append(x)
    return rezultat


def test_eliminare_duplicate():
    assert eliminare_duplicate([]) == []
    assert eliminare_duplicate([10, 20, 10, 5, 5, 5, 6]) == [10, 20, 5, 6]
    assert eliminare_duplicate([1, 2, 3]) == [1, 2, 3]
    assert eliminare_duplicate([10, 10, 10, 10]) == [10]


def main():
    test_eliminare_duplicate()
    l = []
    while True:
        menu()
        optiune = int(input("Dati optiunea: "))
        if optiune == 1:
            l = citire_lista()
        elif optiune == 2:
            print(eliminare_duplicate(l))
        elif optiune == 6:
            break
        elif optiune == 0:
            print(l)


main()