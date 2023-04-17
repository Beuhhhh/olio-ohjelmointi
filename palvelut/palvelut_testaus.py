import random
import palvelut


# Asiakas
a = palvelut.Asiakas('Jompainen', random.randint(20, 30))
b = palvelut.Asiakas('Suvantolainen', random.randint(70, 90))
c = palvelut.Asiakas('Louheatar', random.randint(40, 60))

# Palvelu
p = palvelut.Palvelu('Sammas')

p.lisää_asiakas(a)
p.lisää_asiakas(b)
p.tulosta_asiakkaat()

# ParempiPalvelu
pp = palvelut.ParempiPalvelu('Kirjokansi')

pp.lisää_asiakas(c)
pp.tulosta_asiakkaat()

pp.lisää_etu('Jauhaa rahaa.')
pp.lisää_etu('Jauhaa viljaa.')
pp.lisää_etu('Jauhaa suolaa.')
pp.tulosta_edut()

# Poikkeustapauksien käsittely
print()
pp.poista_etu('Jauhaa kultaa.')
try:
    pp.lisää_asiakas(None)
except ValueError as e:
    print(e)
try:
    a.set_nimi('')
except ValueError as e:
    print(e)
