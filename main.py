def menu():
    print("1. Citirea unei liste de numere intregi")
    print("2. Afisarea listei dupa eliminarea duplicatelor")
    print("3. Afisarea sumei primelor n numere pozitive din lista")
    print("4. Verifica daca toate numerele pozitive din lista sunt in ordine crescatoare")
    print("5. Afisarea listei obtinute din lista initiala in care numerele care apar doar o singura data "
          "sunt inlocuite cu numarul de divizori proprii ai numarului")
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
    :param l: o lista de numere intregi
    :return: lista l, dupa ce a eliminat duplicatele
    '''
    rezultat = []
    for x in l:
        ok = 1
        for y in rezultat:
            if x==y:
                ok = 0
        if ok:
            rezultat.append(x)
    return rezultat


def test_eliminare_duplicate():
    '''
    Functie de test
    '''
    assert eliminare_duplicate([]) == []
    assert eliminare_duplicate([10, 20, 10, 5, 5, 5, 6]) == [10, 20, 5, 6]
    assert eliminare_duplicate([1, 2, 3]) == [1, 2, 3]
    assert eliminare_duplicate([10, 10, 10, 10]) == [10]


def suma_primele_n_pozitive(l, n):
    '''
    Determina suma primelor n numere pozitive din lista
    :param l: o lista de numere intregi
    :param n: un numar natural
    :return: suma primelor n numere pozitive din l, sau,
            daca sunt mai putin de n numere pozitive in l, mesajul
            "Dimensiunea listei este prea mica"
    '''
    suma = 0
    for x in l:
        if n > 0 and x >= 0:
            suma = suma + x
            n = n - 1
    if n > 0:
        return "Dimensiunea listei este prea mica"
    else:
        return suma


def test_suma_primele_n_pozitive():
    '''
    Functia de test
    '''
    assert suma_primele_n_pozitive([], 3) == "Dimensiunea listei este prea mica"
    assert suma_primele_n_pozitive([10, -3, 25, -1, 3, 25, 18], 3) == 38
    assert suma_primele_n_pozitive([1,2,3], 5) == "Dimensiunea listei este prea mica"


def verifica_nr_pozitive_ordine_cresc(l):
    '''
    Verifica daca toate numerele pozitive din lista sunt in ordine crescatoare
    :param l: o lista de numere intregi
    :return: "DA", daca toate numerele pozitive din lista sunt in ordine crescatoare,
            "NU" in caz contrar
    '''
    lista_pozitive = []
    for x in l:
        if x >= 0:
            lista_pozitive.append(x)
    for i in range(len(lista_pozitive)-1):
        if lista_pozitive[i]>lista_pozitive[i+1]:
            return "NU"
    return "DA"


def test_verifica_nr_pozitive_ordine_cresc():
    '''
    Functie de test
    '''
    assert verifica_nr_pozitive_ordine_cresc([]) == "DA"
    assert verifica_nr_pozitive_ordine_cresc([-1, -2, -9, -10, -4]) == "DA"
    assert verifica_nr_pozitive_ordine_cresc([10, 13, -1, 24, 33, 45]) == "DA"
    assert verifica_nr_pozitive_ordine_cresc([1, 2, -3, -4, 5, 1, -9]) == "NU"


def modificare_lista(l):
    '''
    Face o noua lista din lista initiala in care numerele care apar doar o singura data
    sunt inlocuite cu numarul de divizori proprii ai numarului
    :param l: o lista de intregi
    :return: lista obtinuta din l prin inlocuirea numerelor care apar doar o singura data
    cu numarul de divizori proprii ai numarului
    '''
    rezultat = []
    for i in range(len(l)):
        x = l[i]
        cate = 0
        for j in range(len(l)):
            if x == l[j]:
                cate = cate + 1
        if cate == 1:
            duplicat = 0
        else:
            duplicat = 1
        if duplicat == 1:
            rezultat.append(x)
        else:
            nr_div = 0
            if x < 0:
                x = x * (-1)
            for j in range(2,x//2+1):
                if x % j == 0:
                    nr_div = nr_div + 1
            rezultat.append(nr_div)
    return rezultat


def test_modificare_lista():
    '''
    Functie de test
    '''
    assert modificare_lista([]) == []
    assert modificare_lista([25, 13, 26, 13, 19]) == [1, 13, 2, 13, 0]
    assert modificare_lista([2, 6, 6, 25]) == [0, 6, 6, 1]



def main():
    test_eliminare_duplicate()
    test_suma_primele_n_pozitive()
    test_verifica_nr_pozitive_ordine_cresc()
    test_modificare_lista()
    l = []
    while True:
        menu()
        optiune = int(input("Dati optiunea: "))
        if optiune == 1:
            l = citire_lista()
        elif optiune == 2:
            print(eliminare_duplicate(l))
        elif optiune == 3:
            n = int(input("Dati numarul: "))
            print(suma_primele_n_pozitive(l, n))
        elif optiune == 4:
            print(verifica_nr_pozitive_ordine_cresc(l))
        elif optiune == 5:
            print(modificare_lista(l))
        elif optiune == 6:
            break
        elif optiune == 0:
            print(l)


main()