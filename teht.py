import random
import time

""" Luokka, joka kuvaa Olennon """
""" Tästä periytyvät muut luokat tässä tiedostossa """
class Olento:
    def __init__(self, nimi, rohkeus, katseen_voima):
        self.nimi = nimi
        self.rohkeus = rohkeus
        self.katseen_voima = katseen_voima

class Peikko(Olento):
    """Luokka, joka kuvaa Peikon.
    :ivar nimi: peikon nimi, arvotaan
    :type nimi: str
    :ivar rohkeus: peikon rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: peikon katseen voimakkuus, arvotaan
    :type katseen_voima: int
    Julkiset metodit
        arvo_hurraus()
    """

    NIMITAVUT = ("Ur", "Gor", "Groh", "Gur", "Kon", "Kozoh", "Bor", "Bozh", "Rogh", "Rudz")
    RIEMUTAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brar", "Dza", "Gra", "Gur", "Rah", "Urgh", "Ra")

    def __init__(self, nimi='', tyyppi="tavallinen peikko", rohkeus=4, katseen_voima=4):
        """Konstruktori."""
        self.tyyppi = tyyppi
        
        nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        super().__init__(nimi, rohkeus, katseen_voima)
    def _arvo_sanat(self, tavut, n, erotin, p=0.5):
        """Muodostaa satunnaisen tekstin annetuista tavuista.
        :param tavut: ne tavut, joita palautettava teksti voi sisältää
        :type tavut: Union[list[str], tuple[str]]
        :param n: mukaan poimittavien tavujen maksimimäärä
        :type n: int
        :param erotin: tavujen väliin satunnaisesti laitettava merkki
        :type erotin: str
        :param p: todennäköisyys lisätä erotin tavujen väliin (oletus 0.5)
        :type p: float
        :return: satunnainen teksti
        :rtype: str
        """
        osat = random.choices(tavut, k=random.randint(2, n))
        sanat = osat[0]
        for osa in osat[1:]:
            if random.random() < p:
                sanat += erotin + osa
            else:
                sanat += osa.lower()
        return sanat

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.
        :return: hurraava huudahdus
        :rtype: str
        """
        return self._arvo_sanat(self.RIEMUTAVUT, 8, " ", 0.7)

class Vuoripeikko(Peikko):
    """Luokka, joka kuvaa Vuoripeikon.
    :ivar nimi: peikon nimi, arvotaan
    :type nimi: str
    :ivar rohkeus: peikon rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: peikon katseen voimakkuus, arvotaan
    :type katseen_voima: int"""

    NIMITAVUT = ("Yr", "Gry", "Gryh", "Gyr", "Kan", "Kazah", "Bar", "Bazh", "Ragh", "Rydz")
    RIEMUTAVUT = ("Agh", "Ygh", "Oyrgh", "Drar", "Brar", "Dza", "Gra", "Gyr", "Rah", "Yrgh", "Ra")

    def __init__(self):
        """Konstruktori."""
        nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        rohkeus = random.randint(4, 8)
        katseen_voima = random.randint(2, 4)
        tyyppi = "vuoripeikko"

        super().__init__(nimi, tyyppi, rohkeus, katseen_voima)
        

class Luolapeikko(Peikko):
    """Luokka, joka kuvaa Luolapeikon.
    :ivar nimi: peikon nimi, arvotaan
    :type nimi: str
    :ivar rohkeus: peikon rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: peikon katseen voimakkuus, arvotaan
    :type katseen_voima: int"""

    NIMITAVUT = ("Ur", "Gor", "Groh", "Gur", "Kon", "Kozoh", "Bor", "Bozh", "Rogh", "Rudz")
    RIEMUTAVUT = ("Ogh", "Ugh", "Ourgh", "Dror", "Bror", "Dzo", "Gro", "Gur", "Roh", "Urgh", "Ro")

    def __init__(self):
        """Konstruktori."""
        nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        rohkeus = random.randint(4, 8)
        katseen_voima = random.randint(2, 4)
        tyyppi = "luolapeikko"

        super().__init__(nimi, tyyppi, rohkeus, katseen_voima)
        

### Kirjoita luokka Sankari tähän.
class Sankari(Olento):
    """Luokka, joka kuvaa Sankarin.
    :ivar nimi: Sankarin nimi, annetaan parametrina
    :type nimi: str
    :ivar rohkeus: Sankarin rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: Sankarin katseen voimakkuus, arvotaan
    :type katseen_voima: int
    Julkiset metodit
        arvo_hurraus()
    """

    def __init__(self, nimi):
        rohkeus = random.randint(1, 10)
        katseen_voima = random.randint(1, 10)
        
        super().__init__(nimi, rohkeus, katseen_voima)
    def arvo_hurraus(self):
        return random.choice(("Argh", "Wuhuu", "Ärr", "Anggg", "Ungghg"))


def hurraa(olio):
    """Tulostaa satunnaisen hurrauksen annetulle oliolle.
    :param olio: hurraava olio
    """
    print('%s: "%s!"' % (olio.nimi, olio.arvo_hurraus()))


def tulosta_rapaytys(rapayttaja):
    """Tulostaa sopivan tekstin räpäyttävälle oliolle.
    :param rapayttaja: silmiään räpäyttävä olio
    """
    if rapayttaja:
        if rapayttaja.rohkeus > 0:
            print("ja %s räpäyttää!" % rapayttaja.nimi)
        else:
            print("ja %s karkaa!" % rapayttaja.nimi)
    else:
        print("eikä kummankaan silmä rävähdä!")


def tuijota(olio1, olio2):
    """Asettaa annetut oliot taistelemaan keskenään yhden kierroksen.
    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: hävinnyt olio
    :rtype: Union[Sankari, Peikko]
    """
    print("He tuijottavat toisiaan...", end='')
    time.sleep(1)
    # Arvotaan kummankin olion tämän kierroksen vahvuus.
    katse1 = random.randint(0, olio1.katseen_voima)
    katse2 = random.randint(0, olio2.katseen_voima)
    rapayttaja = None

    # heikomman vahvuuden saanut olio menettää rohkeutta
    if katse1 > katse2:
        rapayttaja = olio2
        rapayttaja.rohkeus -= katse1
    elif katse1 < katse2:
        rapayttaja = olio1
        rapayttaja.rohkeus -= katse2
    return rapayttaja


def taistele(vasen, oikea):
    """Asettaa annetut oliot taistelemaan keskenään, kunnes toinen voittaa.
    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: voittanut olio
    :rtype: Union[Sankari, Peikko]
    """
    while vasen.rohkeus > 0 and oikea.rohkeus > 0:
        haviaja = tuijota(vasen, oikea)
        tulosta_rapaytys(haviaja)
        time.sleep(0.5)
    if vasen.rohkeus > 0:
        return vasen
    else:
        return oikea


sankari = Sankari(input("Mikä on sankarimme nimi? "))

pelastetut = 0
# Käydään tuijotuskisoja peikkoja vastaan, kunnes sankari karkaa
while sankari.rohkeus > 0:
    # Tulostetaan kierroksen alkutiedot.
    sankarin_tiedot = sankari.nimi + " [" + str(sankari.rohkeus) + "]"
    print("Sankarimme %s kävelee kohti seikkailua." % sankarin_tiedot)
    time.sleep(0.7)

    peikko_classes = [Peikko, Vuoripeikko, Luolapeikko]
    peikko = peikko_classes[random.randint(0, len(peikko_classes) - 1)]()
    
    peikon_tiedot = f"{peikko.nimi} [{str(peikko.rohkeus)}]"
    print("Vastaan tulee hurja %s, jonka tyyppi on %s!" % (peikon_tiedot, peikko.tyyppi))
    time.sleep(1)

    # Käydään tuijotuskisa peikkoa vastaan.
    voittaja = taistele(peikko, sankari)
    hurraa(voittaja)
    print()
    time.sleep(1.5)

time.sleep(1.5)
print("%s herää sängystään hikisenä - onneksi se oli vain unta!" % sankari.nimi)
