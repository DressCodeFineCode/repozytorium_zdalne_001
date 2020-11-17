"""
print('Adrian')

number = 98
python_age = 'dziewięćdziesiąt osiem'
jakis_tekst = 'Adrian Zięba'
jakis_drugi_tekst = jakis_tekst


print('liczba pythona to:', number)
print(f'Nazywam się {jakis_tekst}.')

ta_zmienna_ma_poprawna_nazwe = 2323
T0_JEST_STAŁA = 2323

NAPIS_001 = 'Agnieszka'
NAPIS_002 = "Zięba"
NAPIS_003 = NAPIS_001 + ' ' + NAPIS_002
print(NAPIS_003)

liczba_float = 23.2323
print(type(liczba_float))
print(f'nazwa zmiennej to {(type(liczba_float))}, a brzmi ona {liczba_float}')

print(type(jakis_tekst))

moja_lista = [
    'Pierwszy obiekt',
    'Drugi obiekt',
    'Trzeci obiekt',
    'Pierwszy obiekt'
              ]
print(type(moja_lista))
print(moja_lista)
print(moja_lista[1])

expenditures = {
    'jedzenie':870,
               
    'czynsz':930,
    'remont':232
                }
print(expenditures)
print(type(expenditures))
print(expenditures['jedzenie'])

wartosc_logiczna = False
wartosc_logiczna_2 = None
print(f'Wartość logiczna to {wartosc_logiczna} i wartość logiczna_2 to {wartosc_logiczna_2}')
import random
random.randint(1,10000)
income = random.randint(1,6000)
print(income)
if income > 5000:
    print("Bogaty z ciebie skurwysyn!")

elif 1200 <= income <= 5000:
    print("No dobra, zarabiasz nieźle ale i tak możesz w Niemczech co najwyżej jeść bułkę z masłem.")

else:
    print("Popatrzcie na niego jaki biedak!")





wartosc_int = 23
wartosc_float = 23.13
wartosc_str = '34'

wartosc_float_from_int = float(wartosc_int)
wartosc_int_from_float = int(wartosc_float)
wartosc_str_from_int = str(wartosc_int)
wartość_int_from_str = int(wartosc_str)
wartosc_float_from_str = float(wartosc_str)
print()

print('hejho', 'maciek', sep='23')
print(f'Wartość ktora tu jest to:\t {type(wartosc_float_from_int)}',' i wynosi ona \t {wartosc_float_from_int}.', sep='\t\t' )
print(f'Wartość ktora tu jest to:\t {type(wartosc_int_from_float)}',' i wynosi ona \t {wartosc_int_from_float}.', sep='\t\t' )
print(f'Wartość ktora tu jest to:\t {type(wartosc_str_from_int)}',' i wynosi ona \t {wartosc_str_from_int}.', sep='\t\t' )
print(f'Wartość ktora tu jest to:\t {type(wartość_int_from_str)}',' i wynosi ona \t {wartość_int_from_str}.', sep='\t\t' )
print(f'Wartość ktora tu jest to:\t {type(wartosc_float_from_str)}',' i wynosi ona \t {wartosc_float_from_str}.', sep='\t\t' )
"""
#
# for maciek in range(0,5):
#     print(maciek)
# maciek = 0
# while maciek !=3:
#     print(maciek)
# number = 1
# while number % 2 != 0:
#     number = int(input('Podaj liczbę parzystą:'))
# print('Brawo skurwysynu, udało Ci się!')

# expeditures = [10000000, 1200, 300, 3020, 20, 30, 100000, 320]
#
# for max_expeditures in expeditures:
#
#     if max_expeditures < 10000:
#         continue
#     else:
#         print(max_expeditures)
#
# print('No i koniec')


def funkcja_mnożenia (a,b):
    return print(a*b)
print(funkcja_mnożenia(23,123))
