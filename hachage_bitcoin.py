# -*- coding: utf-8 -*-

import sys
import math
import random
import time

# X^2 = y mod p ?
# trouver x , p nombre premier et entier y , tel que X^2 = y mod p
def verification(x, y, p):
    if (x * x - y) % p == 0:
        return True
    else:
        return False


print(verification(6, 10, 13))



l = [0, 1, 2, 3, 4, 5]
l_nb_premier = [7, 11, 13, 17, 19, 23]  # necessaire pour les blocs


def add_l_croise(l):
    l_add = l.copy()
    for i in range(1, len(l_add), 2):
        l_add[i] = l_add[i - 1] + l_add[i]
    return l_add


def add_l(l1, l2):
    l_add = l1.copy()
    for i in range(0, len(l_add)):
        l_add[i] = l_add[i] + l2[i]
    return l_add


def mul_l(l, list_nb_premier):
    l_multi = l.copy()
    for i in range(0, len(l_multi)):
        l_multi[i] = l_multi[i] * list_nb_premier[i]
    return l_multi


def add_one(l):
    l_add_one = l.copy()
    for i in range(0, len(l_add_one)):
        l_add_one[i] += 1
    return l_add_one


def rotate_right(l):
    mlist = l.copy()
    a = (mlist.pop(len(mlist) - 1))
    l_rotate = [a]
    for i in range(0, len(mlist)):
        l_rotate.append(mlist[i])
    return l_rotate


def modulo_n(l, n):
    l_modulo = l.copy()
    for i in range(0, len(l_modulo)):
        l_modulo[i] = l_modulo[i] % n
    return l_modulo


def bloc(l, l_nb_prmier):
    return modulo_n(rotate_right(add_one(mul_l(add_l_croise(l), l_nb_premier))), 100)


def ascii_to_int(message):
    liste_message = []
    for i in range(0, 5):
        liste_message.append(ord(message[i]))
    return liste_message


def check_liste_bloc_n(l, n):
    if (len(l) % n) == 0:
        return True
    else:
        return False



def dix_tours(l):
    ll = l.copy()
    for i in range(0, 10):
        r = bloc(ll, l_nb_premier)  # 1 tour
        ll = r.copy()
        # print(r)
    return r


def hachage_liste(message_liste):
    l = (message_liste[0: 6])
    for u in range(6, len(message_liste), 6):
        l1 = (message_liste[u: u + 6])
        # print(l, l1)
        a = (dix_tours(l))
        # print(a)
        somme = (modulo_n(add_l(a, l1), 100))
        # print(somme)
        l = somme.copy()
    a = (dix_tours(l))
    # print(a)
    return a


def verification_preuve(liste, preuve, Max):
    vMax = True
    r = hachage_liste(liste + preuve)  # hachage
    for i in range(0, len(Max)):
        if r[i] > Max[i]:
            vMax = False
    return vMax

# creation aleatoire d une preuve de longueur n
def build_preuve(n):
    preuve = []
    for i in range(0, n):
        nb = random.randint(0, 99)
        preuve.append(nb)
    return preuve


l = [0, 1, 2, 3, 4, 5]
print(dix_tours(l))

l = [1, 1, 2, 3, 4, 5]
print(dix_tours(l))

l = [1, 1, 2, 3, 4, 50]
v = [12, 1, 2, 3, 4, 50]

print(modulo_n(add_l(l, v), 100))

message = 'mon message'
print(ascii_to_int(message))

message_ = [0, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10]
print('\n message de longueur multiple de 6  : ')
print(check_liste_bloc_n(message_, 6))
print("resultat du hachage : ")
print(hachage_liste(message_))

Max = [0, 0, 7]
print("verification preuve < Max , Max= ", Max)

message_ = [0, 1, 2, 3, 4, 5, 12, 3, 24, 72, 47, 77]
print('\n message de longueur multiple de 6  : ')
print(check_liste_bloc_n(message_, 6))
print("resultat du hachage : ")
print(hachage_liste(message_))
print("verification preuve < Max")
print('Objectif atteint ? ', verification_preuve([0, 1, 2, 3, 4, 5], [12, 3, 24, 72, 47, 77], [0, 0, 7]))

message_ = [0, 1, 2, 3, 4, 5, 0, 0, 2, 0, 61, 2]
print('\n message de longueur multiple de 6  : ')
print(check_liste_bloc_n(message_, 6))
print("resultat du hachage : ")
print(hachage_liste(message_))
print("verification preuve < Max")
print('Objectif atteint ? ', verification_preuve([0, 1, 2, 3, 4, 5], [0, 0, 2, 0, 61, 2], [0, 0, 7]))

message_ = [0, 1, 2, 3, 4, 5, 97, 49, 93, 87, 89, 47]
print('\n message de longueur multiple de 6  : ')
print(check_liste_bloc_n(message_, 6))
print("resultat du hachage : ")
print(hachage_liste(message_))
print("verification preuve < Max")
print('Objectif atteint ? ', verification_preuve([0, 1, 2, 3, 4, 5], [97, 49, 93, 87, 89, 47], [0, 0, 7]))


def trouve_preuve(message_, longueur_preuve, Max):
    while True:
        preuve = (build_preuve(longueur_preuve))
        r = (verification_preuve(message_, preuve, Max))
        if r:
            break
    return preuve


Max = [0, 0, 7]
longueur_preuve = 6

message_ = [0, 1, 2, 3, 4, 5]
Max = [0, 0, 7]
longueur_preuve = 6
print('********** trouver  preuve **************')
print(f' trouver la preuve pour le message {message_}  avec l objectif  MAx {Max}  ')
start_t = time.perf_counter()
preuve = trouve_preuve(message_, longueur_preuve, Max)
stop_t = time.perf_counter()
print(f'temps : {stop_t - start_t} s')
print(message_, preuve, Max)
print(f' resultat de la preuve {preuve}')
print(f'test preuve {preuve} pour le message {message_} , et l objectif Max {Max} ', 'Objectif atteint ? ',
      verification_preuve(message_, preuve, Max))
print(' le hachage est ', hachage_liste(message_ + preuve), f' avec la preuve {preuve}')

print('********** test preuve **************')
message_ = [0, 1, 2, 3, 4, 5]
Max = [0, 0, 7]
preuve = [12, 3, 24, 72, 47, 77]
print(f'test preuve {preuve} pour le message {message_} , et l objectif Max {Max} ', 'Objectif atteint ? ',
      verification_preuve(message_, preuve, Max))
print(' le hachage est ', hachage_liste(message_ + preuve), f' avec la preuve {preuve}')

print('********** test preuve **************')
message_ = [0, 1, 2, 3, 4, 5]
Max = [0, 0, 7]
preuve = [12, 13, 24, 72, 47, 77]
print(f'test preuve {preuve} pour le message {message_} , et l objectif Max {Max} ', 'Objectif atteint ? ',
      verification_preuve(message_, preuve, Max))
print(' le hachage est ', hachage_liste(message_ + preuve), f' avec la preuve {preuve}')


def ajout_transaction(s):
    Livre.append(s)
    return Livre


def test_ajout_zero(maliste, nb):
    t = len(maliste) % nb
    if t != 0:
        return [0] * (nb - t) + maliste


def phrase_vers_liste(phrase):
    nouvelle_phrase = []
    for c in phrase:
        nouvelle_phrase.append(ord(c) % 100)
    return test_ajout_zero(nouvelle_phrase, 6)


print(' test phrase vers liste  : Vive moi !')
print(phrase_vers_liste('Vive moi !'))


def verification_livre(Max):
    message_ = Livre[-3] + phrase_vers_liste(Livre[-2])
    preuve = Livre[-1]
    print(' le hachage est ', hachage_liste(message_ + preuve), f' avec la preuve {preuve}')
    return verification_preuve(message_, preuve, Max)


def minage(longueur_preuve, Max):
    message_ = phrase_vers_liste(Livre[-1])  # dernier element
    t = Livre[-2]
    t = message_

    preuve = trouve_preuve(Livre[-2] + message_, longueur_preuve, Max)  # avant dernier element
    Livre.append(preuve)
    return preuve


global Livre
Livre = []
Max = [0, 0, 7]
print(f"Max = {Max} ")
preuve_init = [0, 0, 0, 0, 0, 0]
ajout_transaction(preuve_init)
print("transaction 1 ")
transaction = "Abel + 35"

ajout_transaction(transaction)
print("Le livre :", Livre)
print("minage ...")
minage(longueur_preuve, Max)
print("Le livre :", Livre)
print("Verification Livre :")
print(verification_livre(Max))

print("transaction 2")
transaction = "Bob -77"
ajout_transaction(transaction)
print("Le livre :", Livre)
print("minage ...")
minage(longueur_preuve, Max)
print("Le livre :", Livre)
print("Verification Livre :")
print(verification_livre(Max))

print("transaction 3")
transaction = "Camille -25"
ajout_transaction(transaction)
print("Le livre :", Livre)
print("minage ...")
minage(longueur_preuve, Max)
print("Le livre :", Livre)
print("Verification Livre :")
print(verification_livre(Max))

print("Exemples du cours")
Max = [0, 0, 7]
Livre = [[0, 0, 0, 0, 0, 0], 'Abel +35', [71, 15, 6, 8, 29, 7]]
print("Le livre :", Livre)
print(verification_livre(Max))
Livre = [[0, 0, 0, 0, 0, 0], 'Abel +35', [71, 15, 6, 8, 29, 7],'Bob -77', [50,11,6,22,78,93]]
print("Le livre :", Livre)
print(verification_livre(Max))
Livre = [[0, 0, 0, 0, 0, 0], 'Abel +35', [71, 15, 6, 8, 29, 7],'Bob -77', [50,11,6,22,78,93],'Camille -25',[38,2,30,15,18,81]]
print("Le livre :", Livre)
print(verification_livre(Max))
