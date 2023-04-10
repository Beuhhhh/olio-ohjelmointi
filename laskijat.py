class Laskija:

    def summaa(self, a, b):
        return sum([a, b])

    def kerro(self, a, b):
        tulo = 1
        for luku in [a, b]:
            tulo *= luku
        return tulo


# Lisää MonenLaskija ja argumenttien_tulostaja tähän.

class MonenLaskija(Laskija):
    def summaa(self, *args):

        return sum(args)

    def kerro(self, *args):

        tulo = 1
        for num in args:
            tulo *= num
        return tulo


def argumenttien_tulostaja(**args):
    for arg in args.items():
        print(f'Argumentin "{arg[0]}" arvo on {arg[1]}.')

# Seuraavat rivit tekevät tarkistustulostukset. Älä koske niihin.


l = Laskija()
ml = MonenLaskija()

print(l.summaa(11, 31))
print(l.kerro(3, 12))
print()
print(ml.summaa(1, 2, 3, 4, 5))
print(ml.kerro(1, 2, 3, 4, 5))
print()
print(ml.summaa(1, 2, 3, 4, 5, 6, 7))
print(ml.kerro(1, 2, 3, 4, 5, 6, 7))
print()
argumenttien_tulostaja(eka=42, toka='foo', kolmas=[0, 1, 2])
print()
argumenttien_tulostaja(nimi='Tero', ika=41, kaupunki='Turku', oppilaitos='TAI')
