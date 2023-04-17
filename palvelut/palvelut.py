import random


class Asiakas:
    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä
        self.asiakasnro = self.luo_nro()

    def luo_nro(self):
        # Luo satunnaisen asiakasnumeron
        num1 = f'{random.randint(0, 9)}{random.randint(0, 9)}'
        num2 = f'{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'
        num3 = f'{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'

        nums = [num1, num2, num3]
        return nums

    def set_nimi(self, nimi):
        # Aseta uusi nimi asiakkaalle
        if not nimi:
            raise ValueError("Uusi nimi on annettava.")
        else:
            self.nimi = nimi

    def get_nimi(self):
        # Palauta asiakkaan nimi
        return self.nimi

    def set_ikä(self, ikä):
        # Aseta uusi ikä asiakkaalle
        if not ikä:
            raise ValueError("Uusi ikä on annettava.")
        else:
            self.ikä = ikä

    def get_ikä(self):
        # Palauta asiakkaan ikä
        return self.ikä

    def get_asiakasnumero(self):
        # Palauta asiakkaan asiakasnumero muodossa "xx-xxx-xxx"
        return f'{self.asiakasnro[0]}-{self.asiakasnro[1]}-{self.asiakasnro[2]}'


class Palvelu:
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.asiakkaat = []

    def luo_asiakasrivi(self, asiakas):
        # Luo asiakkaan tiedot sisältävän merkkijonon
        return f'{asiakas.nimi} ({asiakas.get_asiakasnumero()}) on {asiakas.ikä}-vuotias.'

    def lisää_asiakas(self, asiakas):
        # Lisää uusi asiakas asiakkaat-listaan
        if not asiakas:
            raise ValueError("Uusi asiakas on annettava.")
        else:
            self.asiakkaat.append(asiakas)

    def poista_asiakas(self, asiakas):
        # Poista asiakas asiakkaat-listasta
        self.asiakkaat.append(asiakas)

    def tulosta_asiakkaat(self):
        # Tulosta kaikki asiakkaat käyttäen luo_asiakasrivi-metodia
        print("\nTuotteen {} asiakkaat ovat:".format(self.tuotenimi))
        for asiakas in self.asiakkaat:
            asiakasnro = "-".join(asiakas.asiakasnro)
            print("{nimi} ({asiakasnro}) on {ikä}-vuotias.".format(
                nimi=asiakas.nimi,
                asiakasnro=asiakasnro,
                ikä=asiakas.ikä
            ))
    print()


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.edut = []

    def lisää_etu(self, edu):
        self.edut += [edu]  # Lisätään edu listaan

    def poista_etu(self, edu):
        if edu in self.edut:  # Tarkistetaan, että edu löytyy listalta
            self.edut.remove(edu)  # Poistetaan edu listalta

    def tulosta_edut(self):
        print(f'\nTuotteen {self.tuotenimi} edut ovat:')
        for edu in self.edut:
            # Tulostetaan kaikki edut käymällä läpi edut-lista ja tulostamalla jokainen edu
            print(edu)
